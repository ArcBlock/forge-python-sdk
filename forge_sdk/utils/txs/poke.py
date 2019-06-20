import logging
from datetime import datetime

from . import lib
from forge_sdk import utils
from forge_sdk.protos import protos

logger = logging.getLogger('rpc-poke')


def build_poke_itx(encoded=True):
    poke_tx = protos.PokeTx(date=str(datetime.utcnow().date()),
                            address='zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz')
    res = poke_tx if not encoded else utils.encode_to_any(
        type_url='fg:t:poke', data=poke_tx)
    return res


def build_poke_tx(chain_id, wallet=None, pk=None, address=None):
    itx = build_poke_itx()
    nonce = 0
    return lib.build_unsigned_tx(**locals())
