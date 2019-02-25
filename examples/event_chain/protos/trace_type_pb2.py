# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: trace_type.proto
import sys

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

from examples.event_chain.protos import type_pb2 as type__pb2
_b = sys.version_info[0] < 3 and (
    lambda x: x
) or (lambda x: x.encode('latin1'))
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name='trace_type.proto',
    package='forge_abi',
    syntax='proto3',
    serialized_options=None,
    serialized_pb=_b('\n\x10trace_type.proto\x12\tforge_abi\x1a\ntype.proto\"(\n\tPageOrder\x12\r\n\x05\x66ield\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\"N\n\tPageInput\x12\x0e\n\x06\x63ursor\x18\x01 \x01(\t\x12\x0c\n\x04size\x18\x02 \x01(\r\x12#\n\x05order\x18\x03 \x03(\x0b\x32\x14.forge_abi.PageOrder\"\x1b\n\nTypeFilter\x12\r\n\x05types\x18\x01 \x03(\t\"<\n\nTimeFilter\x12\x17\n\x0fstart_date_time\x18\x01 \x01(\t\x12\x15\n\rend_date_time\x18\x02 \x01(\t\"1\n\rAddressFilter\x12\x0e\n\x06sender\x18\x01 \x01(\t\x12\x10\n\x08receiver\x18\x02 \x01(\t\"7\n\x08PageInfo\x12\x0e\n\x06\x63ursor\x18\x01 \x01(\t\x12\x0c\n\x04next\x18\x02 \x01(\x08\x12\r\n\x05total\x18\x03 \x01(\r\"\x84\x01\n\x12IndexedTransaction\x12\x0c\n\x04hash\x18\x01 \x01(\t\x12\x0e\n\x06sender\x18\x02 \x01(\t\x12\x10\n\x08receiver\x18\x03 \x01(\t\x12\x0c\n\x04time\x18\x04 \x01(\t\x12\x0c\n\x04type\x18\x05 \x01(\t\x12\"\n\x02tx\x18\x06 \x01(\x0b\x32\x16.forge_abi.Transaction\"\xf5\x02\n\x13IndexedAccountState\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12#\n\x07\x62\x61lance\x18\x02 \x01(\x0b\x32\x12.forge_abi.BigUint\x12\x12\n\nnum_assets\x18\x03 \x01(\x04\x12\x0f\n\x07num_txs\x18\x04 \x01(\x04\x12\r\n\x05nonce\x18\x05 \x01(\x04\x12\x14\n\x0cgenesis_time\x18\x06 \x01(\t\x12\x18\n\x10renaissance_time\x18\x07 \x01(\t\x12\x0f\n\x07moniker\x18\x08 \x01(\t\x12\x15\n\rmigrated_from\x18\t \x01(\t\x12\x13\n\x0bmigrated_to\x18\n \x01(\t\x12\x31\n\x15total_received_stakes\x18\x0b \x01(\x0b\x32\x12.forge_abi.BigUint\x12(\n\x0ctotal_stakes\x18\x0c \x01(\x0b\x32\x12.forge_abi.BigUint\x12*\n\x0etotal_unstakes\x18\r \x01(\x0b\x32\x12.forge_abi.BigUint\"\x86\x01\n\x11IndexedAssetState\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\r\n\x05owner\x18\x02 \x01(\t\x12\x14\n\x0cgenesis_time\x18\x03 \x01(\t\x12\x18\n\x10renaissance_time\x18\x04 \x01(\t\x12\x0f\n\x07moniker\x18\x05 \x01(\t\x12\x10\n\x08readonly\x18\x06 \x01(\x08\"\xba\x01\n\x11IndexedStakeState\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12#\n\x07\x62\x61lance\x18\x02 \x01(\x0b\x32\x12.forge_abi.BigUint\x12\x0e\n\x06sender\x18\x03 \x01(\t\x12\x10\n\x08receiver\x18\x04 \x01(\t\x12\x14\n\x0cgenesis_time\x18\x05 \x01(\t\x12\x18\n\x10renaissance_time\x18\x06 \x01(\t\x12\x0f\n\x07message\x18\x07 \x01(\t\x12\x0c\n\x04type\x18\x08 \x01(\rb\x06proto3'),
    dependencies=[type__pb2.DESCRIPTOR, ],
)


