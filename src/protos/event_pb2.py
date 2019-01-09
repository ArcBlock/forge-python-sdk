# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: event.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import vendor_pb2 as vendor__pb2
from . import code_pb2 as code__pb2
from . import type_pb2 as type__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='event.proto',
  package='forge_abi',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0b\x65vent.proto\x12\tforge_abi\x1a\x0cvendor.proto\x1a\ncode.proto\x1a\ntype.proto\"F\n\x10RequestSubscribe\x12\"\n\x04type\x18\x01 \x01(\x0e\x32\x14.forge_abi.TopicType\x12\x0e\n\x06\x66ilter\x18\x02 \x01(\t\"\x84\x07\n\x11ResponseSubscribe\x12#\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x15.forge_abi.StatusCode\x12\x0f\n\x05topic\x18\x02 \x01(\tH\x00\x12*\n\x08transfer\x18\x03 \x01(\x0b\x32\x16.forge_abi.TransactionH\x00\x12\x31\n\x0f\x61\x63\x63ount_migrate\x18\x04 \x01(\x0b\x32\x16.forge_abi.TransactionH\x00\x12)\n\x07\x63onfirm\x18\x05 \x01(\x0b\x32\x16.forge_abi.TransactionH\x00\x12.\n\x0c\x63reate_asset\x18\x06 \x01(\x0b\x32\x16.forge_abi.TransactionH\x00\x12*\n\x08\x65xchange\x18\x07 \x01(\x0b\x32\x16.forge_abi.TransactionH\x00\x12(\n\x06revoke\x18\x08 \x01(\x0b\x32\x16.forge_abi.TransactionH\x00\x12\x36\n\x0b\x62\x65gin_block\x18\x10 \x01(\x0b\x32\x1f.forge_vendor.RequestBeginBlockH\x00\x12\x32\n\tend_block\x18\x11 \x01(\x0b\x32\x1d.forge_vendor.RequestEndBlockH\x00\x12)\n\x07\x64\x65\x63lare\x18\x13 \x01(\x0b\x32\x16.forge_abi.TransactionH\x00\x12\x31\n\x0f\x61\x63\x63ount_upgrade\x18\x14 \x01(\x0b\x32\x16.forge_abi.TransactionH\x00\x12\x33\n\x11\x63onsensus_upgrade\x18\x15 \x01(\x0b\x32\x16.forge_abi.TransactionH\x00\x12.\n\x0c\x64\x65\x63lare_file\x18\x16 \x01(\x0b\x32\x16.forge_abi.TransactionH\x00\x12-\n\x0bsys_upgrade\x18\x17 \x01(\x0b\x32\x16.forge_abi.TransactionH\x00\x12\x30\n\raccount_state\x18\x81\x01 \x01(\x0b\x32\x16.forge_abi.TransactionH\x00\x12.\n\x0b\x61sset_state\x18\x82\x01 \x01(\x0b\x32\x16.forge_abi.TransactionH\x00\x12\x30\n\rchannel_state\x18\x83\x01 \x01(\x0b\x32\x16.forge_abi.TransactionH\x00\x12.\n\x0b\x66orge_state\x18\x84\x01 \x01(\x0b\x32\x16.forge_abi.TransactionH\x00\x42\x07\n\x05value*\xaf\x02\n\tTopicType\x12\x0c\n\x08transfer\x10\x00\x12\x13\n\x0f\x61\x63\x63ount_migrate\x10\x01\x12\x0b\n\x07\x63onfirm\x10\x02\x12\x10\n\x0c\x63reate_asset\x10\x03\x12\x0c\n\x08\x65xchange\x10\x04\x12\n\n\x06revoke\x10\x05\x12\x0f\n\x0b\x62\x65gin_block\x10\x10\x12\r\n\tend_block\x10\x11\x12\x0b\n\x07\x64\x65\x63lare\x10\x13\x12\x13\n\x0f\x61\x63\x63ount_upgrade\x10\x14\x12\x15\n\x11\x63onsensus_upgrade\x10\x15\x12\x10\n\x0c\x64\x65\x63lare_file\x10\x16\x12\x0f\n\x0bsys_upgrade\x10\x17\x12\x12\n\raccount_state\x10\x81\x01\x12\x10\n\x0b\x61sset_state\x10\x82\x01\x12\x12\n\rchannel_state\x10\x83\x01\x12\x10\n\x0b\x66orge_state\x10\x84\x01\x32T\n\x08\x45ventRpc\x12H\n\tsubscribe\x12\x1b.forge_abi.RequestSubscribe\x1a\x1c.forge_abi.ResponseSubscribe0\x01\x62\x06proto3')
  ,
  dependencies=[vendor__pb2.DESCRIPTOR,code__pb2.DESCRIPTOR,type__pb2.DESCRIPTOR,])

