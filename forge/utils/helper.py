from enum import Enum


class SupportedActions(Enum):
    VERIFY_TX = 'verify_tx'
    UPDATE_STATE = 'update_state'

    @classmethod
    def has_action(cls, value):
        return any(value == item.value for item in cls)


class TxHandler:
    def __init__(self, tx_type, verify_tx_func, update_state_func):
        self.tx_type = tx_type
        self.verify_tx = verify_tx_func
        self.update_state = update_state_func