_PAGEORDER = _descriptor.Descriptor(
    name='PageOrder',
    full_name='forge_abi.PageOrder',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='field', full_name='forge_abi.PageOrder.field', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='type', full_name='forge_abi.PageOrder.type', index=1,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
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
    serialized_start=43,
    serialized_end=83,
)


_PAGEINPUT = _descriptor.Descriptor(
    name='PageInput',
    full_name='forge_abi.PageInput',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='cursor', full_name='forge_abi.PageInput.cursor', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='size', full_name='forge_abi.PageInput.size', index=1,
            number=2, type=13, cpp_type=3, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='order', full_name='forge_abi.PageInput.order', index=2,
            number=3, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
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
    serialized_start=85,
    serialized_end=163,
)


_TYPEFILTER = _descriptor.Descriptor(
    name='TypeFilter',
    full_name='forge_abi.TypeFilter',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='types', full_name='forge_abi.TypeFilter.types', index=0,
            number=1, type=9, cpp_type=9, label=3,
            has_default_value=False, default_value=[],
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
    serialized_start=165,
    serialized_end=192,
)


_TIMEFILTER = _descriptor.Descriptor(
    name='TimeFilter',
    full_name='forge_abi.TimeFilter',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='start_date_time', full_name='forge_abi.TimeFilter.start_date_time', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='end_date_time', full_name='forge_abi.TimeFilter.end_date_time', index=1,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
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
    serialized_start=194,
    serialized_end=254,
)


_ADDRESSFILTER = _descriptor.Descriptor(
    name='AddressFilter',
    full_name='forge_abi.AddressFilter',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='sender', full_name='forge_abi.AddressFilter.sender', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='receiver', full_name='forge_abi.AddressFilter.receiver', index=1,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
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
    serialized_start=256,
    serialized_end=305,
)


_PAGEINFO = _descriptor.Descriptor(
    name='PageInfo',
    full_name='forge_abi.PageInfo',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='cursor', full_name='forge_abi.PageInfo.cursor', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='next', full_name='forge_abi.PageInfo.next', index=1,
            number=2, type=8, cpp_type=7, label=1,
            has_default_value=False, default_value=False,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='total', full_name='forge_abi.PageInfo.total', index=2,
            number=3, type=13, cpp_type=3, label=1,
            has_default_value=False, default_value=0,
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
    serialized_start=307,
    serialized_end=362,
)


_INDEXEDTRANSACTION = _descriptor.Descriptor(
    name='IndexedTransaction',
    full_name='forge_abi.IndexedTransaction',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='hash', full_name='forge_abi.IndexedTransaction.hash', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='sender', full_name='forge_abi.IndexedTransaction.sender', index=1,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='receiver', full_name='forge_abi.IndexedTransaction.receiver', index=2,
            number=3, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='time', full_name='forge_abi.IndexedTransaction.time', index=3,
            number=4, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='type', full_name='forge_abi.IndexedTransaction.type', index=4,
            number=5, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='tx', full_name='forge_abi.IndexedTransaction.tx', index=5,
            number=6, type=11, cpp_type=10, label=1,
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
    serialized_start=365,
    serialized_end=497,
)


_INDEXEDACCOUNTSTATE = _descriptor.Descriptor(
    name='IndexedAccountState',
    full_name='forge_abi.IndexedAccountState',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='address', full_name='forge_abi.IndexedAccountState.address', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='balance', full_name='forge_abi.IndexedAccountState.balance', index=1,
            number=2, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='num_assets', full_name='forge_abi.IndexedAccountState.num_assets', index=2,
            number=3, type=4, cpp_type=4, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='num_txs', full_name='forge_abi.IndexedAccountState.num_txs', index=3,
            number=4, type=4, cpp_type=4, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='nonce', full_name='forge_abi.IndexedAccountState.nonce', index=4,
            number=5, type=4, cpp_type=4, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='genesis_time', full_name='forge_abi.IndexedAccountState.genesis_time', index=5,
            number=6, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='renaissance_time', full_name='forge_abi.IndexedAccountState.renaissance_time', index=6,
            number=7, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='moniker', full_name='forge_abi.IndexedAccountState.moniker', index=7,
            number=8, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='migrated_from', full_name='forge_abi.IndexedAccountState.migrated_from', index=8,
            number=9, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='migrated_to', full_name='forge_abi.IndexedAccountState.migrated_to', index=9,
            number=10, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='total_received_stakes', full_name='forge_abi.IndexedAccountState.total_received_stakes', index=10,
            number=11, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='total_stakes', full_name='forge_abi.IndexedAccountState.total_stakes', index=11,
            number=12, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='total_unstakes', full_name='forge_abi.IndexedAccountState.total_unstakes', index=12,
            number=13, type=11, cpp_type=10, label=1,
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
    serialized_start=500,
    serialized_end=873,
)


