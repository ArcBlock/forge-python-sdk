import logging

from . import lib
from forge_sdk import utils
from forge_sdk.protos import protos

logger = logging.getLogger('rpc-poke')


def build_transfer_itx(to, value=None, assets=None, data=None):
    value = utils.value_to_biguint(value)
    return utils.encode_to_any(
        type_url="fg:t:transfer",
        data=protos.TransferTx(**locals()))


def build_transfer_tx(**kwargs):
    transfer_itx = build_transfer_itx(
        to=kwargs.get('to'),
        value=kwargs.get('value'),
        assets=kwargs.get('assets'),
        data=kwargs.get('data')
    )
    return lib.build_unsigned_tx(itx=transfer_itx,
                                 nonce=1,
                                 wallet=kwargs.get('wallet'),
                                 pk=kwargs.get('pk'),
                                 address=kwargs.get('address'),
                                 chain_id=kwargs.get('chain_id'))
