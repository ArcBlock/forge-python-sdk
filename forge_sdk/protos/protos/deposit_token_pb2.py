# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: deposit_token.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import type_pb2 as type__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='deposit_token.proto',
  package='forge_abi',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x13\x64\x65posit_token.proto\x12\tforge_abi\x1a\ntype.proto\"k\n\x0e\x44\x65positTokenTx\x12!\n\x05value\x18\x01 \x01(\x0b\x32\x12.forge_abi.BigUint\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\x12%\n\x08\x65vidence\x18\x03 \x01(\x0b\x32\x13.forge_abi.Evidenceb\x06proto3')
  ,
  dependencies=[type__pb2.DESCRIPTOR,])




_DEPOSITTOKENTX = _descriptor.Descriptor(
  name='DepositTokenTx',
  full_name='forge_abi.DepositTokenTx',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='forge_abi.DepositTokenTx.value', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='address', full_name='forge_abi.DepositTokenTx.address', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='evidence', full_name='forge_abi.DepositTokenTx.evidence', index=2,
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
  ],
  serialized_start=46,
  serialized_end=153,
)

_DEPOSITTOKENTX.fields_by_name['value'].message_type = type__pb2._BIGUINT
_DEPOSITTOKENTX.fields_by_name['evidence'].message_type = type__pb2._EVIDENCE
DESCRIPTOR.message_types_by_name['DepositTokenTx'] = _DEPOSITTOKENTX
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DepositTokenTx = _reflection.GeneratedProtocolMessageType('DepositTokenTx', (_message.Message,), dict(
  DESCRIPTOR = _DEPOSITTOKENTX,
  __module__ = 'deposit_token_pb2'
  # @@protoc_insertion_point(class_scope:forge_abi.DepositTokenTx)
  ))
_sym_db.RegisterMessage(DepositTokenTx)


# @@protoc_insertion_point(module_scope)