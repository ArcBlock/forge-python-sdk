# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: transfer.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from . import type_pb2 as type__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='transfer.proto',
  package='forge_abi',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0etransfer.proto\x12\tforge_abi\x1a\x19google/protobuf/any.proto\x1a\ntype.proto\"o\n\nTransferTx\x12\n\n\x02to\x18\x01 \x01(\t\x12!\n\x05value\x18\x02 \x01(\x0b\x32\x12.forge_abi.BigUint\x12\x0e\n\x06\x61ssets\x18\x03 \x03(\t\x12\"\n\x04\x64\x61ta\x18\x0f \x01(\x0b\x32\x14.google.protobuf.Anyb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,type__pb2.DESCRIPTOR,])




_TRANSFERTX = _descriptor.Descriptor(
  name='TransferTx',
  full_name='forge_abi.TransferTx',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='to', full_name='forge_abi.TransferTx.to', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='forge_abi.TransferTx.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='assets', full_name='forge_abi.TransferTx.assets', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='forge_abi.TransferTx.data', index=3,
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
  serialized_start=68,
  serialized_end=179,
)

_TRANSFERTX.fields_by_name['value'].message_type = type__pb2._BIGUINT
_TRANSFERTX.fields_by_name['data'].message_type = google_dot_protobuf_dot_any__pb2._ANY
DESCRIPTOR.message_types_by_name['TransferTx'] = _TRANSFERTX
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TransferTx = _reflection.GeneratedProtocolMessageType('TransferTx', (_message.Message,), dict(
  DESCRIPTOR = _TRANSFERTX,
  __module__ = 'transfer_pb2'
  # @@protoc_insertion_point(class_scope:forge_abi.TransferTx)
  ))
_sym_db.RegisterMessage(TransferTx)


# @@protoc_insertion_point(module_scope)
