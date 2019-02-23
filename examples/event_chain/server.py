import logging

from . import models
from . import protos
from forge import ForgeSdk
from forge import helper as forge_helper
from forge import utils as forge_utils

logger = logging.getLogger('ec-server')
forgeSdk = ForgeSdk()
forgeRpc = forgeSdk.rpc


def exchange_verify(request):
    logger.debug("ExchangeTx verify_request has been received.")
    # TODO: should get type_url from parameters
    exchange_tx = forge_utils.parse_to_proto(
        request.tx.itx.value,
        protos.ExchangeTx,
    )
    if exchange_tx.data.type_url == "ec:x:event_address":
        event_address = exchange_tx.data.value.decode()
        logger.debug(
            "ExchangeTx contains an event address {}".format(
                event_address,
            ),
        )
    else:
        logger.error(
            "Received an update_reqeust for ExchangeTx not recognized.",
        )

    return protos.ResponseVerifyTx(code=0)


def exchange_update(request):
    logger.debug("ExchangeTx update_request has been received.")
    exchange_tx = forge_utils.parse_to_proto(
        request.tx.itx.value,
        protos.ExchangeTx,
    )

    if exchange_tx.data.type_url == "ec:x:event_address":
        event_address = exchange_tx.data.value.decode()
        logger.debug(
            "ExchangeTx contains an event address {}".format(
                event_address,
            ),
        )
        state = forgeRpc.get_single_asset_state(event_address)
        asset_state = models.EventAssetState(state)
        updated_state = asset_state.pop_executed_ticket()
        return protos.ResponseUpdateState(
            code=0,
            assets=[updated_state],
        )
    else:
        logger.error(
            "Received an update_reqeust for ExchangeTx not recognized.",
        )

    return protos.ResponseUpdateState(code=0)


exchange_tx_handler = forge_helper.TxHandler(
    'fg:t:exchange',
    exchange_verify,
    exchange_update,
)
forgeSdk.register_handler(exchange_tx_handler)


def activate_asset_verify(request):
    logger.debug("ActivateAssetTx verify_request has been received.")
    # TODO: should get type_url from parameters
    # Not verifying
    return protos.ResponseVerifyTx(code=0)


def activate_asset_update(request):
    logger.debug("ActivateAssetTx update_request has been received.")
    activate_itx = forge_utils.parse_to_proto(
        request.tx.itx.value,
        protos.ActivateAssetTx,
    )

    state = forgeRpc.get_single_asset_state(activate_itx.address)
    asset_state = models.TicketAssetState(state)
    asset_state.is_used = True
    asset_state.activated = True
    updated_state = asset_state.to_state()
    return protos.ResponseUpdateState(
        code=0,
        assets=[updated_state],
    )


activate_tx_handler = forge_helper.TxHandler(
    'fg:t:activate_asset',
    activate_asset_verify,
    activate_asset_update,
)
forgeSdk.register_handler(activate_tx_handler)

if __name__ == "__main__":
    forgeSdk.server.start()
