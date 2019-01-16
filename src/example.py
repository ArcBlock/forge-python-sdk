from forge_sdk import ForgeSdk

import protos


# def example():
#     forge_sdk = ForgeSdk.init(path)
#     rpc = forge_sdk.rpc
#     abi_server = forge_sdk.abi_server
#     tornado = Tornado(abi_server)
#     tornado.run()
#     response = rpc.get_chain_info()

# user code


def run():
    rpc = ForgeSdk().rpc
    res = rpc.create_wallet(
        protos.RequestCreateWallet(
            type=protos.WalletType(pk=0, hash=1, address=1),
            moniker="jintian", passphrase='abcde123',
        ),
    )
    print(res)


if __name__ == "__main__":
    run()
