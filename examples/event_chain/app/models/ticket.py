import logging

from event_chain.app.models.states.asset import TicketAssetState

from forge_sdk import rpc as forge_rpc

logger = logging.getLogger('model-ticket')


def get_ticket_state(ticket_address):
    state = forge_rpc.get_single_asset_state(ticket_address)
    if not state:
        logger.error("Ticket {} doesn't exist.".format(ticket_address))
    else:
        return TicketAssetState(state)
