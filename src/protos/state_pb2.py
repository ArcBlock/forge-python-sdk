# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: state.proto
import sys

from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2

from . import type_pb2 as type__pb2
from . import vendor_pb2 as vendor__pb2
_b = sys.version_info[0] < 3 and (
    lambda x: x
) or (lambda x: x.encode('latin1'))
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name='state.proto',
    package='forge_abi',
    syntax='proto3',
    serialized_options=None,
    serialized_pb=_b('\n\x0bstate.proto\x12\tforge_abi\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x19google/protobuf/any.proto\x1a\x0cvendor.proto\x1a\ntype.proto\"\xbf\x03\n\x0c\x41\x63\x63ountState\x12#\n\x07\x62\x61lance\x18\x01 \x01(\x0b\x32\x12.forge_abi.BigUint\x12\r\n\x05nonce\x18\x02 \x01(\x04\x12\x0f\n\x07num_txs\x18\x03 \x01(\x04\x12\x0f\n\x07\x61\x64\x64ress\x18\x04 \x01(\t\x12\n\n\x02pk\x18\x05 \x01(\x0c\x12#\n\x04type\x18\x06 \x01(\x0b\x32\x15.forge_abi.WalletType\x12\x0f\n\x07moniker\x18\x07 \x01(\t\x12$\n\x04role\x18\x08 \x01(\x0e\x32\x16.forge_abi.AccountRole\x12\x12\n\ngenesis_tx\x18\t \x01(\t\x12\x16\n\x0erenaissance_tx\x18\n \x01(\t\x12\x30\n\x0cgenesis_time\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x34\n\x10renaissance_time\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x13\n\x0bmigrated_to\x18\r \x01(\t\x12\x15\n\rmigrated_from\x18\x0e \x03(\t\x12\r\n\x05power\x18\x0f \x01(\x04\x12\"\n\x04\x64\x61ta\x18\x32 \x01(\x0b\x32\x14.google.protobuf.Any\"\xf5\x01\n\nAssetState\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\r\n\x05owner\x18\x02 \x01(\t\x12\x0f\n\x07moniker\x18\x03 \x01(\t\x12\x12\n\ngenesis_tx\x18\t \x01(\t\x12\x16\n\x0erenaissance_tx\x18\n \x01(\t\x12\x30\n\x0cgenesis_time\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x34\n\x10renaissance_time\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\"\n\x04\x64\x61ta\x18\x32 \x01(\x0b\x32\x14.google.protobuf.Any\"\xf1\x02\n\x0c\x43hannelState\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x17\n\x0ftotal_confirmed\x18\x02 \x01(\x04\x12\x13\n\x0bmax_waiting\x18\x03 \x01(\r\x12\x15\n\rmax_confirmed\x18\x04 \x01(\r\x12+\n\x07waiting\x18\x05 \x03(\x0b\x32\x1a.forge_abi.TransactionInfo\x12&\n\tconfirmed\x18\x06 \x03(\x0b\x32\x13.forge_abi.TxStatus\x12\x12\n\ngenesis_tx\x18\t \x01(\t\x12\x16\n\x0erenaissance_tx\x18\n \x01(\t\x12\x30\n\x0cgenesis_time\x18\x0b \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x34\n\x10renaissance_time\x18\x0c \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\"\n\x04\x64\x61ta\x18\x32 \x01(\x0b\x32\x14.google.protobuf.Any\"\x89\x02\n\nForgeState\x12\x14\n\x0clatest_block\x18\x01 \x01(\x04\x12\x17\n\x0flatest_app_hash\x18\x02 \x01(\x0c\x12\x18\n\x10\x63onsensus_engine\x18\x03 \x01(\t\x12\x16\n\x0estorage_engine\x18\x04 \x01(\t\x12/\n\x05tasks\x18\r \x03(\x0b\x32 .forge_abi.ForgeState.TasksEntry\x12\"\n\x04\x64\x61ta\x18\x0e \x01(\x0b\x32\x14.google.protobuf.Any\x1a\x45\n\nTasksEntry\x12\x0b\n\x03key\x18\x01 \x01(\x04\x12&\n\x05value\x18\x02 \x01(\x0b\x32\x17.forge_abi.UpgradeTasks:\x02\x38\x01\x62\x06proto3'),
    dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR, google_dot_protobuf_dot_any__pb2.DESCRIPTOR, vendor__pb2.DESCRIPTOR, type__pb2.DESCRIPTOR, ],
)


