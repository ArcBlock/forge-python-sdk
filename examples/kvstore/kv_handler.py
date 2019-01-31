import kv_protos

from forge import helper
from forge import protos
from forge import utils


def verify_tx(request):
    kv_tx = utils.parse_to_proto(request.tx.itx.value, kv_protos.KvTx)
    if __is_empty_string(kv_tx.key) or __is_empty_string(kv_tx.value):
        return protos.ResponseVerifyTx(
            code=9,
        )

    sender_state = request.sender
    existing_data = sender_state.data.value
    if existing_data != b'':
        account_kv_state = utils.decode_to_proto(
            sender_state.data.value, kv_protos.AccountKvState,
        )

        for store in account_kv_state:
            if store.kv_pair.key == store.kv_tx.key:
                return protos.ResponseVerifyTx(
                    code=protos.StatusCode.invalid_sender_state,
                )
    else:
        return protos.ResponseVerifyTx(code=0)


def update_state(request):
    kv_tx = utils.parse_to_proto(request.tx.itx.value, kv_protos.KvTx)
    key = kv_tx.key
    value = kv_tx.value
    sender_state = request.sender
    existing_data = sender_state.data.value
    if existing_data != b'':
        account_kv_state = utils.decode_to_proto(
            sender_state.data.value, kv_protos.AccountKvState,
        )
        existing_data = []
        for pair in account_kv_state.store:
            existing_data.append(pair)
        existing_data.append(kv_protos.KVPair(key, value))
        # update sender state
        sender_state.data = utils.encode_to_any(
            request.tx.itx.type_url, account_kv_state,
        )

    else:
        new_pairs = [kv_protos.KVPair(key=key, value=value)]
        new_data = kv_protos.AccountKvState(store=new_pairs)
        new_itx = utils.encode_to_any('kv:t:kv', new_data)
        sender_state = protos.AccountState(
            address=sender_state.address,
            nonce=sender_state.nonce,
            moniker='updated!!!',
            data=new_itx,
        )
    return protos.ResponseUpdateState(
        code=0,
        states=[sender_state],
    )


def init_kv_handler():
    return helper.TxHandler(
        tx_type='kv:t:kv',
        verify_tx_func=verify_tx,
        update_state_func=update_state,
    )


def __is_empty_string(field):
    if not field or str(field).strip() == "":
        return True
    else:
        return False
