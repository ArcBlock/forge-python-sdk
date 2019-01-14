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
    rpc = ForgeSdk(
        "/Users/shi/projects/Arcblock/forge/tools/forge_sdk/priv"
        "/forge.toml",
    ).rpc
    response = rpc.get_chain_info()
    # app_hash = base64.b64encode(response.info.app_hash)
    print('Chain info:', response)
    # print('Search: ', rpc.search(key='1', value='2'))
    # wallet rpc
    res = rpc.wallet.create_wallet(
        protos.RequestCreateWallet(
            type=protos.WalletType(pk=0, hash=1, address=1),
            moniker="jintian", passphrase='abcde123',
        ),
    )
    print(res)


if __name__ == "__main__":
    run()
