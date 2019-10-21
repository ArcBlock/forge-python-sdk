from datetime import datetime

from forge_sdk import protos
from forge_sdk.utils import conversion as conversion_util, \
    crypto as crypto_util, proto as proto_util


def create_asset_itx(data, **kwargs):
    itx = protos.CreateAssetTx(
            moniker=kwargs.get('moniker'),
            readonly=kwargs.get('readonly', False),
            transferrable=kwargs.get('transferrable', True),
            ttl=kwargs.get('ttl'),
            parent=kwargs.get('parent'),
            data=data,
    )
    address = crypto_util.to_asset_address(itx)
    itx.address = address
    return itx


def update_asset_itx(address, data, **kwargs):
    itx = protos.UpdateAssetTx(
            moniker=kwargs.get('moniker'),
            address=address,
            data=data
    )
    return itx


def consume_asset_itx(issuer, **kwargs):
    itx = protos.ConsumeAssetTx(
            issuer=issuer,
            address=kwargs.get('address'),
            data=kwargs.get('data')
    )
    return itx


def transfer_itx(to, **kwargs):
    value = kwargs.get('value')
    if isinstance(value, int):
        value = conversion_util.int_to_biguint(value)

    itx = protos.TransferTx(
            to=to,
            value=value,
            assets=kwargs.get('assets'),
            data=kwargs.get('data')
    )
    return itx


def declare_itx(moniker, **kwargs):
    itx = protos.DeclareTx(
            moniker=moniker,
            issuer=kwargs.get('issuer'),
            data=kwargs.get('data')
    )
    return itx


def account_migrate_itx(address, pk, **kwargs):
    itx = protos.AccountMigrateTx(
            address=address,
            pk=pk,
            data=kwargs.get('data')
    )
    return itx


def delegate_itx(to, **kwargs):
    itx = protos.DelegateTx(
            to=to,
            ops=kwargs.get('ops'),
            data=kwargs.get('data')
    )
    sender = kwargs.get('wallet').address
    itx.address = crypto_util.to_delegate_address(sender, to)
    return itx


def revoke_delegate_itx(to, **kwargs):
    itx = protos.RevokeDelegateTx(
            to=to,
            type_urls=kwargs.get('type_urls'),
            data=kwargs.get('data')
    )
    sender = kwargs.get('wallet').address
    itx.address = crypto_util.to_delegate_address(sender, to)
    return itx


def poke_itx(**kwargs):
    itx = protos.PokeTx(
            date=str(datetime.utcnow().date()),
            address='zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz'
    )
    return itx


def exchange_itx(sender, receiver, **kwargs):
    itx = protos.ExchangeTx(
            to=kwargs.get('to'),
            sender=sender,
            receiver=receiver,
            expired_at=proto_util.proto_time(kwargs.get('expired_at')),
            data=kwargs.get('data')
    )
    return itx


def exchange_info(value=None, assets=None):
    if isinstance(value, int):
        value = conversion_util.int_to_biguint(value)
    if isinstance(assets, str):
        assets = [assets]
    return protos.ExchangeInfo(value=value,
                               assets=assets)

def activate_protocol_itx(address, **kwargs):
    itx = protos.ActivateProtocolTx(
            address=address,
            data=kwargs.get('data')
    )
    return itx

def deactivate_protocol_itx(address, **kwargs):
    itx = protos.DeactivateProtocolTx(
            address=address,
            data=kwargs.get('data')
    )
    return itx

def upgrade_node_itx(height, version, **kwargs):
    itx = protos.UpgradeNodeTx(
            height=height,
            version=version,
            overwrite=kwargs.get('overwrite', False),
    )
    return itx