_TOPICTYPE = _descriptor.EnumDescriptor(
  name='TopicType',
  full_name='forge_abi.TopicType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='transfer', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='account_migrate', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='confirm', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='create_asset', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='exchange', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='revoke', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='begin_block', index=6, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='end_block', index=7, number=17,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='declare', index=8, number=19,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='account_upgrade', index=9, number=20,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='consensus_upgrade', index=10, number=21,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='declare_file', index=11, number=22,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='sys_upgrade', index=12, number=23,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='account_state', index=13, number=129,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='asset_state', index=14, number=130,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='channel_state', index=15, number=131,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='forge_state', index=16, number=132,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1040,
  serialized_end=1343,
)
_sym_db.RegisterEnumDescriptor(_TOPICTYPE)

TopicType = enum_type_wrapper.EnumTypeWrapper(_TOPICTYPE)
transfer = 0
account_migrate = 1
confirm = 2
create_asset = 3
exchange = 4
revoke = 5
begin_block = 16
end_block = 17
declare = 19
account_upgrade = 20
consensus_upgrade = 21
declare_file = 22
sys_upgrade = 23
account_state = 129
asset_state = 130
channel_state = 131
forge_state = 132



_REQUESTSUBSCRIBE = _descriptor.Descriptor(
  name='RequestSubscribe',
  full_name='forge_abi.RequestSubscribe',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='forge_abi.RequestSubscribe.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='filter', full_name='forge_abi.RequestSubscribe.filter', index=1,
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
  serialized_start=64,
  serialized_end=134,
)


_RESPONSESUBSCRIBE = _descriptor.Descriptor(
  name='ResponseSubscribe',
  full_name='forge_abi.ResponseSubscribe',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='forge_abi.ResponseSubscribe.code', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='topic', full_name='forge_abi.ResponseSubscribe.topic', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transfer', full_name='forge_abi.ResponseSubscribe.transfer', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='account_migrate', full_name='forge_abi.ResponseSubscribe.account_migrate', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='confirm', full_name='forge_abi.ResponseSubscribe.confirm', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='create_asset', full_name='forge_abi.ResponseSubscribe.create_asset', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='exchange', full_name='forge_abi.ResponseSubscribe.exchange', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='revoke', full_name='forge_abi.ResponseSubscribe.revoke', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='begin_block', full_name='forge_abi.ResponseSubscribe.begin_block', index=8,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_block', full_name='forge_abi.ResponseSubscribe.end_block', index=9,
      number=17, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='declare', full_name='forge_abi.ResponseSubscribe.declare', index=10,
      number=19, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='account_upgrade', full_name='forge_abi.ResponseSubscribe.account_upgrade', index=11,
      number=20, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='consensus_upgrade', full_name='forge_abi.ResponseSubscribe.consensus_upgrade', index=12,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='declare_file', full_name='forge_abi.ResponseSubscribe.declare_file', index=13,
      number=22, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sys_upgrade', full_name='forge_abi.ResponseSubscribe.sys_upgrade', index=14,
      number=23, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='account_state', full_name='forge_abi.ResponseSubscribe.account_state', index=15,
      number=129, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='asset_state', full_name='forge_abi.ResponseSubscribe.asset_state', index=16,
      number=130, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='channel_state', full_name='forge_abi.ResponseSubscribe.channel_state', index=17,
      number=131, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='forge_state', full_name='forge_abi.ResponseSubscribe.forge_state', index=18,
      number=132, type=11, cpp_type=10, label=1,
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
      name='value', full_name='forge_abi.ResponseSubscribe.value',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=137,
  serialized_end=1037,
)

