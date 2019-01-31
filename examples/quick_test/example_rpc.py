from time import sleep

from forge import ForgeRpc

FORGE_TEST_SOCKET = 'unix:///tmp/.forge_test/core/socks/forge_grpc.sock'


def run():
    rpc = ForgeRpc(socket=FORGE_TEST_SOCKET)

    wallet1 = rpc.create_wallet(moniker='aliceya', passphrase='abc123')
    # wallet2 = rpc.create_wallet(moniker='lucia', passphrase='abc123')
    sleep(2)

    reqs = [
        {'address': wallet1.wallet.address},
        {'address': 'abcdhash'},
    ]
    # req = {'address': wallet1.wallet.address}
    # req2 = protos.RequestGetAccountState(
    #     address=wallet1.wallet.address, keys=['moniker', 'num_txs'],
    # )

    states = rpc.get_account_state(reqs)
    print([i for i in states])


if __name__ == "__main__":
    run()
