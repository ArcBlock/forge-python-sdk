import logging
from datetime import datetime

from forge_sdk import utils
from forge_sdk.protos import protos
from forge_sdk.rpc import helper

logger = logging.getLogger('rpc-poke')


def poke(wallet, token=None):
    """
    Send a Poke Transaction.

    Args:
        token(string): required if the wallet does not have a secret key.

    Returns:
        :obj:`ResponseSendTx`

    Examples:
        >>> from forge_sdk.rpc.forge_rpc import wallet
        >>> alice = wallet.create_wallet(moniker='alice', passphrase='abc123')
        >>> res = poke(alice.wallet)
        >>> assert res.hash

    """
    itx = build_poke_itx()
    nonce = 0
    return helper.send_itx(**locals())


def build_poke_itx():
    poke_tx = protos.PokeTx(date=str(datetime.utcnow().date()),
                            address='zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz')
    return utils.encode_to_any(type_url='fg:t:poke', data=poke_tx)


def build_poke_tx(wallet=None, pk=None, address=None):
    itx = build_poke_itx()
    nonce = 0
    return helper.build_unsigned_tx(**locals())
