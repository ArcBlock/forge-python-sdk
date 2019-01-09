

import base64
from rpc import ForgeRpc

# def example():
#     forge_sdk = ForgeSdk.init(path)
#     rpc = forge_sdk.rpc
#     abi_server = forge_sdk.abi_server
#     tornado = Tornado(abi_server)
#     tornado.run()
#     response = rpc.get_chain_info()

def run():
    rpc = ForgeRpc()
    response = rpc.get_chain_info()
    rpc.abcde
    app_hash = base64.b64encode(response.info.app_hash)
    print('Chain info:', response, app_hash)
    print(type(response))

if __name__ == "__main__":
    run()
