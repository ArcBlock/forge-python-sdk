import logging

from examples.event_chain import config
from examples.event_chain import helpers
from examples.event_chain import models
from examples.event_chain import protos
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
        # update event state
        asset_state = models.get_event_state(event_address)
        updated_event_state = asset_state.pop_executed_ticket()
        logger.debug("Event state update is prepared.")

        # update buyer state
        buyer_address = request.tx.signatures[0].key.decode()
        buyer_state = models.get_participant_state(buyer_address)
        ticket_address = exchange_tx.sender.assets[0]
        buyer_state.add_unused_ticket(ticket_address)
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
    helpers.ForgeTxType.EXCHANGE.value,
    exchange_verify,
    exchange_update,
)


def activate_asset_verify(request):
    logger.debug("ActivateAssetTx verify_request has been received.")
    # TODO: should get type_url from parameters
    # Not verifying
    return protos.ResponseVerifyTx(code=OK)


def activate_asset_update(request):
    logger.debug("ActivateAssetTx update_request has been received.")
    activate_itx = forge_utils.parse_to_proto(
        request.tx.itx.value,
        protos.ActivateAssetTx,
    )

    # update ticket state
    ticket_state = models.get_ticket_state(activate_itx.address)
    ticket_state.activate()
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


activate_tx_handler = forge_helper.TxHandler(
    helpers.ForgeTxType.ACTIVATE_ASSET.value,
    activate_asset_verify,
    activate_asset_update,
)


def update_hosted_verify(request):
    logger.debug("UpdateHostedTx needs verify.")
    # verify that tx sender and event creator are the same person
    tx_sender = getattr(request.tx, 'from')
    update_hosted_tx = forge_utils.parse_to_proto(
        request.tx.itx.value,
        protos.UpdateHostedTx,
    )
    event_state = forgeRpc.get_single_asset_state(update_hosted_tx.address)
    if tx_sender == event_state.owner:
        logger.debug("UpdateHostedTx has been verified successfully!")
        return protos.ResponseVerifyTx(code=0)
    else:
        logger.error("Tx sender is not event owner!")
        return protos.ResponseVerifyTx(code=INVALID_SENDER_STATE)


def update_hosted_update(request):
    logger.debug("UpdateHostedTx needs update.")
    update_hosted_tx = forge_utils.parse_to_proto(
        request.tx.itx.value,
        protos.UpdateHostedTx,
    )

    event_address = update_hosted_tx.address
    sender_address = getattr(request.tx, 'from')
    sender_state = models.get_participant_state(sender_address)
    sender_state.add_hosted(event_address)
    updated_sender_state = sender_state.to_state()
    return protos.ResponseUpdateState(
        code=OK,
        states=[updated_sender_state],
    )


update_hosted_tx_handler = forge_helper.TxHandler(
    'ec:t:update_hosted',
    update_hosted_verify,
    update_hosted_update,
)

forgeSdk.register_handler(activate_tx_handler)
forgeSdk.register_handler(exchange_tx_handler)
forgeSdk.register_handler(update_hosted_tx_handler)

if __name__ == "__main__":
    forgeSdk.server.start()