_INDEXEDASSETSTATE = _descriptor.Descriptor(
    name='IndexedAssetState',
    full_name='forge_abi.IndexedAssetState',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='address', full_name='forge_abi.IndexedAssetState.address', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='owner', full_name='forge_abi.IndexedAssetState.owner', index=1,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='genesis_time', full_name='forge_abi.IndexedAssetState.genesis_time', index=2,
            number=3, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='renaissance_time', full_name='forge_abi.IndexedAssetState.renaissance_time', index=3,
            number=4, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='moniker', full_name='forge_abi.IndexedAssetState.moniker', index=4,
            number=5, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='readonly', full_name='forge_abi.IndexedAssetState.readonly', index=5,
            number=6, type=8, cpp_type=7, label=1,
            has_default_value=False, default_value=False,
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
    serialized_start=876,
    serialized_end=1010,
)


_INDEXEDSTAKESTATE = _descriptor.Descriptor(
    name='IndexedStakeState',
    full_name='forge_abi.IndexedStakeState',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='address', full_name='forge_abi.IndexedStakeState.address', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='balance', full_name='forge_abi.IndexedStakeState.balance', index=1,
            number=2, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='sender', full_name='forge_abi.IndexedStakeState.sender', index=2,
            number=3, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='receiver', full_name='forge_abi.IndexedStakeState.receiver', index=3,
            number=4, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='genesis_time', full_name='forge_abi.IndexedStakeState.genesis_time', index=4,
            number=5, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='renaissance_time', full_name='forge_abi.IndexedStakeState.renaissance_time', index=5,
            number=6, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='message', full_name='forge_abi.IndexedStakeState.message', index=6,
            number=7, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='type', full_name='forge_abi.IndexedStakeState.type', index=7,
            number=8, type=13, cpp_type=3, label=1,
            has_default_value=False, default_value=0,
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
    serialized_start=1013,
    serialized_end=1199,
)

_PAGEINPUT.fields_by_name['order'].message_type = _PAGEORDER
_INDEXEDTRANSACTION.fields_by_name['tx'].message_type = type__pb2._TRANSACTION
_INDEXEDACCOUNTSTATE.fields_by_name['balance'].message_type = type__pb2._BIGUINT
_INDEXEDACCOUNTSTATE.fields_by_name['total_received_stakes'].message_type = type__pb2._BIGUINT
_INDEXEDACCOUNTSTATE.fields_by_name['total_stakes'].message_type = type__pb2._BIGUINT
_INDEXEDACCOUNTSTATE.fields_by_name['total_unstakes'].message_type = type__pb2._BIGUINT
_INDEXEDSTAKESTATE.fields_by_name['balance'].message_type = type__pb2._BIGUINT
DESCRIPTOR.message_types_by_name['PageOrder'] = _PAGEORDER
DESCRIPTOR.message_types_by_name['PageInput'] = _PAGEINPUT
DESCRIPTOR.message_types_by_name['TypeFilter'] = _TYPEFILTER
DESCRIPTOR.message_types_by_name['TimeFilter'] = _TIMEFILTER
DESCRIPTOR.message_types_by_name['AddressFilter'] = _ADDRESSFILTER
DESCRIPTOR.message_types_by_name['PageInfo'] = _PAGEINFO
DESCRIPTOR.message_types_by_name['IndexedTransaction'] = _INDEXEDTRANSACTION
DESCRIPTOR.message_types_by_name['IndexedAccountState'] = _INDEXEDACCOUNTSTATE
DESCRIPTOR.message_types_by_name['IndexedAssetState'] = _INDEXEDASSETSTATE
DESCRIPTOR.message_types_by_name['IndexedStakeState'] = _INDEXEDSTAKESTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PageOrder = _reflection.GeneratedProtocolMessageType(
    'PageOrder', (_message.Message,), dict(
        DESCRIPTOR=_PAGEORDER,
        __module__='trace_type_pb2',
        # @@protoc_insertion_point(class_scope:forge_abi.PageOrder)
    ),
)
_sym_db.RegisterMessage(PageOrder)

