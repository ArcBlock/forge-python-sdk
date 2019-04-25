# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: abi.proto
import sys

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

from . import enum_pb2 as enum__pb2
from . import state_pb2 as state__pb2
from . import type_pb2 as type__pb2
_b = sys.version_info[0] < 3 and (
    lambda x: x) or (lambda x: x.encode('latin1'))
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name='abi.proto',
    package='forge_abi',
    syntax='proto3',
    serialized_options=None,
    serialized_pb=_b('\n\tabi.proto\x12\tforge_abi\x1a\nenum.proto\x1a\ntype.proto\x1a\x0bstate.proto\"\xff\x01\n\x0fRequestVerifyTx\x12\"\n\x02tx\x18\x01 \x01(\x0b\x32\x16.forge_abi.Transaction\x12\'\n\x06states\x18\x02 \x03(\x0b\x32\x17.forge_abi.AccountState\x12%\n\x06\x61ssets\x18\x03 \x03(\x0b\x32\x15.forge_abi.AssetState\x12%\n\x06stakes\x18\x04 \x03(\x0b\x32\x15.forge_abi.StakeState\x12\'\n\x07\x63ontext\x18\x05 \x01(\x0b\x32\x16.forge_abi.AbciContext\x12(\n\tapp_state\x18\x0f \x01(\x0b\x32\x15.forge_abi.ForgeState\"7\n\x10ResponseVerifyTx\x12#\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x15.forge_abi.StatusCode\"\x82\x02\n\x12RequestUpdateState\x12\"\n\x02tx\x18\x01 \x01(\x0b\x32\x16.forge_abi.Transaction\x12\'\n\x06states\x18\x02 \x03(\x0b\x32\x17.forge_abi.AccountState\x12%\n\x06\x61ssets\x18\x03 \x03(\x0b\x32\x15.forge_abi.AssetState\x12%\n\x06stakes\x18\x04 \x03(\x0b\x32\x15.forge_abi.StakeState\x12\'\n\x07\x63ontext\x18\x05 \x01(\x0b\x32\x16.forge_abi.AbciContext\x12(\n\tapp_state\x18\x0f \x01(\x0b\x32\x15.forge_abi.ForgeState\"\xdb\x01\n\x13ResponseUpdateState\x12#\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x15.forge_abi.StatusCode\x12\'\n\x06states\x18\x02 \x03(\x0b\x32\x17.forge_abi.AccountState\x12%\n\x06\x61ssets\x18\x03 \x03(\x0b\x32\x15.forge_abi.AssetState\x12%\n\x06stakes\x18\x04 \x03(\x0b\x32\x15.forge_abi.StakeState\x12(\n\tapp_state\x18\x0f \x01(\x0b\x32\x15.forge_abi.ForgeState\"$\n\x0bRequestInfo\x12\x15\n\rforge_version\x18\x01 \x01(\t\"3\n\x0cResponseInfo\x12\x11\n\ttype_urls\x18\x01 \x03(\t\x12\x10\n\x08\x61pp_hash\x18\x02 \x01(\x0c\"\xa2\x01\n\x07Request\x12/\n\tverify_tx\x18\x01 \x01(\x0b\x32\x1a.forge_abi.RequestVerifyTxH\x00\x12\x35\n\x0cupdate_state\x18\x02 \x01(\x0b\x32\x1d.forge_abi.RequestUpdateStateH\x00\x12&\n\x04info\x18\x03 \x01(\x0b\x32\x16.forge_abi.RequestInfoH\x00\x42\x07\n\x05value\"\xa6\x01\n\x08Response\x12\x30\n\tverify_tx\x18\x01 \x01(\x0b\x32\x1b.forge_abi.ResponseVerifyTxH\x00\x12\x36\n\x0cupdate_state\x18\x02 \x01(\x0b\x32\x1e.forge_abi.ResponseUpdateStateH\x00\x12\'\n\x04info\x18\x03 \x01(\x0b\x32\x17.forge_abi.ResponseInfoH\x00\x42\x07\n\x05value2}\n\x0b\x46orgeAppRpc\x12\x36\n\x0bprocess_one\x12\x12.forge_abi.Request\x1a\x13.forge_abi.Response\x12\x36\n\x07process\x12\x12.forge_abi.Request\x1a\x13.forge_abi.Response(\x01\x30\x01\x62\x06proto3'),
    dependencies=[enum__pb2.DESCRIPTOR, type__pb2.DESCRIPTOR, state__pb2.DESCRIPTOR, ])


