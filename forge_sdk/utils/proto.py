import json
import logging
from datetime import datetime

from forge_sdk import protos
from forge_sdk.utils import conversion
from google.protobuf.any_pb2 import Any
from google.protobuf.timestamp_pb2 import Timestamp

logger = logging.getLogger('forge-utils')

PROTO_TYPE_URL = {
    'CreateAssetTx': 'fg:t:create_asset',
    'UpdateAssetTx': 'fg:t:update_asset',
    'AcquireAssetTx': 'fg:t:acquire_asset',
    'ConsumeAssetTx': 'fg:t:consume_asset',

    'DelegateTx': 'fg:t:delegate',
    'DeclareTx': 'fg:t:declare',
    'RevokeDelegateTx': 'fg:t:revoke_delegate',
    'AccountMigrateTx': 'fg:t:account_migrate',

    'TransferTx': 'fg:t:transfer',
    'ExchangeTx': 'fg:t:exchange',

    'DeployProtocolTx': 'fg:t:deploy_protocol',
    'UpgradeNodeTx': 'fg:t:upgrade_node',
    'ActivateProtocolTx': 'fg:t:activate_protocol',
    'DeactivateProtocolTx': 'fg:t:deactivate_protocol',

    'DepositTokenTx': 'fg:t:deposit_token',
    'WithdrawTokenTx': 'fg:t:withdraw_token',
    'ApproveWithdrawTx': 'fg:t:approve_withdraw',
    'RevokeWithdrawTx': 'fg:t:revoke_withdraw',

    'PokeTx': 'fg:t:poke',
    'AssetFactory': 'fg:x:asset_factory',
}


def parse_to_proto(binary, proto_message):
    '''
    Parse bytes to given proto message

    Args:
        binary(bytes): serialized value of proto message
        proto_message(:obj:`'objects`): proto message objects

    Returns:
        :obj:`'objects`

    Examples:
        >>> from forge_sdk import protos
        >>> serialized = 'TransferTx(to='mike address').SerializeToString()
        >>> tx = parse_to_proto(serialized, 'TransferTx)
        >>> tx.to
        'mike address'

    '''
    result = proto_message()
    result.ParseFromString(binary)
    return result


def encode_to_any(type_url, data):
    '''
    Encode the provided data into :obj:`protobuf.Any`. This function encodes
    string with UTF-8, integer with helper function `int_to_bytes`, and proto
    messages with internal `SerializeToString()` method.

    Args:
        type_url(string): the type_url to encode the data with. This will be
            the `type_url` field of final result.
        data(bytes or tx): the data to encode. This will be the `value`
        field of
            final result.

    Returns:
        :obj:`Any`

    Examples:
        >>> res = encode_to_any('test_string','test')
        >>> res.type_url
        'test_string
        >>> res.value
        b'test'

    '''
    if isinstance(data, str):
        value = data.encode()
    elif isinstance(data, int):
        value = conversion.int_to_bytes(data)
    elif isinstance(data, bytes):
        value = data
    else:
        value = data.SerializeToString()

    return Any(
            type_url=type_url,
            value=value
    )


def to_any(data, type_url=None):
    name = type(data).__name__
    if name == 'str' and is_valid_json(data):
        type_url = 'fg:x:json'
    else:
        type_url = PROTO_TYPE_URL.get(name, type_url)

    if not type_url:
        logger.error(f'Please provide a type_url for {name}.')
    else:
        return encode_to_any(type_url, data)


def is_valid_json(data):
    try:
        json.loads(data)
        return True
    except ValueError as e:
        return False


def from_any(data):
    if data.type_url == 'fg:x:json':
        return json.loads(data.value)
    for name, url in PROTO_TYPE_URL.items():
        if url == data.type_url:
            return parse_to_proto(data.value, getattr(protos, name))
    logger.error(f'Fail to decode type_url: {data.type_url}')
    return


def is_proto_empty(proto_message):
    '''
    Check if proto message is empty

    Args:
        proto_message(:obj:`proto.objects`): proto objects

    Returns:
        bool

    Examples:
        >>> is_proto_empty('DeclareTx())
        True
        >>> is_proto_empty('TransferTx(to='mike'))
        False
    '''
    return proto_message.SerializeToString() == b''


def proto_time(time):
    t = Timestamp()
    if isinstance(time, datetime):
        return t.FromDatetime(time)
    elif isinstance(time, int):
        return t.FromSeconds(time)
    elif isinstance(time, Timestamp):
        return time
    else:
        logger.error(
                f'{time} is not a valid timestamp. Please provide a datetime, '
                f'unix_timestamp, or google.protobuf.Timestamp format of '
                f'time.')