_REQUESTSUBSCRIBE.fields_by_name['type'].enum_type = _TOPICTYPE
_RESPONSESUBSCRIBE.fields_by_name['code'].enum_type = code__pb2._STATUSCODE
_RESPONSESUBSCRIBE.fields_by_name['transfer'].message_type = type__pb2._TRANSACTION
_RESPONSESUBSCRIBE.fields_by_name['account_migrate'].message_type = type__pb2._TRANSACTION
_RESPONSESUBSCRIBE.fields_by_name['confirm'].message_type = type__pb2._TRANSACTION
_RESPONSESUBSCRIBE.fields_by_name['create_asset'].message_type = type__pb2._TRANSACTION
_RESPONSESUBSCRIBE.fields_by_name['exchange'].message_type = type__pb2._TRANSACTION
_RESPONSESUBSCRIBE.fields_by_name['revoke'].message_type = type__pb2._TRANSACTION
_RESPONSESUBSCRIBE.fields_by_name['begin_block'].message_type = vendor__pb2._REQUESTBEGINBLOCK
_RESPONSESUBSCRIBE.fields_by_name['end_block'].message_type = vendor__pb2._REQUESTENDBLOCK
_RESPONSESUBSCRIBE.fields_by_name['declare'].message_type = type__pb2._TRANSACTION
_RESPONSESUBSCRIBE.fields_by_name['account_upgrade'].message_type = type__pb2._TRANSACTION
_RESPONSESUBSCRIBE.fields_by_name['consensus_upgrade'].message_type = type__pb2._TRANSACTION
_RESPONSESUBSCRIBE.fields_by_name['declare_file'].message_type = type__pb2._TRANSACTION
_RESPONSESUBSCRIBE.fields_by_name['sys_upgrade'].message_type = type__pb2._TRANSACTION
_RESPONSESUBSCRIBE.fields_by_name['account_state'].message_type = type__pb2._TRANSACTION
_RESPONSESUBSCRIBE.fields_by_name['asset_state'].message_type = type__pb2._TRANSACTION
_RESPONSESUBSCRIBE.fields_by_name['channel_state'].message_type = type__pb2._TRANSACTION
_RESPONSESUBSCRIBE.fields_by_name['forge_state'].message_type = type__pb2._TRANSACTION
_RESPONSESUBSCRIBE.oneofs_by_name['value'].fields.append(
  _RESPONSESUBSCRIBE.fields_by_name['topic'])
_RESPONSESUBSCRIBE.fields_by_name['topic'].containing_oneof = _RESPONSESUBSCRIBE.oneofs_by_name['value']
_RESPONSESUBSCRIBE.oneofs_by_name['value'].fields.append(
  _RESPONSESUBSCRIBE.fields_by_name['transfer'])
_RESPONSESUBSCRIBE.fields_by_name['transfer'].containing_oneof = _RESPONSESUBSCRIBE.oneofs_by_name['value']
_RESPONSESUBSCRIBE.oneofs_by_name['value'].fields.append(
  _RESPONSESUBSCRIBE.fields_by_name['account_migrate'])
_RESPONSESUBSCRIBE.fields_by_name['account_migrate'].containing_oneof = _RESPONSESUBSCRIBE.oneofs_by_name['value']
_RESPONSESUBSCRIBE.oneofs_by_name['value'].fields.append(
  _RESPONSESUBSCRIBE.fields_by_name['confirm'])
_RESPONSESUBSCRIBE.fields_by_name['confirm'].containing_oneof = _RESPONSESUBSCRIBE.oneofs_by_name['value']
_RESPONSESUBSCRIBE.oneofs_by_name['value'].fields.append(
  _RESPONSESUBSCRIBE.fields_by_name['create_asset'])
_RESPONSESUBSCRIBE.fields_by_name['create_asset'].containing_oneof = _RESPONSESUBSCRIBE.oneofs_by_name['value']
_RESPONSESUBSCRIBE.oneofs_by_name['value'].fields.append(
  _RESPONSESUBSCRIBE.fields_by_name['exchange'])
_RESPONSESUBSCRIBE.fields_by_name['exchange'].containing_oneof = _RESPONSESUBSCRIBE.oneofs_by_name['value']
_RESPONSESUBSCRIBE.oneofs_by_name['value'].fields.append(
  _RESPONSESUBSCRIBE.fields_by_name['revoke'])
_RESPONSESUBSCRIBE.fields_by_name['revoke'].containing_oneof = _RESPONSESUBSCRIBE.oneofs_by_name['value']
_RESPONSESUBSCRIBE.oneofs_by_name['value'].fields.append(
  _RESPONSESUBSCRIBE.fields_by_name['begin_block'])
_RESPONSESUBSCRIBE.fields_by_name['begin_block'].containing_oneof = _RESPONSESUBSCRIBE.oneofs_by_name['value']
_RESPONSESUBSCRIBE.oneofs_by_name['value'].fields.append(
  _RESPONSESUBSCRIBE.fields_by_name['end_block'])
_RESPONSESUBSCRIBE.fields_by_name['end_block'].containing_oneof = _RESPONSESUBSCRIBE.oneofs_by_name['value']
_RESPONSESUBSCRIBE.oneofs_by_name['value'].fields.append(
  _RESPONSESUBSCRIBE.fields_by_name['declare'])
