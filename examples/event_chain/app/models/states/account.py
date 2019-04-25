import event_chain.protos as protos
from event_chain.app import utils

from forge_sdk.utils import utils as forge_utils


class ParticipantAccountState:

    def __init__(self, state):
        self.balance = state.balance
        self.nonce = state.nonce
        self.num_txs = state.num_txs
        self.address = state.address
        self.pk = state.pk
        self.type = state.type
        self.moniker = state.moniker
        self.issuer = state.issuer
        self.context = state.context
        self.migrated_to = state.migrated_to
        self.migrated_from = state.migrated_from
        self.num_assets = state.num_assets
        self.stake = state.stake
        self.pinned_files = state.pinned_files

        self.display_balance = forge_utils.bytes_to_int(
            self.balance.value) / 1e16

        self.participant_info = forge_utils.parse_to_proto(
            state.data.value,
            protos.ParticipantInfo,
        )
        self.hosted = self.participant_info.hosted
        self.participated = self.participant_info.participated
        self.unused = self.participant_info.unused
        self.used = self.participant_info.used

    def to_state(self):
        participant_info = protos.ParticipantInfo(
            hosted=self.hosted,
            participated=self.participated,
            unused=self.unused,
            used=self.used,
        )

        state = protos.AccountState(
            balance=self.balance,
            nonce=self.nonce,
            num_txs=self.num_txs,
            address=self.address,
            pk=self.pk,
            type=self.type,
            moniker=self.moniker,
            issuer=self.issuer,
            context=self.context,
            migrated_to=self.migrated_to,
            migrated_from=self.migrated_from,
            num_assets=self.num_assets,
            stake=self.stake,
            pinned_files=self.pinned_files,
            data=forge_utils.encode_to_any(
                'ec:s:participant_info',
                participant_info,
            ),
        )
        return state

    def add_participated(self, address):
        self.participated = utils.add_to_proto_list(
            address,
            self.participated,
        )

    def add_unused_ticket(self, address):
        self.unused = utils.add_to_proto_list(address, self.unused)

    def remove_unused_ticket(self, address):
        self.unused = utils.remove_from_proto_list(address, self.unused)

    def add_used_ticket(self, address):
        self.used = utils.add_to_proto_list(address, self.used)
