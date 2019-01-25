from . import kv_protos
from forge import helper
from forge import protos
from forge import utils


def verify_tx(request):
    kv_tx = utils.parse_to_proto(request.tx.itx.value, kv_protos.KvTx)
    if __is_empty_string(kv_tx.key) or __is_empty_string(kv_tx.value):
        return protos.ResponseVerifyTx(
            code=protos.StatusCode.insufficient_data,
        )

    sender_state = request.sender
    account_kv_state = utils.decode_to_proto(
        sender_state.data, kv_protos.AccountKvState,
    )

    for kv_pair in account_kv_state.store:
        if kv_pair.key == kv_tx.key:
            return protos.ResponseVerifyTx(
                code=protos.StatusCode.invalid_sender_state,
            )
    return protos.ResponseVerifyTx(code=protos.StatusCode.ok)


def update_state(request):
    kv_tx = utils.parse_to_proto(request.tx.itx.value, kv_protos.KvTx)
    key = kv_tx.key
    value = kv_tx.value
    sender_state = request.sender
    account_kv_state = utils.decode_to_proto(
        sender_state.data, kv_protos.AccountKvState,
    )

    # if store is decoded to list. modify sender.state.data
    account_kv_state.store.append(kv_protos.KVPair(key, value))

    # update sender state
    updated_sender_state = sender_state
    updated_sender_state.data = utils.encode_to_any(
        request.tx.itx.type_url, account_kv_state,
    )

    return protos.ResponseUpdateState(
        code=protos.StatusCode.ok,
        states=[updated_sender_state],
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
