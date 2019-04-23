from event_chain.app.models.admin import *
from event_chain.app.models.event import *
from event_chain.app.models.mobile import *
from event_chain.app.models.sql import *
from event_chain.app.models.states import *
from event_chain.app.models.ticket import *


class TransactionInfo:
    def __init__(self, state):
        self.height = state.height
        self.hash = state.hash
        self.tx = state.tx
        self.time = state.time