_REQUESTVERIFYTX = _descriptor.Descriptor(
    name='RequestVerifyTx',
    full_name='forge_abi.RequestVerifyTx',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='tx', full_name='forge_abi.RequestVerifyTx.tx', index=0,
            number=1, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='states', full_name='forge_abi.RequestVerifyTx.states', index=1,
            number=2, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='assets', full_name='forge_abi.RequestVerifyTx.assets', index=2,
            number=3, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='stakes', full_name='forge_abi.RequestVerifyTx.stakes', index=3,
            number=4, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='context', full_name='forge_abi.RequestVerifyTx.context', index=4,
            number=5, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='app_state', full_name='forge_abi.RequestVerifyTx.app_state', index=5,
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
    serialized_start=62,
    serialized_end=317,
)


_RESPONSEVERIFYTX = _descriptor.Descriptor(
    name='ResponseVerifyTx',
    full_name='forge_abi.ResponseVerifyTx',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='code', full_name='forge_abi.ResponseVerifyTx.code', index=0,
            number=1, type=14, cpp_type=8, label=1,
            has_default_value=False, default_value=0,
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
    serialized_start=319,
    serialized_end=374,
)


_REQUESTUPDATESTATE = _descriptor.Descriptor(
    name='RequestUpdateState',
    full_name='forge_abi.RequestUpdateState',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='tx', full_name='forge_abi.RequestUpdateState.tx', index=0,
            number=1, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='states', full_name='forge_abi.RequestUpdateState.states', index=1,
            number=2, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='assets', full_name='forge_abi.RequestUpdateState.assets', index=2,
            number=3, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='stakes', full_name='forge_abi.RequestUpdateState.stakes', index=3,
            number=4, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='context', full_name='forge_abi.RequestUpdateState.context', index=4,
            number=5, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='app_state', full_name='forge_abi.RequestUpdateState.app_state', index=5,
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
    serialized_start=377,
    serialized_end=635,
)


_RESPONSEUPDATESTATE = _descriptor.Descriptor(
    name='ResponseUpdateState',
    full_name='forge_abi.ResponseUpdateState',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='code', full_name='forge_abi.ResponseUpdateState.code', index=0,
            number=1, type=14, cpp_type=8, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='states', full_name='forge_abi.ResponseUpdateState.states', index=1,
            number=2, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='assets', full_name='forge_abi.ResponseUpdateState.assets', index=2,
            number=3, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='stakes', full_name='forge_abi.ResponseUpdateState.stakes', index=3,
            number=4, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='app_state', full_name='forge_abi.ResponseUpdateState.app_state', index=4,
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
    serialized_start=638,
    serialized_end=857,
)


_REQUESTINFO = _descriptor.Descriptor(
    name='RequestInfo',
    full_name='forge_abi.RequestInfo',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='forge_version', full_name='forge_abi.RequestInfo.forge_version', index=0,
            number=1, type=9, cpp_type=9, label=1,
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
    serialized_start=859,
    serialized_end=895,
)


_RESPONSEINFO = _descriptor.Descriptor(
    name='ResponseInfo',
    full_name='forge_abi.ResponseInfo',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='type_urls', full_name='forge_abi.ResponseInfo.type_urls', index=0,
            number=1, type=9, cpp_type=9, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='app_hash', full_name='forge_abi.ResponseInfo.app_hash', index=1,
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
    serialized_start=897,
    serialized_end=948,
)


_REQUEST = _descriptor.Descriptor(
    name='Request',
    full_name='forge_abi.Request',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='verify_tx', full_name='forge_abi.Request.verify_tx', index=0,
            number=1, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='update_state', full_name='forge_abi.Request.update_state', index=1,
            number=2, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='info', full_name='forge_abi.Request.info', index=2,
            number=3, type=11, cpp_type=10, label=1,
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
        _descriptor.OneofDescriptor(
            name='value', full_name='forge_abi.Request.value',
            index=0, containing_type=None, fields=[]),
    ],
    serialized_start=951,
    serialized_end=1113,
)