PageInput = _reflection.GeneratedProtocolMessageType(
    'PageInput', (_message.Message,), dict(
        DESCRIPTOR=_PAGEINPUT,
        __module__='trace_type_pb2',
        # @@protoc_insertion_point(class_scope:forge_abi.PageInput)
    ),
)
_sym_db.RegisterMessage(PageInput)

TypeFilter = _reflection.GeneratedProtocolMessageType(
    'TypeFilter', (_message.Message,), dict(
        DESCRIPTOR=_TYPEFILTER,
        __module__='trace_type_pb2',
        # @@protoc_insertion_point(class_scope:forge_abi.TypeFilter)
    ),
)
_sym_db.RegisterMessage(TypeFilter)

TimeFilter = _reflection.GeneratedProtocolMessageType(
    'TimeFilter', (_message.Message,), dict(
        DESCRIPTOR=_TIMEFILTER,
        __module__='trace_type_pb2',
        # @@protoc_insertion_point(class_scope:forge_abi.TimeFilter)
    ),
)
_sym_db.RegisterMessage(TimeFilter)

AddressFilter = _reflection.GeneratedProtocolMessageType(
    'AddressFilter', (_message.Message,), dict(
        DESCRIPTOR=_ADDRESSFILTER,
        __module__='trace_type_pb2',
        # @@protoc_insertion_point(class_scope:forge_abi.AddressFilter)
    ),
)
_sym_db.RegisterMessage(AddressFilter)

PageInfo = _reflection.GeneratedProtocolMessageType(
    'PageInfo', (_message.Message,), dict(
        DESCRIPTOR=_PAGEINFO,
        __module__='trace_type_pb2',
        # @@protoc_insertion_point(class_scope:forge_abi.PageInfo)
    ),
)
_sym_db.RegisterMessage(PageInfo)

IndexedTransaction = _reflection.GeneratedProtocolMessageType(
    'IndexedTransaction', (_message.Message,), dict(
        DESCRIPTOR=_INDEXEDTRANSACTION,
        __module__='trace_type_pb2',
        # @@protoc_insertion_point(class_scope:forge_abi.IndexedTransaction)
    ),
)
_sym_db.RegisterMessage(IndexedTransaction)

IndexedAccountState = _reflection.GeneratedProtocolMessageType(
    'IndexedAccountState', (_message.Message,), dict(
        DESCRIPTOR=_INDEXEDACCOUNTSTATE,
        __module__='trace_type_pb2',
        # @@protoc_insertion_point(class_scope:forge_abi.IndexedAccountState)
    ),
)
_sym_db.RegisterMessage(IndexedAccountState)

IndexedAssetState = _reflection.GeneratedProtocolMessageType(
    'IndexedAssetState', (_message.Message,), dict(
        DESCRIPTOR=_INDEXEDASSETSTATE,
        __module__='trace_type_pb2',
        # @@protoc_insertion_point(class_scope:forge_abi.IndexedAssetState)
    ),
)
_sym_db.RegisterMessage(IndexedAssetState)

IndexedStakeState = _reflection.GeneratedProtocolMessageType(
    'IndexedStakeState', (_message.Message,), dict(
        DESCRIPTOR=_INDEXEDSTAKESTATE,
        __module__='trace_type_pb2',
        # @@protoc_insertion_point(class_scope:forge_abi.IndexedStakeState)
    ),
)
_sym_db.RegisterMessage(IndexedStakeState)


# @@protoc_insertion_point(module_scope)
