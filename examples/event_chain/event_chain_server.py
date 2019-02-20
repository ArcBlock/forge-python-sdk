import logging

import models
import protos

from forge import ForgeSdk
from forge import helper as forge_helper
from forge import utils as forge_utils

logger = logging.getLogger(__name__)

forgeSdk = ForgeSdk()
forgeRpc = forgeSdk.rpc


def update_event_verify(request):
    logger.info("update_event tranaction has been verified by forge-app.")
    return protos.ResponseVerifyTx(code=0)


def update_event_update(request):
    logger.info("forge-app has received update request.")
    update_event_itx = forge_utils.parse_to_proto(
        request.tx.itx.value,
        protos.UpdateEventTx,
    )
    asset_address = update_event_itx.address
    event_asset = forgeRpc.get_single_asset_state(asset_address)
    asset_state = models.EventAssetState(event_asset)
    updated_state = asset_state.pop_executed_ticket()

    return protos.ResponseUpdateState(
        code=0,
        assets=[updated_state],
    )


exchange_tx_handler = forge_helper.TxHandler(
    'ec:t:update_event',
    update_event_verify,
    update_event_update,
)
forgeSdk.register_handler(exchange_tx_handler)

if __name__ == "__main__":
    forgeSdk.server.start()
