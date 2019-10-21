import base64

import base58
from forge_sdk import did
from forge_sdk import protos, utils
from forge_sdk.mcrypto import Hasher


def multibase_b58encode(data):
    """
    Follow forge's base58 encode convention to encode bytes.

    Args:
        data(bytes): data to be encoded

    Returns:
        string

    Examples:
        >>> multibase_b58encode(b'hello')
        'zCn8eVZg'
    """
    raw = base58.b58encode(data)
    return 'z' + raw.decode()


def multibase_b58decode(data):
    """
    Follow forge's base58 encode convention to decode string

    Args:
        data(string): encoded string

    Returns:
        bytes

    Examples:
        >>> multibase_b58decode('zCn8eVZg')
        b'hello'

    """
    if data.startswith('z'):
        return base58.b58decode((data[1:]).encode())
    raise ValueError('{} cannot be decoded by multibase'
                     ' base58.'.format(str(data)))


def multibase_b64encode(data):
    """
    Follow forge's base64 urlsafe encode convention to encode bytes

    Args:
        data(bytes): data to be encoded

    Returns:
        string

    Examples:
        >>> multibase_b64encode(b'hello')
        'aGVsbG8'
    """
    if isinstance(data, str):
        data = data.encode()
    return base64.urlsafe_b64encode(data).decode().rstrip('=')


def multibase_b64decode(data):
    """
    Follow forge's base64 urlsafe encode convention to decode string

    Args:
        data(string): encoded string

    Returns: bytes

    Examples:
        >>> multibase_b64decode('aGVsbG8')
        b'hello'
    """

    if isinstance(data, str):
        data = data.encode()
    return base64.urlsafe_b64decode(
            (data + b'=' * (-len(data) % 4)))


def is_sk_exist(wallet):
    return wallet.sk and not wallet.sk == b''


def hash_data(data, wallet, rd=None):
    if isinstance(data, protos.Transaction):
        data = data.SerializeToString()
    did_type = did.AbtDid.parse_type_from_did(wallet.address, rd=rd)
    return did_type.hasher.hash(data)


def sign_data(data, wallet, rd=None):
    did_type = did.AbtDid.parse_type_from_did(wallet.address, rd=rd)
    return did_type.signer.sign(data, wallet.sk)


def to_asset_address(itx):
    """
    Calculate asset address for provided CreateAssetTx

    Args:
        did_address(string): user's did address to create this asset
        itx(:obj:`google.protobuf.any`): encoded createAssetTx

    Returns:
        asset_address(string)

    Examples:
        >>> from forge_sdk import protos, utils
        >>> itx = protos.CreateAssetTx(data=utils.encode_to_any(None,b'123'))
        >>> res = to_asset_address(itx)

    """
    data = itx.SerializeToString()
    asset_did = did.AbtDid(role_type='asset', form='short')
    asset_address = asset_did.pk_to_did(data)
    return asset_address


def to_stake_address(addr1, addr2):
    hasher = Hasher('sha3')
    hash = hasher.hash((addr1 + addr2).encode())
    stake_did = did.AbtDid(role_type='stake', form='short')
    stake_address = stake_did.hash_to_did(hash)
    return stake_address


def to_tether_address(hash):
    tether_did = did.AbtDid(role_type='tether',
                            hash_type='sha2', round=1, form='short')
    return tether_did.hash_to_did(hash)


def to_delegate_address(addr1, addr2):
    data = (addr1 + addr2).encode()
    delegate_did = did.AbtDid(role_type='delegate', form='short')
    return delegate_did.hash_to_did(Hasher('sha3').hash(data))


def to_tx_address(tx):
    tx_did = did.AbtDid(role_type='tx',
                        form='short')
    tx_hash = Hasher('sha3').hash(tx.SerializeToString())
    return tx_did.hash_to_did(tx_hash)
