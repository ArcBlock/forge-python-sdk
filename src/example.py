import base64
from forge_sdk import ForgeSdk
# def example():
#     forge_sdk = ForgeSdk.init(path)
#     rpc = forge_sdk.rpc
#     abi_server = forge_sdk.abi_server
#     tornado = Tornado(abi_server)
#     tornado.run()
#     response = rpc.get_chain_info()


def simple_rpc_example():
    forge_sdk = ForgeSdk()
    rpc = forge_sdk.rpc
    response = rpc.get_chain_info()
    app_hash = base64.b64encode(response.info.app_hash)
    print('Chain info:', response, app_hash)


if __name__ == "__main__":
    simple_rpc_example()
