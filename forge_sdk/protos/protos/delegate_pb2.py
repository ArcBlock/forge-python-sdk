# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: delegate.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='delegate.proto',
  package='forge_abi',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0e\x64\x65legate.proto\x12\tforge_abi\x1a\x19google/protobuf/any.proto\"q\n\nDelegateTx\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\n\n\x02to\x18\x02 \x01(\t\x12\"\n\x03ops\x18\x03 \x03(\x0b\x32\x15.forge_abi.DelegateOp\x12\"\n\x04\x64\x61ta\x18\x0f \x01(\x0b\x32\x14.google.protobuf.Any\"-\n\nDelegateOp\x12\x10\n\x08type_url\x18\x01 \x01(\t\x12\r\n\x05rules\x18\x02 \x03(\tb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,])




_DELEGATETX = _descriptor.Descriptor(
  name='DelegateTx',
  full_name='forge_abi.DelegateTx',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='forge_abi.DelegateTx.address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='to', full_name='forge_abi.DelegateTx.to', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ops', full_name='forge_abi.DelegateTx.ops', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='forge_abi.DelegateTx.data', index=3,
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
  serialized_start=56,
  serialized_end=169,
)


_DELEGATEOP = _descriptor.Descriptor(
  name='DelegateOp',
  full_name='forge_abi.DelegateOp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type_url', full_name='forge_abi.DelegateOp.type_url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rules', full_name='forge_abi.DelegateOp.rules', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=171,
  serialized_end=216,
)

_DELEGATETX.fields_by_name['ops'].message_type = _DELEGATEOP
_DELEGATETX.fields_by_name['data'].message_type = google_dot_protobuf_dot_any__pb2._ANY
DESCRIPTOR.message_types_by_name['DelegateTx'] = _DELEGATETX
DESCRIPTOR.message_types_by_name['DelegateOp'] = _DELEGATEOP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DelegateTx = _reflection.GeneratedProtocolMessageType('DelegateTx', (_message.Message,), dict(
  DESCRIPTOR = _DELEGATETX,
  __module__ = 'delegate_pb2'
  # @@protoc_insertion_point(class_scope:forge_abi.DelegateTx)
  ))
_sym_db.RegisterMessage(DelegateTx)

DelegateOp = _reflection.GeneratedProtocolMessageType('DelegateOp', (_message.Message,), dict(
  DESCRIPTOR = _DELEGATEOP,
  __module__ = 'delegate_pb2'
  # @@protoc_insertion_point(class_scope:forge_abi.DelegateOp)
  ))
_sym_db.RegisterMessage(DelegateOp)


# @@protoc_insertion_point(module_scope)
