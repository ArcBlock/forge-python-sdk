import logging

from forge_sdk import utils
from forge_sdk.protos import protos
from forge_sdk.rpc import helper

logger = logging.getLogger('rpc-poke')


def transfer(transfer_tx, wallet, token=None):
    """
    Send a Transfer transaction.

    Args:
        transfer_tx(:obj:`TransferTx`): transfer inner transaction
        wallet(:obj:`WalletInfo`): wallet of the sender
        token(string): required if the wallet does not have a secret key.

    Returns:
        :obj:`ResponseSendTx`

    Examples:
        >>> from forge_sdk.rpc.forge_rpc import wallet
        >>> alice = wallet.create_wallet(moniker='alice', passphrase='abc123')
        >>> mike = wallet.create_wallet(moniker='mike', passphrase='abc123')
        >>> transfer_tx = protos.TransferTx(to=mike.wallet.address, value =
        utils.int_to_biguint(10))
        >>> res = transfer(transfer_tx, alice.wallet)
        >>> assert res.hash

    """
    return helper.send_itx(type_url='fg:t:transfer', tx=transfer_tx,
                           wallet=wallet,
                           token=token)


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
    return helper.build_unsigned_tx(itx=transfer_itx,
                                    nonce=1,
                                    wallet=kwargs.get('wallet'),
                                    pk=kwargs.get('pk'),
                                    address=kwargs.get('address'))
