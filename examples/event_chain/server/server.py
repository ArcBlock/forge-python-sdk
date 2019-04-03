import logging

from event_chain import protos
from event_chain.application import models

from forge import helper as forge_helper
from forge import utils as forge_utils
from forge.sdk import sdk

logger = logging.getLogger('ec-server')

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
            "Received an verify_reqeust for ExchangeTx not recognized.",
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
        updated_event_info = forge_utils.parse_to_proto(
            updated_event_state.data.value,
            protos.EventInfo,
        )

        # update buyer state
        buyer_address = request.tx.signatures[0].signer
        logger.debug("buyer address :{}".format(buyer_address))

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
    'fg:t:exchange',
    exchange_verify,
    exchange_update,
)

sdk.init_server([exchange_tx_handler])
