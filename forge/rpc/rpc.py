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
    encoded_itx = utils.encode_to_any(type_url, itx)
    tx = create_tx(
        itx=encoded_itx, from_address=wallet.address,
        wallet=wallet, token=token, nonce=nonce
    )
    return send_tx(tx.tx)


def create_asset(type_url, asset, wallet, token):
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
    if address:
        accounts = get_account_state({'address': address})
        account = next(accounts)
        if utils.is_proto_empty(account):
            return None
        else:
            return account.state


def get_single_tx_info(hash):
    if hash:
        infos = get_tx(hash)
        info = next(infos)
        if utils.is_proto_empty(info):
            return None
        else:
            return info.info


def get_single_asset_state(address):
    if address:
        assets = get_asset_state({'address': address})
        asset = next(assets)
        if not utils.is_proto_empty(asset):
            return asset.state


def get_nonce(address):
    account = get_single_account_state(address)
    return account.nonce


def multisig_consume_asset_tx(tx, wallet, token, data):
    return multisig(tx, wallet, token, data=data)
