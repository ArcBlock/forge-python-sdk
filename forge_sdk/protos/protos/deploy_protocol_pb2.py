# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: deploy_protocol.proto
import sys

from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_b = sys.version_info[0] < 3 and (
    lambda x: x) or (lambda x: x.encode('latin1'))
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name='deploy_protocol.proto',
    package='forge_abi',
    syntax='proto3',
    serialized_options=None,
    serialized_pb=_b('\n\x15\x64\x65ploy_protocol.proto\x12\tforge_abi\x1a\x19google/protobuf/any.proto\",\n\x08\x43odeInfo\x12\x10\n\x08\x63hecksum\x18\x01 \x01(\x0c\x12\x0e\n\x06\x62inary\x18\x02 \x01(\x0c\"\'\n\x08TypeUrls\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x0e\n\x06module\x18\x02 \x01(\t\"\x8b\x02\n\x10\x44\x65ployProtocolTx\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07version\x18\x03 \x01(\r\x12\x11\n\tnamespace\x18\x04 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12&\n\ttype_urls\x18\x06 \x03(\x0b\x32\x13.forge_abi.TypeUrls\x12\r\n\x05proto\x18\x07 \x01(\t\x12\x10\n\x08pipeline\x18\x08 \x01(\t\x12\x0f\n\x07sources\x18\t \x03(\t\x12!\n\x04\x63ode\x18\n \x03(\x0b\x32\x13.forge_abi.CodeInfo\x12\"\n\x04\x64\x61ta\x18\x0f \x01(\x0b\x32\x14.google.protobuf.Anyb\x06proto3'),
    dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR, ])


_CODEINFO = _descriptor.Descriptor(
    name='CodeInfo',
    full_name='forge_abi.CodeInfo',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='checksum', full_name='forge_abi.CodeInfo.checksum', index=0,
            number=1, type=12, cpp_type=9, label=1,
            has_default_value=False, default_value=_b(""),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='binary', full_name='forge_abi.CodeInfo.binary', index=1,
            number=2, type=12, cpp_type=9, label=1,
            has_default_value=False, default_value=_b(""),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
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
    serialized_start=63,
    serialized_end=107,
)


_TYPEURLS = _descriptor.Descriptor(
    name='TypeUrls',
    full_name='forge_abi.TypeUrls',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='url', full_name='forge_abi.TypeUrls.url', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='module', full_name='forge_abi.TypeUrls.module', index=1,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
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
    serialized_start=109,
    serialized_end=148,
)


_DEPLOYPROTOCOLTX = _descriptor.Descriptor(
    name='DeployProtocolTx',
    full_name='forge_abi.DeployProtocolTx',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='address', full_name='forge_abi.DeployProtocolTx.address', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='name', full_name='forge_abi.DeployProtocolTx.name', index=1,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='version', full_name='forge_abi.DeployProtocolTx.version', index=2,
            number=3, type=13, cpp_type=3, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='namespace', full_name='forge_abi.DeployProtocolTx.namespace', index=3,
            number=4, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='description', full_name='forge_abi.DeployProtocolTx.description', index=4,
            number=5, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='type_urls', full_name='forge_abi.DeployProtocolTx.type_urls', index=5,
            number=6, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='proto', full_name='forge_abi.DeployProtocolTx.proto', index=6,
            number=7, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='pipeline', full_name='forge_abi.DeployProtocolTx.pipeline', index=7,
            number=8, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='sources', full_name='forge_abi.DeployProtocolTx.sources', index=8,
            number=9, type=9, cpp_type=9, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='code', full_name='forge_abi.DeployProtocolTx.code', index=9,
            number=10, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='data', full_name='forge_abi.DeployProtocolTx.data', index=10,
            number=15, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
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
    serialized_start=151,
    serialized_end=418,
)

_DEPLOYPROTOCOLTX.fields_by_name['type_urls'].message_type = _TYPEURLS
_DEPLOYPROTOCOLTX.fields_by_name['code'].message_type = _CODEINFO
_DEPLOYPROTOCOLTX.fields_by_name['data'].message_type = google_dot_protobuf_dot_any__pb2._ANY
DESCRIPTOR.message_types_by_name['CodeInfo'] = _CODEINFO
DESCRIPTOR.message_types_by_name['TypeUrls'] = _TYPEURLS
DESCRIPTOR.message_types_by_name['DeployProtocolTx'] = _DEPLOYPROTOCOLTX
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CodeInfo = _reflection.GeneratedProtocolMessageType('CodeInfo', (_message.Message,), dict(
    DESCRIPTOR=_CODEINFO,
    __module__='deploy_protocol_pb2'
    # @@protoc_insertion_point(class_scope:forge_abi.CodeInfo)
))
_sym_db.RegisterMessage(CodeInfo)

TypeUrls = _reflection.GeneratedProtocolMessageType('TypeUrls', (_message.Message,), dict(
    DESCRIPTOR=_TYPEURLS,
    __module__='deploy_protocol_pb2'
    # @@protoc_insertion_point(class_scope:forge_abi.TypeUrls)
))
_sym_db.RegisterMessage(TypeUrls)

DeployProtocolTx = _reflection.GeneratedProtocolMessageType('DeployProtocolTx', (_message.Message,), dict(
    DESCRIPTOR=_DEPLOYPROTOCOLTX,
    __module__='deploy_protocol_pb2'
    # @@protoc_insertion_point(class_scope:forge_abi.DeployProtocolTx)
))
_sym_db.RegisterMessage(DeployProtocolTx)


# @@protoc_insertion_point(module_scope)
