from forge_sdk import ForgeSdk


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
    response = rpc.get_chain_info()
    # app_hash = base64.b64encode(response.info.app_hash)
    print('Chain info:', response)
    # print('Search: ', rpc.search(key='1', value='2'))
    # wallet rpc
    print('list_wallet: ')
    for i in rpc.list_wallets():
        print(i)


if __name__ == "__main__":
    run()
