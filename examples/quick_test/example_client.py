from time import sleep

from google.protobuf.any_pb2 import Any

from forge import ForgeSdk
from forge import protos

sdk = ForgeSdk(handlers={})
rpc = sdk.rpc


def run():
    wallet1 = rpc.create_wallet(moniker='aliceya', passphrase='abc123')
    print(wallet1.wallet)
    sleep(5)

    reqs = [
        protos.RequestGetAccountState(
            address=wallet1.wallet.address,
        ),
    ]

    before_state = rpc.get_account_state(req=reqs.__iter__())
    for i in before_state:
        print('before', i)

    itx = Any(
        type_url='test:t:test',
        value=protos.pythonSDKTx(
            to=wallet1.wallet.address,
            value=100,
        ).SerializeToString(),
    )
    kwargs = {
        'itx': itx,
        'from_address': wallet1.wallet.address,
        'wallet': wallet1.wallet,
        'nonce': 2,
        'token': wallet1.token,
    }
    tx = rpc.create_tx(**kwargs)
    res = rpc.send_tx(tx=tx.tx)
    print(res)

    sleep(5)

    after_state = rpc.get_account_state(req=reqs.__iter__())
    for i in after_state:
        print('after', i.state.moniker)


def wallet_test():
    wallet = rpc.create_wallet(passphrase='abcde1234')
    # wallet1 = rpc.create_wallet(moniker='alice', passphrase='abcde1234')
    print(wallet)

    recovered_wallet = rpc.recover_wallet(
        passphrase='abcde1234', moniker='alice',
        data=wallet.wallet.sk,
    )
    print(recovered_wallet)
    sleep(5)
    account = rpc.get_single_account_state(wallet.wallet.address)
    print(account)


if __name__ == "__main__":
    run()
