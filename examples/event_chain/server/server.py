import logging

from event_chain import protos
from event_chain.application import models
from event_chain.config import config

from forge import ForgeSdk
from forge import helper as forge_helper
from forge import utils as forge_utils

logger = logging.getLogger('ec-server')
forgeSdk = ForgeSdk(config=config.forge_config)
forgeRpc = forgeSdk.rpc

INVALID_SENDER_STATE = protos.StatusCode.Value('invalid_sender_state')
OK = protos.StatusCode.Value('ok')


def exchange_verify(request):
    logger.debug("ExchangeTx verify_request has been received.")
    # TODO: should get type_url from parameters
    exchange_tx = forge_utils.parse_to_proto(
        request.tx.itx.value,
        protos.ExchangeTx,
    )
    if exchange_tx.data.type_url == "ec:x:event_address":
        event_address = exchange_tx.data.value.decode('utf8')
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
        event_address = exchange_tx.data.value.decode('utf8')
        logger.debug(
            "ExchangeTx contains an event address {}".format(
                event_address,
            ),
        )
        # update event state
        asset_state = models.get_event_state(event_address)
        logger.debug("Price before popping: {}".format(
            asset_state.event_info.ticket_price,
        ))
        updated_event_state = asset_state.pop_executed_ticket()
        updated_event_info = forge_utils.parse_to_proto(
            updated_event_state.data.value,
            protos.EventInfo,
        )
        logger.debug("Price after popping: {}".format(
            updated_event_info.ticket_price,
        ))
        logger.debug("Event state update is prepared.")

        # update buyer state
        buyer_address = request.tx.signatures[0].signer
        logger.debug("buyer address :{}".format(buyer_address))

        buyer_state = models.get_participant_state(buyer_address)
        logger.debug(
            "buyer unused tickets before :{}".format(buyer_state.unused),
        )

        ticket_address = exchange_tx.sender.assets[0]
        buyer_state.add_unused_ticket(ticket_address)
        logger.debug(
            "buyer unused tickets after :{}".format(buyer_state.unused),
        )

        updated_buyer_state = buyer_state.to_state()

        logger.debug("buyer state update is prepared.")

        return protos.ResponseUpdateState(
            code=0,
            assets=[updated_event_state],
            states=[updated_buyer_state],
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


def consume_asset_verify(request):
    logger.debug("ConsumeAsset verify_request has been received.")
    # Not verifying
    return protos.ResponseVerifyTx(code=OK)


def consume_asset_update(request):
    logger.debug("ConsumeAsset update_request has been received.")
    activate_itx = forge_utils.parse_to_proto(
        request.tx.itx.value,
        protos.ConsumeAssetTx,
    )

    # update ticket state
    ticket_state = models.get_ticket_state(activate_itx.address)
    updated_ticket_state = ticket_state.to_state()
    logger.debug("Ticket state update is prepared.")

    # update buyer state
    buyer_state = models.get_participant_state(getattr(request.tx, 'from'))
    buyer_state.remove_unused_ticket(ticket_state.address)
    buyer_state.add_used_ticket(ticket_state.address)
    buyer_state.add_participated(ticket_state.event_address)
    updated_buyer_state = buyer_state.to_state()
    return protos.ResponseUpdateState(
        code=OK,
        assets=[updated_ticket_state],
        states=[updated_buyer_state],
    )


consume_tx_handler = forge_helper.TxHandler(
    'fg:t:consume_asset',
    consume_asset_verify,
    consume_asset_update,
)

forgeSdk.register_handler(exchange_tx_handler)