_RESPONSESUBSCRIBE.fields_by_name['declare'].containing_oneof = _RESPONSESUBSCRIBE.oneofs_by_name['value']
_RESPONSESUBSCRIBE.oneofs_by_name['value'].fields.append(
  _RESPONSESUBSCRIBE.fields_by_name['account_upgrade'])
_RESPONSESUBSCRIBE.fields_by_name['account_upgrade'].containing_oneof = _RESPONSESUBSCRIBE.oneofs_by_name['value']
_RESPONSESUBSCRIBE.oneofs_by_name['value'].fields.append(
  _RESPONSESUBSCRIBE.fields_by_name['consensus_upgrade'])
_RESPONSESUBSCRIBE.fields_by_name['consensus_upgrade'].containing_oneof = _RESPONSESUBSCRIBE.oneofs_by_name['value']
_RESPONSESUBSCRIBE.oneofs_by_name['value'].fields.append(
  _RESPONSESUBSCRIBE.fields_by_name['declare_file'])
_RESPONSESUBSCRIBE.fields_by_name['declare_file'].containing_oneof = _RESPONSESUBSCRIBE.oneofs_by_name['value']
_RESPONSESUBSCRIBE.oneofs_by_name['value'].fields.append(
  _RESPONSESUBSCRIBE.fields_by_name['sys_upgrade'])
_RESPONSESUBSCRIBE.fields_by_name['sys_upgrade'].containing_oneof = _RESPONSESUBSCRIBE.oneofs_by_name['value']
_RESPONSESUBSCRIBE.oneofs_by_name['value'].fields.append(
  _RESPONSESUBSCRIBE.fields_by_name['account_state'])
_RESPONSESUBSCRIBE.fields_by_name['account_state'].containing_oneof = _RESPONSESUBSCRIBE.oneofs_by_name['value']
_RESPONSESUBSCRIBE.oneofs_by_name['value'].fields.append(
  _RESPONSESUBSCRIBE.fields_by_name['asset_state'])
_RESPONSESUBSCRIBE.fields_by_name['asset_state'].containing_oneof = _RESPONSESUBSCRIBE.oneofs_by_name['value']
_RESPONSESUBSCRIBE.oneofs_by_name['value'].fields.append(
  _RESPONSESUBSCRIBE.fields_by_name['channel_state'])
_RESPONSESUBSCRIBE.fields_by_name['channel_state'].containing_oneof = _RESPONSESUBSCRIBE.oneofs_by_name['value']
_RESPONSESUBSCRIBE.oneofs_by_name['value'].fields.append(
  _RESPONSESUBSCRIBE.fields_by_name['forge_state'])
_RESPONSESUBSCRIBE.fields_by_name['forge_state'].containing_oneof = _RESPONSESUBSCRIBE.oneofs_by_name['value']
DESCRIPTOR.message_types_by_name['RequestSubscribe'] = _REQUESTSUBSCRIBE
DESCRIPTOR.message_types_by_name['ResponseSubscribe'] = _RESPONSESUBSCRIBE
DESCRIPTOR.enum_types_by_name['TopicType'] = _TOPICTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RequestSubscribe = _reflection.GeneratedProtocolMessageType('RequestSubscribe', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTSUBSCRIBE,
  __module__ = 'event_pb2'
  # @@protoc_insertion_point(class_scope:forge_abi.RequestSubscribe)
  ))
_sym_db.RegisterMessage(RequestSubscribe)

ResponseSubscribe = _reflection.GeneratedProtocolMessageType('ResponseSubscribe', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSESUBSCRIBE,
  __module__ = 'event_pb2'
  # @@protoc_insertion_point(class_scope:forge_abi.ResponseSubscribe)
  ))
_sym_db.RegisterMessage(ResponseSubscribe)



_EVENTRPC = _descriptor.ServiceDescriptor(
  name='EventRpc',
  full_name='forge_abi.EventRpc',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1345,
  serialized_end=1429,
  methods=[
  _descriptor.MethodDescriptor(
    name='subscribe',
    full_name='forge_abi.EventRpc.subscribe',
    index=0,
    containing_service=None,
    input_type=_REQUESTSUBSCRIBE,
    output_type=_RESPONSESUBSCRIBE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_EVENTRPC)

DESCRIPTOR.services_by_name['EventRpc'] = _EVENTRPC

# @@protoc_insertion_point(module_scope)
