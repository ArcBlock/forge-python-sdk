import logging
from datetime import datetime

import event_chain.protos as protos
from event_chain.app.models.states.account import ParticipantAccountState

from forge_sdk import rpc as forge_rpc

logger = logging.getLogger('model-admin')


class User:
    def __init__(self, moniker, passphrase, address=None, data=None):
        self.moniker = moniker
        self.passphrase = passphrase
        if address:
            logger.debug("Loading wallet for {}".format(moniker))
            self.wallet, self.token = self.__load_wallet(address, passphrase)
            self.address = address
        else:
            logger.debug("creating wallet for {}".format(moniker))
            self.address, self.wallet, self.token = self.__init_wallet()
        logger.debug("wallet: {}".format(self.wallet))
        logger.debug("token: {}".format(self.token))
        logger.debug("address: {}".format(self.address))

    def get_wallet(self):
        wallet = protos.WalletInfo()
        wallet.ParseFromString(self.wallet)
        return wallet

    def __init_wallet(self):
        res = forge_rpc.create_wallet(
            moniker=self.moniker,
            passphrase=self.passphrase,
        )
        if res.code != 0:
            logger.error("Creating wallet failed!")
            logger.error(res)
        return res.wallet.address, res.wallet.SerializeToString(), res.token

    def __load_wallet(self, address, passphrase):
        res = forge_rpc.load_wallet(address, passphrase)
        if res.code != 0:
            logger.error(
                "Reloading wallet failed! Please check your passphrase.",
            )
            logger.error(res)
        return res.wallet.SerializeToString(), res.token

    def get_state(self):
        state = get_participant_state(self.address)
        return state

    def poke(self):
        pokeTx = protos.PokeTx(date=str(datetime.utcnow().date()),
                               address='zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz')
        res = forge_rpc.send_itx(type_url='fg:t:poke',
                                 itx=pokeTx,
                                 wallet=self.get_wallet(),
                                 token=self.token,
                                 nonce=0)

        if res.code != 0:
            logger.error("Poke Failed.")
            logger.error(res)
        else:
            logger.debug('Poke successfully.hash: {}'.format(res.hash))


def get_participant_state(participant_address):
    state = forge_rpc.get_single_account_state(participant_address)
    if not state:
        logger.error(
            "Participant {} doesn't exist.".format(participant_address),
        )
    else:
        return ParticipantAccountState(state)