_RESPONSE = _descriptor.Descriptor(
    name='Response',
    full_name='forge_abi.Response',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='verify_tx', full_name='forge_abi.Response.verify_tx', index=0,
            number=1, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='update_state', full_name='forge_abi.Response.update_state', index=1,
            number=2, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR),
        _descriptor.FieldDescriptor(
            name='info', full_name='forge_abi.Response.info', index=2,
            number=3, type=11, cpp_type=10, label=1,
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
        _descriptor.OneofDescriptor(
            name='value', full_name='forge_abi.Response.value',
            index=0, containing_type=None, fields=[]),
    ],
    serialized_start=1116,
    serialized_end=1282,
)

_REQUESTVERIFYTX.fields_by_name['tx'].message_type = type__pb2._TRANSACTION
_REQUESTVERIFYTX.fields_by_name['states'].message_type = state__pb2._ACCOUNTSTATE
_REQUESTVERIFYTX.fields_by_name['assets'].message_type = state__pb2._ASSETSTATE
_REQUESTVERIFYTX.fields_by_name['stakes'].message_type = state__pb2._STAKESTATE
_REQUESTVERIFYTX.fields_by_name['context'].message_type = type__pb2._ABCICONTEXT
_REQUESTVERIFYTX.fields_by_name['app_state'].message_type = state__pb2._FORGESTATE
_RESPONSEVERIFYTX.fields_by_name['code'].enum_type = enum__pb2._STATUSCODE
_REQUESTUPDATESTATE.fields_by_name['tx'].message_type = type__pb2._TRANSACTION
_REQUESTUPDATESTATE.fields_by_name['states'].message_type = state__pb2._ACCOUNTSTATE
_REQUESTUPDATESTATE.fields_by_name['assets'].message_type = state__pb2._ASSETSTATE
_REQUESTUPDATESTATE.fields_by_name['stakes'].message_type = state__pb2._STAKESTATE
_REQUESTUPDATESTATE.fields_by_name['context'].message_type = type__pb2._ABCICONTEXT
_REQUESTUPDATESTATE.fields_by_name['app_state'].message_type = state__pb2._FORGESTATE
_RESPONSEUPDATESTATE.fields_by_name['code'].enum_type = enum__pb2._STATUSCODE
_RESPONSEUPDATESTATE.fields_by_name['states'].message_type = state__pb2._ACCOUNTSTATE
_RESPONSEUPDATESTATE.fields_by_name['assets'].message_type = state__pb2._ASSETSTATE
_RESPONSEUPDATESTATE.fields_by_name['stakes'].message_type = state__pb2._STAKESTATE
_RESPONSEUPDATESTATE.fields_by_name['app_state'].message_type = state__pb2._FORGESTATE
_REQUEST.fields_by_name['verify_tx'].message_type = _REQUESTVERIFYTX
_REQUEST.fields_by_name['update_state'].message_type = _REQUESTUPDATESTATE
_REQUEST.fields_by_name['info'].message_type = _REQUESTINFO
_REQUEST.oneofs_by_name['value'].fields.append(
    _REQUEST.fields_by_name['verify_tx'])
_REQUEST.fields_by_name['verify_tx'].containing_oneof = _REQUEST.oneofs_by_name['value']
_REQUEST.oneofs_by_name['value'].fields.append(
    _REQUEST.fields_by_name['update_state'])
_REQUEST.fields_by_name['update_state'].containing_oneof = _REQUEST.oneofs_by_name['value']
_REQUEST.oneofs_by_name['value'].fields.append(
    _REQUEST.fields_by_name['info'])
_REQUEST.fields_by_name['info'].containing_oneof = _REQUEST.oneofs_by_name['value']
_RESPONSE.fields_by_name['verify_tx'].message_type = _RESPONSEVERIFYTX
_RESPONSE.fields_by_name['update_state'].message_type = _RESPONSEUPDATESTATE
_RESPONSE.fields_by_name['info'].message_type = _RESPONSEINFO
_RESPONSE.oneofs_by_name['value'].fields.append(
    _RESPONSE.fields_by_name['verify_tx'])
_RESPONSE.fields_by_name['verify_tx'].containing_oneof = _RESPONSE.oneofs_by_name['value']
_RESPONSE.oneofs_by_name['value'].fields.append(
    _RESPONSE.fields_by_name['update_state'])
_RESPONSE.fields_by_name['update_state'].containing_oneof = _RESPONSE.oneofs_by_name['value']
_RESPONSE.oneofs_by_name['value'].fields.append(
    _RESPONSE.fields_by_name['info'])
