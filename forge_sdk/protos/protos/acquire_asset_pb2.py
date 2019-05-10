# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: acquire_asset.proto

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
  name='acquire_asset.proto',
  package='forge_abi',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x13\x61\x63quire_asset.proto\x12\tforge_abi\x1a\x19google/protobuf/any.proto\"*\n\tAssetSpec\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\t\"e\n\x0e\x41\x63quireAssetTx\x12\n\n\x02to\x18\x01 \x01(\t\x12#\n\x05specs\x18\x02 \x03(\x0b\x32\x14.forge_abi.AssetSpec\x12\"\n\x04\x64\x61ta\x18\x0f \x01(\x0b\x32\x14.google.protobuf.Anyb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,])




_ASSETSPEC = _descriptor.Descriptor(
  name='AssetSpec',
  full_name='forge_abi.AssetSpec',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='forge_abi.AssetSpec.address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='forge_abi.AssetSpec.data', index=1,
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
  serialized_start=61,
  serialized_end=103,
)


_ACQUIREASSETTX = _descriptor.Descriptor(
  name='AcquireAssetTx',
  full_name='forge_abi.AcquireAssetTx',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='to', full_name='forge_abi.AcquireAssetTx.to', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='specs', full_name='forge_abi.AcquireAssetTx.specs', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='forge_abi.AcquireAssetTx.data', index=2,
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
  serialized_start=105,
  serialized_end=206,
)

_ACQUIREASSETTX.fields_by_name['specs'].message_type = _ASSETSPEC
_ACQUIREASSETTX.fields_by_name['data'].message_type = google_dot_protobuf_dot_any__pb2._ANY
DESCRIPTOR.message_types_by_name['AssetSpec'] = _ASSETSPEC
DESCRIPTOR.message_types_by_name['AcquireAssetTx'] = _ACQUIREASSETTX
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AssetSpec = _reflection.GeneratedProtocolMessageType('AssetSpec', (_message.Message,), dict(
  DESCRIPTOR = _ASSETSPEC,
  __module__ = 'acquire_asset_pb2'
  # @@protoc_insertion_point(class_scope:forge_abi.AssetSpec)
  ))
_sym_db.RegisterMessage(AssetSpec)

AcquireAssetTx = _reflection.GeneratedProtocolMessageType('AcquireAssetTx', (_message.Message,), dict(
  DESCRIPTOR = _ACQUIREASSETTX,
  __module__ = 'acquire_asset_pb2'
  # @@protoc_insertion_point(class_scope:forge_abi.AcquireAssetTx)
  ))
_sym_db.RegisterMessage(AcquireAssetTx)


# @@protoc_insertion_point(module_scope)
