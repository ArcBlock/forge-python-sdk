import logging

from forge_sdk import did
from forge_sdk import utils
from forge_sdk.protos import protos
from forge_sdk.rpc.forge_rpc import chain as chain_rpc
from forge_sdk.rpc.forge_rpc import state as state_rpc

logger = logging.getLogger('rpc-helper')


def send_itx(type_url, tx, wallet, token, nonce=1):
    """
    GRPC call to send inner transaction

    Args:
        type_url(string): type_url for this itx
        tx(:obj:`protos.object`): transactions defined in protos
        wallet(:obj:`WalletInfo`): sender's wallet
        token(string): sender's token
        nonce(int): need to be set to 0 if itx is pokeTx

    Returns:
        :obj:`ResponseSendTx`

    """
    encoded_itx = utils.encode_to_any(type_url, tx)
    tx = build_tx(
        itx=encoded_itx,
        wallet=wallet,
        token=token,
        nonce=nonce
    )
    return chain_rpc.send_tx(tx)


def create_asset(type_url, asset, wallet, token=None, **kwargs):
    """
    GRPC call to create asset
    Create asset on the chain. If asset address is not provided in kwargs,
    sdk will calculate and fill the asset address.

    Args:
        type_url(string): type_url for this itx
        asset(object): asset to be included in itx, can be string, bytes,
            or protobuf objects
        wallet(:obj:`WalletInfo`): sender's wallet
        token(string): sender's token

    Returns:
        :obj:`ResponseSendTx`, string

    """

    encoded_asset = utils.encode_to_any(type_url, asset)
    params = {
        'moniker': kwargs.get('moniker'),
        'readonly': kwargs.get('readonly'),
        'transferrable': kwargs.get('transferrable'),
        'ttl': kwargs.get('ttl'),
        'parent': kwargs.get('parent'),
        'data': encoded_asset,
    }
    if not kwargs.get('address'):
        itx_no_address = protos.CreateAssetTx(**params)
        asset_address = did.get_asset_address(wallet.address,
                                              itx_no_address)
        params['address'] = asset_address
    else:
        params['address'] = kwargs.get('address')
    itx = protos.CreateAssetTx(**params)

    tx = build_tx(
        utils.encode_to_any('fg:t:create_asset', itx), wallet, token,
    )
    res = chain_rpc.send_tx(tx)
    return res, itx.address


def update_asset(type_url, address, asset, wallet, token):
    """
    GRPC call to create asset

    Args:
        type_url(string): type_url for this itx
        address(string): address of asset to update
        asset(object): asset to be updated in itx, can be string, bytes,
            or protobuf objects
        wallet(:obj:`WalletInfo`): sender's wallet
        token(string): sender's token

    Returns:
        :obj:`ResponseSendTx`
        """

    encoded_asset = utils.encode_to_any(type_url, asset)
    update_asset_itx = utils.encode_to_any(
        type_url='fg:t:update_asset',
        data=protos.UpdateAssetTx(
            address=address,
            data=encoded_asset,
        ),
    )
    tx = chain_rpc.create_tx(
        update_asset_itx, wallet.address, wallet, token,
    )
    return chain_rpc.send_tx(tx.tx)


def get_single_account_state(address):
    """
    GRPC call to get account state of a single address

    Args:
        address(string): address of the account

    Returns:
        :obj:`AccountState`

    """
    if address:
        accounts = state_rpc.get_account_state({'address': address})
        account = next(accounts)
        if utils.is_proto_empty(account):
            return None
        else:
            return account.state


def get_single_tx_info(hash):
    """
    GRPC call to get transaction state of a single hash

    Args:
        hash(string): hash of the transaction

    Returns:
        :obj:`TransactionInfo`

    """
    if hash:
        infos = chain_rpc.get_tx(hash)
        info = next(infos)
        if utils.is_proto_empty(info):
            return None
        else:
            return info.info


def get_single_asset_state(address):
    """
    GRPC call to get asset state of a single address

    Args:
        address(string): address of the asset

    Returns:
        :obj:`AssetState`

    """
    if address:
        assets = state_rpc.get_asset_state({'address': address})
        asset = next(assets)
        if not utils.is_proto_empty(asset):
            return asset.state


def build_tx(itx, wallet, token=None, nonce=1):
    """
    Build a transaction for user. If wallet has secret key, use the provided
    secret key to sign transaction; otherwise, it's assumed that this wallet
    is created and kept on forge, and sdk will ask forge to sign the
    transaction with provided token.

    Args:
        itx(:obj:`google.protobuf.any`): encoded itx with type_url
        wallet(:obj:`WalletInfo`): wallet to build the tx
        token(string): only required if wallet doesn't include secret key
        nonce(int): required to be 0 if building a PokeTx

    Returns:
        :obj:`Transaction`

    """
    if __is_sk_included(wallet):
        return __build_tx(itx, wallet, nonce)
    else:
        tx_response = chain_rpc.create_tx(itx, wallet.address, wallet, token,
                                          nonce)
        if tx_response.code != 0:
            logger.error(f"Error in creating tx: {tx_response}")
        else:
            return tx_response.tx


def build_multisig(tx, wallet, token=None, data=None):
    """
    Build a multisig for transaction. If wallet has secret key, use the provided
    secret key to sign transaction; otherwise, it's assumed that this wallet
    is created and kept on forge, and sdk will ask forge to sign the
    transaction with provided token.

    Args:
        tx(:obj:`Transaction`): transaction that needs multi-signed
        wallet(:obj:`WalletInfo`): wallet to build the tx
        token(string): only required if wallet doesn't include secret key
        data(bytes): extra data to be included in the multisig

    Returns:
        :obj:`Transaction`

    """
    if __is_sk_included(wallet):
        return __build_multisig(tx, wallet, data)
    else:
        return chain_rpc.multisig(tx, wallet, token, data)


def __is_sk_included(wallet):
    assert (type(wallet) == protos.WalletInfo)
    return wallet.sk and wallet.sk == b''


def __build_tx(itx, wallet, nonce):
    __chain_id = chain_rpc.get_chain_info().info.network
    params = {
        'from': wallet.address,
        'nonce': nonce,
        'chain_id': __chain_id,
        'pk': wallet.pk,
        'itx': itx
    }
    params['signature'] = __sign_tx(wallet.address,
                                    protos.Transaction(**params))
    return protos.Transaction(**params)


def __build_multisig(tx, wallet, data):
    params = {
        'from': getattr(tx, 'from'),
        'nonce': tx.nonce,
        'chain_id': tx.chain_id,
        'pk': tx.pk,
        'signature': tx.signature,
        'itx': tx.itx,
        'signatures': protos.Multisig(
            signer=wallet.address,
            pk=wallet.pk,
            data=data,
        )
    }
    unmultisig_tx = protos.Transaction(**params)
    params['signatures'] = protos.Multisig(
        signer=wallet.address,
        pk=wallet.pk,
        signature=__sign_tx(wallet.address, unmultisig_tx),
        data=data
    )
    return protos.Transaction(**params)


def __sign_tx(did_address, tx):
    did_type = did.AbtDid.parse_type_from_did(did_address)
    tx_hash = did_type.hasher.hash(tx.SerializeToString())
    signature = did_type.signer.sign(tx_hash)
    return signature
