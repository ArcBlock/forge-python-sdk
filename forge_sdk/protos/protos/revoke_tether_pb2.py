# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: revoke_tether.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from . import type_pb2 as type__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='revoke_tether.proto',
  package='forge_abi',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x13revoke_tether.proto\x12\tforge_abi\x1a\x19google/protobuf/any.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\ntype.proto\"D\n\x0eRevokeTetherTx\x12\x0e\n\x06tether\x18\x01 \x01(\t\x12\"\n\x04\x64\x61ta\x18\x0f \x01(\x0b\x32\x14.google.protobuf.Anyb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,type__pb2.DESCRIPTOR,])




_REVOKETETHERTX = _descriptor.Descriptor(
  name='RevokeTetherTx',
  full_name='forge_abi.RevokeTetherTx',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tether', full_name='forge_abi.RevokeTetherTx.tether', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='forge_abi.RevokeTetherTx.data', index=1,
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
  serialized_start=106,
  serialized_end=174,
)

_REVOKETETHERTX.fields_by_name['data'].message_type = google_dot_protobuf_dot_any__pb2._ANY
DESCRIPTOR.message_types_by_name['RevokeTetherTx'] = _REVOKETETHERTX
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RevokeTetherTx = _reflection.GeneratedProtocolMessageType('RevokeTetherTx', (_message.Message,), dict(
  DESCRIPTOR = _REVOKETETHERTX,
  __module__ = 'revoke_tether_pb2'
  # @@protoc_insertion_point(class_scope:forge_abi.RevokeTetherTx)
  ))
_sym_db.RegisterMessage(RevokeTetherTx)


# @@protoc_insertion_point(module_scope)
