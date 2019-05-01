import logging

from forge_sdk import did
from forge_sdk import utils
from forge_sdk.protos import protos
from forge_sdk.rpc.forge_rpc import chain as chain_rpc
from forge_sdk.rpc.forge_rpc import state as state_rpc

logger = logging.getLogger('rpc-helper')


def send_itx(type_url, itx, wallet, token, nonce=1):
    """GRPC call to send inner transaction

    Args:
        type_url(string): type_url for this itx
        itx(:obj:`protos.object`): inner transactions defined in protos
        wallet(:obj:`WalletInfo`): sender's wallet
        token(string): sender's token
        nonce(int): need to be set to 0 if itx is pokeTx

    Returns:
        ResponseSendTx

    """
    encoded_itx = utils.encode_to_any(type_url, itx)
    tx = chain_rpc.create_tx(
        itx=encoded_itx,
        from_address=wallet.address,
        wallet=wallet,
        token=token,
        nonce=nonce
    )
    return chain_rpc.send_tx(tx.tx)


def create_asset(type_url, asset, wallet, token):
    """GRPC call to create asset

    Args:
        type_url(string): type_url for this itx
        asset(object): asset to be included in itx, can be string, bytes,
            or protobuf objects
        wallet(:obj:`WalletInfo`): sender's wallet
        token(string): sender's token

    Returns:
        ResponseSendTx

    """
    encoded_asset = utils.encode_to_any(type_url, asset)
    create_asset_itx = utils.encode_to_any(
        type_url='fg:t:create_asset',
        data=protos.CreateAssetTx(data=encoded_asset),
    )
    tx = chain_rpc.create_tx(
        create_asset_itx, wallet.address, wallet, token,
    )
    return chain_rpc.send_tx(tx.tx)


def update_asset(type_url, address, asset, wallet, token):
    """GRPC call to create asset

    Args:
        type_url(string): type_url for this itx
        address(string): address of asset to update
        asset(object): asset to be updated in itx, can be string, bytes,
            or protobuf objects
        wallet(:obj:`WalletInfo`): sender's wallet
        token(string): sender's token

    Returns:
        ResponseSendTx

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
    """GRPC call to get account state of a single address

    Args:
        address(string): address of the account

    Returns:
        AccountState

    """
    if address:
        accounts = state_rpc.get_account_state({'address': address})
        account = next(accounts)
        if utils.is_proto_empty(account):
            return None
        else:
            return account.state


def get_single_tx_info(hash):
    """GRPC call to get transaction state of a single hash

    Args:
        hash(string): hash of the transaction

    Returns:
        TransactionInfo

    """
    if hash:
        infos = chain_rpc.get_tx(hash)
        info = next(infos)
        if utils.is_proto_empty(info):
            return None
        else:
            return info.info


def get_single_asset_state(address):
    """GRPC call to get asset state of a single address

    Args:
        address(string): address of the asset

    Returns:
        AssetState

    """
    if address:
        assets = state_rpc.get_asset_state({'address': address})
        asset = next(assets)
        if not utils.is_proto_empty(asset):
            return asset.state


def send_deploy_protocol_tx(wallet, token, **kwargs):
    itx = protos.DeployProtocolTx(**kwargs)
    return send_itx("fg:t:deploy_protocol", itx, wallet, token)


def build_tx(itx, wallet, token=None, nonce=1):
    if __is_sk_included(wallet):
        return __build_tx(itx, wallet.address, wallet, nonce)
    else:
        tx_response = chain_rpc.create_tx(itx, wallet.address, wallet, token,
                                          nonce)
        if tx_response.code != 0:
            logger.error(f"Error in creating tx: {tx_response}")
        else:
            return tx_response.tx


def build_multisig(tx, wallet, token=None, data=None):
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