_ACCOUNTSTATE = _descriptor.Descriptor(
    name='AccountState',
    full_name='forge_abi.AccountState',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='balance', full_name='forge_abi.AccountState.balance', index=0,
            number=1, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='nonce', full_name='forge_abi.AccountState.nonce', index=1,
            number=2, type=4, cpp_type=4, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='num_txs', full_name='forge_abi.AccountState.num_txs', index=2,
            number=3, type=4, cpp_type=4, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='address', full_name='forge_abi.AccountState.address', index=3,
            number=4, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='pk', full_name='forge_abi.AccountState.pk', index=4,
            number=5, type=12, cpp_type=9, label=1,
            has_default_value=False, default_value=_b(""),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='type', full_name='forge_abi.AccountState.type', index=5,
            number=6, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='moniker', full_name='forge_abi.AccountState.moniker', index=6,
            number=7, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='role', full_name='forge_abi.AccountState.role', index=7,
            number=8, type=14, cpp_type=8, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='genesis_tx', full_name='forge_abi.AccountState.genesis_tx', index=8,
            number=9, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='renaissance_tx', full_name='forge_abi.AccountState.renaissance_tx', index=9,
            number=10, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='genesis_time', full_name='forge_abi.AccountState.genesis_time', index=10,
            number=11, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='renaissance_time', full_name='forge_abi.AccountState.renaissance_time', index=11,
            number=12, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='migrated_to', full_name='forge_abi.AccountState.migrated_to', index=12,
            number=13, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='migrated_from', full_name='forge_abi.AccountState.migrated_from', index=13,
            number=14, type=9, cpp_type=9, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='power', full_name='forge_abi.AccountState.power', index=14,
            number=15, type=4, cpp_type=4, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='data', full_name='forge_abi.AccountState.data', index=15,
            number=50, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=113,
    serialized_end=560,
)


_ASSETSTATE = _descriptor.Descriptor(
    name='AssetState',
    full_name='forge_abi.AssetState',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='address', full_name='forge_abi.AssetState.address', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='owner', full_name='forge_abi.AssetState.owner', index=1,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='moniker', full_name='forge_abi.AssetState.moniker', index=2,
            number=3, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='genesis_tx', full_name='forge_abi.AssetState.genesis_tx', index=3,
            number=9, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='renaissance_tx', full_name='forge_abi.AssetState.renaissance_tx', index=4,
            number=10, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='genesis_time', full_name='forge_abi.AssetState.genesis_time', index=5,
            number=11, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='renaissance_time', full_name='forge_abi.AssetState.renaissance_time', index=6,
            number=12, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='data', full_name='forge_abi.AssetState.data', index=7,
            number=50, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=563,
    serialized_end=808,
)


_CHANNELSTATE = _descriptor.Descriptor(
    name='ChannelState',
    full_name='forge_abi.ChannelState',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='address', full_name='forge_abi.ChannelState.address', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='total_confirmed', full_name='forge_abi.ChannelState.total_confirmed', index=1,
            number=2, type=4, cpp_type=4, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='max_waiting', full_name='forge_abi.ChannelState.max_waiting', index=2,
            number=3, type=13, cpp_type=3, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='max_confirmed', full_name='forge_abi.ChannelState.max_confirmed', index=3,
            number=4, type=13, cpp_type=3, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='waiting', full_name='forge_abi.ChannelState.waiting', index=4,
            number=5, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='confirmed', full_name='forge_abi.ChannelState.confirmed', index=5,
            number=6, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='genesis_tx', full_name='forge_abi.ChannelState.genesis_tx', index=6,
            number=9, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='renaissance_tx', full_name='forge_abi.ChannelState.renaissance_tx', index=7,
            number=10, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='genesis_time', full_name='forge_abi.ChannelState.genesis_time', index=8,
            number=11, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='renaissance_time', full_name='forge_abi.ChannelState.renaissance_time', index=9,
            number=12, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='data', full_name='forge_abi.ChannelState.data', index=10,
            number=50, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=811,
    serialized_end=1180,
)


_FORGESTATE_TASKSENTRY = _descriptor.Descriptor(
    name='TasksEntry',
    full_name='forge_abi.ForgeState.TasksEntry',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='key', full_name='forge_abi.ForgeState.TasksEntry.key', index=0,
            number=1, type=4, cpp_type=4, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='value', full_name='forge_abi.ForgeState.TasksEntry.value', index=1,
            number=2, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
    ],
    extensions=[
    ],
    nested_types=[],
    enum_types=[
    ],
    serialized_options=_b('8\001'),
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=1379,
    serialized_end=1448,
)

