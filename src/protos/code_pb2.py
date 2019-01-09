# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: code.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='code.proto',
  package='forge_abi',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\ncode.proto\x12\tforge_abi*\x89\x04\n\nStatusCode\x12\x06\n\x02ok\x10\x00\x12\x11\n\rinvalid_nonce\x10\x01\x12\x15\n\x11invalid_signature\x10\x02\x12\x18\n\x14invalid_sender_state\x10\x03\x12\x1a\n\x16invalid_receiver_state\x10\x04\x12\x15\n\x11insufficient_data\x10\x05\x12\x15\n\x11insufficient_fund\x10\x06\x12\x11\n\rinvalid_owner\x10\x07\x12\x0e\n\ninvalid_tx\x10\x08\x12\x12\n\x0eunsupported_tx\x10\t\x12\x13\n\x0finvalid_moniker\x10\x10\x12\x16\n\x12invalid_passphrase\x10\x11\x12\x13\n\x0finvalid_channel\x10\x12\x12 \n\x1cinvalid_channel_waiting_data\x10\x13\x12\x14\n\x10invalid_multisig\x10\x14\x12\x12\n\x0einvalid_wallet\x10\x15\x12\x14\n\x10invalid_chain_id\x10\x16\x12\x15\n\x11need_confirmation\x10\x17\x12\x17\n\x13\x63onsensus_rpc_error\x10\x18\x12\x15\n\x11storage_rpc_error\x10\x19\x12\t\n\x05noent\x10\x1a\x12\x14\n\x10\x61\x63\x63ount_migrated\x10\x1b\x12\x13\n\x0f\x63hannel_is_full\x10\x1c\x12\r\n\x08internal\x10\xf4\x03\x62\x06proto3')
)

_STATUSCODE = _descriptor.EnumDescriptor(
  name='StatusCode',
  full_name='forge_abi.StatusCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ok', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='invalid_nonce', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='invalid_signature', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='invalid_sender_state', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='invalid_receiver_state', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='insufficient_data', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='insufficient_fund', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='invalid_owner', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='invalid_tx', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='unsupported_tx', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='invalid_moniker', index=10, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='invalid_passphrase', index=11, number=17,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='invalid_channel', index=12, number=18,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='invalid_channel_waiting_data', index=13, number=19,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='invalid_multisig', index=14, number=20,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='invalid_wallet', index=15, number=21,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='invalid_chain_id', index=16, number=22,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='need_confirmation', index=17, number=23,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='consensus_rpc_error', index=18, number=24,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='storage_rpc_error', index=19, number=25,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='noent', index=20, number=26,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='account_migrated', index=21, number=27,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='channel_is_full', index=22, number=28,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='internal', index=23, number=500,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=26,
  serialized_end=547,
)
_sym_db.RegisterEnumDescriptor(_STATUSCODE)

StatusCode = enum_type_wrapper.EnumTypeWrapper(_STATUSCODE)
ok = 0
invalid_nonce = 1
invalid_signature = 2
invalid_sender_state = 3
invalid_receiver_state = 4
insufficient_data = 5
insufficient_fund = 6
invalid_owner = 7
invalid_tx = 8
unsupported_tx = 9
invalid_moniker = 16
invalid_passphrase = 17
invalid_channel = 18
invalid_channel_waiting_data = 19
invalid_multisig = 20
invalid_wallet = 21
invalid_chain_id = 22
need_confirmation = 23
consensus_rpc_error = 24
storage_rpc_error = 25
noent = 26
account_migrated = 27
channel_is_full = 28
internal = 500


DESCRIPTOR.enum_types_by_name['StatusCode'] = _STATUSCODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