_RESPONSE.fields_by_name['info'].containing_oneof = _RESPONSE.oneofs_by_name['value']
DESCRIPTOR.message_types_by_name['RequestVerifyTx'] = _REQUESTVERIFYTX
DESCRIPTOR.message_types_by_name['ResponseVerifyTx'] = _RESPONSEVERIFYTX
DESCRIPTOR.message_types_by_name['RequestUpdateState'] = _REQUESTUPDATESTATE
DESCRIPTOR.message_types_by_name['ResponseUpdateState'] = _RESPONSEUPDATESTATE
DESCRIPTOR.message_types_by_name['RequestInfo'] = _REQUESTINFO
DESCRIPTOR.message_types_by_name['ResponseInfo'] = _RESPONSEINFO
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RequestVerifyTx = _reflection.GeneratedProtocolMessageType('RequestVerifyTx', (_message.Message,), dict(
    DESCRIPTOR=_REQUESTVERIFYTX,
    __module__='abi_pb2'
    # @@protoc_insertion_point(class_scope:forge_abi.RequestVerifyTx)
))
_sym_db.RegisterMessage(RequestVerifyTx)

ResponseVerifyTx = _reflection.GeneratedProtocolMessageType('ResponseVerifyTx', (_message.Message,), dict(
    DESCRIPTOR=_RESPONSEVERIFYTX,
    __module__='abi_pb2'
    # @@protoc_insertion_point(class_scope:forge_abi.ResponseVerifyTx)
))
_sym_db.RegisterMessage(ResponseVerifyTx)

RequestUpdateState = _reflection.GeneratedProtocolMessageType('RequestUpdateState', (_message.Message,), dict(
    DESCRIPTOR=_REQUESTUPDATESTATE,
    __module__='abi_pb2'
    # @@protoc_insertion_point(class_scope:forge_abi.RequestUpdateState)
))
_sym_db.RegisterMessage(RequestUpdateState)

ResponseUpdateState = _reflection.GeneratedProtocolMessageType('ResponseUpdateState', (_message.Message,), dict(
    DESCRIPTOR=_RESPONSEUPDATESTATE,
    __module__='abi_pb2'
    # @@protoc_insertion_point(class_scope:forge_abi.ResponseUpdateState)
))
_sym_db.RegisterMessage(ResponseUpdateState)

RequestInfo = _reflection.GeneratedProtocolMessageType('RequestInfo', (_message.Message,), dict(
    DESCRIPTOR=_REQUESTINFO,
    __module__='abi_pb2'
    # @@protoc_insertion_point(class_scope:forge_abi.RequestInfo)
))
_sym_db.RegisterMessage(RequestInfo)

ResponseInfo = _reflection.GeneratedProtocolMessageType('ResponseInfo', (_message.Message,), dict(
    DESCRIPTOR=_RESPONSEINFO,
    __module__='abi_pb2'
    # @@protoc_insertion_point(class_scope:forge_abi.ResponseInfo)
))
_sym_db.RegisterMessage(ResponseInfo)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
    DESCRIPTOR=_REQUEST,
    __module__='abi_pb2'
    # @@protoc_insertion_point(class_scope:forge_abi.Request)
))
_sym_db.RegisterMessage(Request)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
    DESCRIPTOR=_RESPONSE,
    __module__='abi_pb2'
    # @@protoc_insertion_point(class_scope:forge_abi.Response)
))
_sym_db.RegisterMessage(Response)


_FORGEAPPRPC = _descriptor.ServiceDescriptor(
    name='ForgeAppRpc',
    full_name='forge_abi.ForgeAppRpc',
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    serialized_start=1284,
    serialized_end=1409,
    methods=[
        _descriptor.MethodDescriptor(
            name='process_one',
            full_name='forge_abi.ForgeAppRpc.process_one',
            index=0,
            containing_service=None,
            input_type=_REQUEST,
            output_type=_RESPONSE,
            serialized_options=None,
        ),
        _descriptor.MethodDescriptor(
            name='process',
            full_name='forge_abi.ForgeAppRpc.process',
            index=1,
            containing_service=None,
            input_type=_REQUEST,
            output_type=_RESPONSE,
            serialized_options=None,
        ),
    ])
_sym_db.RegisterServiceDescriptor(_FORGEAPPRPC)

DESCRIPTOR.services_by_name['ForgeAppRpc'] = _FORGEAPPRPC

# @@protoc_insertion_point(module_scope)