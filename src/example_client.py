from forge_sdk import ForgeSdk
from google.protobuf.any_pb2 import Any

import protos


def run():
    sdk = ForgeSdk(handlers={})
    rpc = sdk.rpc

    wallet1 = rpc.create_wallet(moniker='aliceya', passphrase='abc123')
    print(wallet1)

    reqs = [
        protos.RequestGetAccountState(
            address='zzzYFfYydmBU616jD3BW319tzKB6',
        ),
    ]

    before_state = rpc.get_account_state(req=reqs.__iter__())
    for i in before_state:
        print('before', i.state.num_txs)

    itx = Any(
        type_url='tx/test',
        value=protos.pythonSDKTx(
            to='zzzYFfYydmBU616jD3BW319tzKB6',
            value=100,
        ).SerializeToString(),
    )
    kwargs = {
        'itx': itx,
        'from_address': wallet1.wallet.address,
        'nonce': 1,
        'wallet': wallet1.wallet,
        'token': wallet1.token,
    }
    tx = rpc.create_tx(**kwargs).tx
    res = rpc.send_tx(tx=tx)
    print(res)

    after_state = rpc.get_account_state(req=reqs.__iter__())
    for i in after_state:
        print('after', i.state.num_txs)


if __name__ == "__main__":
    run()