_FORGESTATE = _descriptor.Descriptor(
    name='ForgeState',
    full_name='forge_abi.ForgeState',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='latest_block', full_name='forge_abi.ForgeState.latest_block', index=0,
            number=1, type=4, cpp_type=4, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='latest_app_hash', full_name='forge_abi.ForgeState.latest_app_hash', index=1,
            number=2, type=12, cpp_type=9, label=1,
            has_default_value=False, default_value=_b(""),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='consensus_engine', full_name='forge_abi.ForgeState.consensus_engine', index=2,
            number=3, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='storage_engine', full_name='forge_abi.ForgeState.storage_engine', index=3,
            number=4, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='tasks', full_name='forge_abi.ForgeState.tasks', index=4,
            number=13, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='data', full_name='forge_abi.ForgeState.data', index=5,
            number=14, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
    ],
    extensions=[
    ],
    nested_types=[_FORGESTATE_TASKSENTRY, ],
    enum_types=[
    ],
    serialized_options=None,
    is_extendable=False,
    syntax='proto3',
    extension_ranges=[],
    oneofs=[
    ],
    serialized_start=1183,
    serialized_end=1448,
)

_ACCOUNTSTATE.fields_by_name['balance'].message_type = type__pb2._BIGUINT
_ACCOUNTSTATE.fields_by_name['type'].message_type = type__pb2._WALLETTYPE
_ACCOUNTSTATE.fields_by_name['role'].enum_type = type__pb2._ACCOUNTROLE
_ACCOUNTSTATE.fields_by_name['genesis_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ACCOUNTSTATE.fields_by_name['renaissance_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ACCOUNTSTATE.fields_by_name['data'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_ASSETSTATE.fields_by_name['genesis_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ASSETSTATE.fields_by_name['renaissance_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ASSETSTATE.fields_by_name['data'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_CHANNELSTATE.fields_by_name['waiting'].message_type = type__pb2._TRANSACTIONINFO
_CHANNELSTATE.fields_by_name['confirmed'].message_type = type__pb2._TXSTATUS
_CHANNELSTATE.fields_by_name['genesis_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_CHANNELSTATE.fields_by_name['renaissance_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_CHANNELSTATE.fields_by_name['data'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_FORGESTATE_TASKSENTRY.fields_by_name['value'].message_type = type__pb2._UPGRADETASKS
_FORGESTATE_TASKSENTRY.containing_type = _FORGESTATE
_FORGESTATE.fields_by_name['tasks'].message_type = _FORGESTATE_TASKSENTRY
_FORGESTATE.fields_by_name['data'].message_type = google_dot_protobuf_dot_any__pb2._ANY
DESCRIPTOR.message_types_by_name['AccountState'] = _ACCOUNTSTATE
DESCRIPTOR.message_types_by_name['AssetState'] = _ASSETSTATE
DESCRIPTOR.message_types_by_name['ChannelState'] = _CHANNELSTATE
DESCRIPTOR.message_types_by_name['ForgeState'] = _FORGESTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AccountState = _reflection.GeneratedProtocolMessageType(
    'AccountState', (_message.Message,), dict(
        DESCRIPTOR=_ACCOUNTSTATE,
        __module__='state_pb2',
        # @@protoc_insertion_point(class_scope:forge_abi.AccountState)
    ),
)
_sym_db.RegisterMessage(AccountState)

AssetState = _reflection.GeneratedProtocolMessageType(
    'AssetState', (_message.Message,), dict(
        DESCRIPTOR=_ASSETSTATE,
        __module__='state_pb2',
        # @@protoc_insertion_point(class_scope:forge_abi.AssetState)
    ),
)
_sym_db.RegisterMessage(AssetState)

ChannelState = _reflection.GeneratedProtocolMessageType(
    'ChannelState', (_message.Message,), dict(
        DESCRIPTOR=_CHANNELSTATE,
        __module__='state_pb2',
        # @@protoc_insertion_point(class_scope:forge_abi.ChannelState)
    ),
)
_sym_db.RegisterMessage(ChannelState)

ForgeState = _reflection.GeneratedProtocolMessageType(
    'ForgeState', (_message.Message,), dict(

        TasksEntry=_reflection.GeneratedProtocolMessageType(
            'TasksEntry', (_message.Message,), dict(
                DESCRIPTOR=_FORGESTATE_TASKSENTRY,
                __module__='state_pb2',
                # @@protoc_insertion_point(class_scope:forge_abi.ForgeState.TasksEntry)
            ),
        ),
        DESCRIPTOR=_FORGESTATE,
        __module__='state_pb2',
        # @@protoc_insertion_point(class_scope:forge_abi.ForgeState)
    ),
)
_sym_db.RegisterMessage(ForgeState)
_sym_db.RegisterMessage(ForgeState.TasksEntry)


_FORGESTATE_TASKSENTRY._options = None
# @@protoc_insertion_point(module_scope)
