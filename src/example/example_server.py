import utils
from forge_sdk import ForgeSdk
from forge_sdk import TxHandler

import protos


def run():
    def tx_test_verify_tx(request):
        itx = utils.parse_to_proto(request.tx.itx.value, protos.pythonSDKTx)
        if itx.value != 100:
            print("Wrong value!")
            return protos.ResponseVerifyTx(code=1)
        else:
            print("Tranaction is verified!")
            return protos.ResponseVerifyTx(code=0)

    def tx_test_update_state(request):
        itx = utils.parse_to_proto(request.tx.itx.value, protos.pythonSDKTx)
        new_account_state = protos.AccountState(
            address=itx.to,
            moniker='changedbyriley',
        )
        return protos.ResponseUpdateState(
            code=0,
            states=[new_account_state],
        )

    test_handler = TxHandler(
        tx_type='tx/test',
        verify_tx_func=tx_test_verify_tx,
        update_state_func=tx_test_update_state,
    )

    sdk = ForgeSdk(handlers=[test_handler])
    server = sdk.server
    server.start()


if __name__ == "__main__":
    run()
