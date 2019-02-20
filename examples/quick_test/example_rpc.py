from forge import ForgeRpc

FORGE_TEST_SOCKET = '127.0.0.1:27210'
rpc = ForgeRpc(FORGE_TEST_SOCKET)


def run():
    rpc = ForgeRpc(FORGE_TEST_SOCKET)
    wallet = rpc.create_wallet(passphrase='abdd123')
    print(wallet)


if __name__ == "__main__":
    res = rpc.get_single_asset_state("123dfdad")
    print(res.SerializeToString())
