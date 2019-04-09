import logging
from inspect import getmembers
from inspect import isfunction

from forge import protos
from forge import utils
from forge.rpc import chain
from forge.rpc import event
from forge.rpc import file
from forge.rpc import state
from forge.rpc import statistic
from forge.rpc import wallet

logger = logging.getLogger('forge-rpc')


def __get_module_functions(module):
    return {item[0]: getattr(module, item[0]) for item in
            getmembers(module, isfunction)}


__all_services = {**__get_module_functions(chain),
                  **__get_module_functions(state),
                  **__get_module_functions(event),
                  **__get_module_functions(file),
                  **__get_module_functions(wallet),
                  **__get_module_functions(statistic)}

for name, func in __all_services.items():
    vars()[name] = func


__wallet_type = protos.WalletType(pk=0, hash=1, address=1)


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
    tx = create_tx(
        itx=encoded_itx, from_address=wallet.address,
        wallet=wallet, token=token, nonce=nonce
    )
    return send_tx(tx.tx)


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
    tx = create_tx(
        create_asset_itx, wallet.address, wallet, token,
    )
    return send_tx(tx.tx)


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
    tx = create_tx(
        update_asset_itx, wallet.address, wallet, token,
    )
    return send_tx(tx.tx)


def get_single_account_state(address):
    """GRPC call to get account state of a single address

    Args:
        address(string): address of the account

    Returns:
        AccountState

    """
    if address:
        accounts = get_account_state({'address': address})
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
        infos = get_tx(hash)
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
        assets = get_asset_state({'address': address})
        asset = next(assets)
        if not utils.is_proto_empty(asset):
            return asset.state
