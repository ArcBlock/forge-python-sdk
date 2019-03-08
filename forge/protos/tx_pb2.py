# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tx.proto

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
  name='tx.proto',
  package='forge_abi',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x08tx.proto\x12\tforge_abi\x1a\x19google/protobuf/any.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\ntype.proto\"C\n\x10\x41\x63\x63ountMigrateTx\x12\n\n\x02pk\x18\x01 \x01(\x0c\x12#\n\x04type\x18\x02 \x01(\x0b\x32\x15.forge_abi.WalletType\"\xb6\x01\n\x12\x43onsensusUpgradeTx\x12(\n\nvalidators\x18\x01 \x03(\x0b\x32\x14.forge_abi.Validator\x12\x11\n\tmax_bytes\x18\x02 \x01(\x04\x12\x0f\n\x07max_gas\x18\x03 \x01(\x12\x12\x16\n\x0emax_validators\x18\x04 \x01(\r\x12\x16\n\x0emax_candidates\x18\x05 \x01(\r\x12\"\n\x04\x64\x61ta\x18\x0f \x01(\x0b\x32\x14.google.protobuf.Any\"U\n\x0e\x43onsumeAssetTx\x12\x0e\n\x06issuer\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\x12\"\n\x04\x64\x61ta\x18\x0f \x01(\x0b\x32\x14.google.protobuf.Any\"\x8a\x01\n\rCreateAssetTx\x12\x0f\n\x07moniker\x18\x01 \x01(\t\x12\"\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x10\n\x08readonly\x18\x03 \x01(\x08\x12\x15\n\rtransferrable\x18\x04 \x01(\x08\x12\x0b\n\x03ttl\x18\x05 \x01(\r\x12\x0e\n\x06parent\x18\x06 \x01(\t\"\x81\x01\n\tDeclareTx\x12\x0f\n\x07moniker\x18\x01 \x01(\t\x12\n\n\x02pk\x18\x02 \x01(\x0c\x12#\n\x04type\x18\x03 \x01(\x0b\x32\x15.forge_abi.WalletType\x12\x0e\n\x06issuer\x18\x04 \x01(\t\x12\"\n\x04\x64\x61ta\x18\x0f \x01(\x0b\x32\x14.google.protobuf.Any\"\x1d\n\rDeclareFileTx\x12\x0c\n\x04hash\x18\x01 \x01(\t\"A\n\x0c\x45xchangeInfo\x12!\n\x05value\x18\x01 \x01(\x0b\x32\x12.forge_abi.BigUint\x12\x0e\n\x06\x61ssets\x18\x02 \x03(\t\"\xc0\x01\n\nExchangeTx\x12\n\n\x02to\x18\x01 \x01(\t\x12\'\n\x06sender\x18\x02 \x01(\x0b\x32\x17.forge_abi.ExchangeInfo\x12)\n\x08receiver\x18\x03 \x01(\x0b\x32\x17.forge_abi.ExchangeInfo\x12.\n\nexpired_at\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\"\n\x04\x64\x61ta\x18\x0f \x01(\x0b\x32\x14.google.protobuf.Any\"\x0f\n\rstakeForAsset\"\x0f\n\rstakeForChain\"\x0e\n\x0cStakeForNode\"\x0e\n\x0cstakeForUser\"m\n\x07StakeTx\x12\n\n\x02to\x18\x01 \x01(\t\x12!\n\x05value\x18\x02 \x01(\x0b\x32\x12.forge_abi.BigSint\x12\x0f\n\x07message\x18\x03 \x01(\t\x12\"\n\x04\x64\x61ta\x18\x0f \x01(\x0b\x32\x14.google.protobuf.Any\"n\n\x0cSysUpgradeTx\x12$\n\x04task\x18\x01 \x01(\x0b\x32\x16.forge_abi.UpgradeTask\x12\x14\n\x0cgrace_period\x18\x02 \x01(\x04\x12\"\n\x04\x64\x61ta\x18\x0f \x01(\x0b\x32\x14.google.protobuf.Any\"o\n\nTransferTx\x12\n\n\x02to\x18\x01 \x01(\t\x12!\n\x05value\x18\x02 \x01(\x0b\x32\x12.forge_abi.BigUint\x12\x0e\n\x06\x61ssets\x18\x03 \x03(\t\x12\"\n\x04\x64\x61ta\x18\x0f \x01(\x0b\x32\x14.google.protobuf.Any\"U\n\rUpdateAssetTx\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\x12\x0f\n\x07moniker\x18\x02 \x01(\t\x12\"\n\x04\x64\x61ta\x18\x0f \x01(\x0b\x32\x14.google.protobuf.Anyb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,type__pb2.DESCRIPTOR,])




_ACCOUNTMIGRATETX = _descriptor.Descriptor(
  name='AccountMigrateTx',
  full_name='forge_abi.AccountMigrateTx',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pk', full_name='forge_abi.AccountMigrateTx.pk', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='forge_abi.AccountMigrateTx.type', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=95,
  serialized_end=162,
)


_CONSENSUSUPGRADETX = _descriptor.Descriptor(
  name='ConsensusUpgradeTx',
  full_name='forge_abi.ConsensusUpgradeTx',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='validators', full_name='forge_abi.ConsensusUpgradeTx.validators', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_bytes', full_name='forge_abi.ConsensusUpgradeTx.max_bytes', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_gas', full_name='forge_abi.ConsensusUpgradeTx.max_gas', index=2,
      number=3, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_validators', full_name='forge_abi.ConsensusUpgradeTx.max_validators', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_candidates', full_name='forge_abi.ConsensusUpgradeTx.max_candidates', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='forge_abi.ConsensusUpgradeTx.data', index=5,
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
  serialized_start=165,
  serialized_end=347,
)


_CONSUMEASSETTX = _descriptor.Descriptor(
  name='ConsumeAssetTx',
  full_name='forge_abi.ConsumeAssetTx',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='issuer', full_name='forge_abi.ConsumeAssetTx.issuer', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='address', full_name='forge_abi.ConsumeAssetTx.address', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='forge_abi.ConsumeAssetTx.data', index=2,
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
  serialized_start=349,
  serialized_end=434,
)


_CREATEASSETTX = _descriptor.Descriptor(
  name='CreateAssetTx',
  full_name='forge_abi.CreateAssetTx',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='moniker', full_name='forge_abi.CreateAssetTx.moniker', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='forge_abi.CreateAssetTx.data', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='readonly', full_name='forge_abi.CreateAssetTx.readonly', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transferrable', full_name='forge_abi.CreateAssetTx.transferrable', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ttl', full_name='forge_abi.CreateAssetTx.ttl', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parent', full_name='forge_abi.CreateAssetTx.parent', index=5,
      number=6, type=9, cpp_type=9, label=1,
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
  serialized_start=437,
  serialized_end=575,
)


_DECLARETX = _descriptor.Descriptor(
  name='DeclareTx',
  full_name='forge_abi.DeclareTx',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='moniker', full_name='forge_abi.DeclareTx.moniker', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pk', full_name='forge_abi.DeclareTx.pk', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='forge_abi.DeclareTx.type', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='issuer', full_name='forge_abi.DeclareTx.issuer', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='forge_abi.DeclareTx.data', index=4,
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
  serialized_start=578,
  serialized_end=707,
)


_DECLAREFILETX = _descriptor.Descriptor(
  name='DeclareFileTx',
  full_name='forge_abi.DeclareFileTx',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hash', full_name='forge_abi.DeclareFileTx.hash', index=0,
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
  serialized_start=709,
  serialized_end=738,
)


_EXCHANGEINFO = _descriptor.Descriptor(
  name='ExchangeInfo',
  full_name='forge_abi.ExchangeInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='forge_abi.ExchangeInfo.value', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='assets', full_name='forge_abi.ExchangeInfo.assets', index=1,
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
  serialized_start=740,
  serialized_end=805,
)


_EXCHANGETX = _descriptor.Descriptor(
  name='ExchangeTx',
  full_name='forge_abi.ExchangeTx',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='to', full_name='forge_abi.ExchangeTx.to', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sender', full_name='forge_abi.ExchangeTx.sender', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='receiver', full_name='forge_abi.ExchangeTx.receiver', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expired_at', full_name='forge_abi.ExchangeTx.expired_at', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='forge_abi.ExchangeTx.data', index=4,
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
  serialized_start=808,
  serialized_end=1000,
)


_STAKEFORASSET = _descriptor.Descriptor(
  name='stakeForAsset',
  full_name='forge_abi.stakeForAsset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=1002,
  serialized_end=1017,
)


_STAKEFORCHAIN = _descriptor.Descriptor(
  name='stakeForChain',
  full_name='forge_abi.stakeForChain',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=1019,
  serialized_end=1034,
)


_STAKEFORNODE = _descriptor.Descriptor(
  name='StakeForNode',
  full_name='forge_abi.StakeForNode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=1036,
  serialized_end=1050,
)


_STAKEFORUSER = _descriptor.Descriptor(
  name='stakeForUser',
  full_name='forge_abi.stakeForUser',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=1052,
  serialized_end=1066,
)


_STAKETX = _descriptor.Descriptor(
  name='StakeTx',
  full_name='forge_abi.StakeTx',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='to', full_name='forge_abi.StakeTx.to', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='forge_abi.StakeTx.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='forge_abi.StakeTx.message', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='forge_abi.StakeTx.data', index=3,
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
  serialized_start=1068,
  serialized_end=1177,
)


_SYSUPGRADETX = _descriptor.Descriptor(
  name='SysUpgradeTx',
  full_name='forge_abi.SysUpgradeTx',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='task', full_name='forge_abi.SysUpgradeTx.task', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='grace_period', full_name='forge_abi.SysUpgradeTx.grace_period', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='forge_abi.SysUpgradeTx.data', index=2,
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
  serialized_start=1179,
  serialized_end=1289,
)


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
  serialized_start=1291,
  serialized_end=1402,
)


_UPDATEASSETTX = _descriptor.Descriptor(
  name='UpdateAssetTx',
  full_name='forge_abi.UpdateAssetTx',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='forge_abi.UpdateAssetTx.address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='moniker', full_name='forge_abi.UpdateAssetTx.moniker', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='data', full_name='forge_abi.UpdateAssetTx.data', index=2,
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
  serialized_start=1404,
  serialized_end=1489,
)

_ACCOUNTMIGRATETX.fields_by_name['type'].message_type = type__pb2._WALLETTYPE
_CONSENSUSUPGRADETX.fields_by_name['validators'].message_type = type__pb2._VALIDATOR
_CONSENSUSUPGRADETX.fields_by_name['data'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_CONSUMEASSETTX.fields_by_name['data'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_CREATEASSETTX.fields_by_name['data'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_DECLARETX.fields_by_name['type'].message_type = type__pb2._WALLETTYPE
_DECLARETX.fields_by_name['data'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_EXCHANGEINFO.fields_by_name['value'].message_type = type__pb2._BIGUINT
_EXCHANGETX.fields_by_name['sender'].message_type = _EXCHANGEINFO
_EXCHANGETX.fields_by_name['receiver'].message_type = _EXCHANGEINFO
_EXCHANGETX.fields_by_name['expired_at'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_EXCHANGETX.fields_by_name['data'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_STAKETX.fields_by_name['value'].message_type = type__pb2._BIGSINT
_STAKETX.fields_by_name['data'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_SYSUPGRADETX.fields_by_name['task'].message_type = type__pb2._UPGRADETASK
_SYSUPGRADETX.fields_by_name['data'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_TRANSFERTX.fields_by_name['value'].message_type = type__pb2._BIGUINT
_TRANSFERTX.fields_by_name['data'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_UPDATEASSETTX.fields_by_name['data'].message_type = google_dot_protobuf_dot_any__pb2._ANY
DESCRIPTOR.message_types_by_name['AccountMigrateTx'] = _ACCOUNTMIGRATETX
DESCRIPTOR.message_types_by_name['ConsensusUpgradeTx'] = _CONSENSUSUPGRADETX
DESCRIPTOR.message_types_by_name['ConsumeAssetTx'] = _CONSUMEASSETTX
DESCRIPTOR.message_types_by_name['CreateAssetTx'] = _CREATEASSETTX
DESCRIPTOR.message_types_by_name['DeclareTx'] = _DECLARETX
DESCRIPTOR.message_types_by_name['DeclareFileTx'] = _DECLAREFILETX
DESCRIPTOR.message_types_by_name['ExchangeInfo'] = _EXCHANGEINFO
DESCRIPTOR.message_types_by_name['ExchangeTx'] = _EXCHANGETX
DESCRIPTOR.message_types_by_name['stakeForAsset'] = _STAKEFORASSET
DESCRIPTOR.message_types_by_name['stakeForChain'] = _STAKEFORCHAIN
DESCRIPTOR.message_types_by_name['StakeForNode'] = _STAKEFORNODE
DESCRIPTOR.message_types_by_name['stakeForUser'] = _STAKEFORUSER
DESCRIPTOR.message_types_by_name['StakeTx'] = _STAKETX
DESCRIPTOR.message_types_by_name['SysUpgradeTx'] = _SYSUPGRADETX
DESCRIPTOR.message_types_by_name['TransferTx'] = _TRANSFERTX
DESCRIPTOR.message_types_by_name['UpdateAssetTx'] = _UPDATEASSETTX
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AccountMigrateTx = _reflection.GeneratedProtocolMessageType('AccountMigrateTx', (_message.Message,), dict(
  DESCRIPTOR = _ACCOUNTMIGRATETX,
  __module__ = 'tx_pb2'
  # @@protoc_insertion_point(class_scope:forge_abi.AccountMigrateTx)
  ))
_sym_db.RegisterMessage(AccountMigrateTx)

ConsensusUpgradeTx = _reflection.GeneratedProtocolMessageType('ConsensusUpgradeTx', (_message.Message,), dict(
  DESCRIPTOR = _CONSENSUSUPGRADETX,
  __module__ = 'tx_pb2'
  # @@protoc_insertion_point(class_scope:forge_abi.ConsensusUpgradeTx)
  ))
_sym_db.RegisterMessage(ConsensusUpgradeTx)

ConsumeAssetTx = _reflection.GeneratedProtocolMessageType('ConsumeAssetTx', (_message.Message,), dict(
  DESCRIPTOR = _CONSUMEASSETTX,
  __module__ = 'tx_pb2'
  # @@protoc_insertion_point(class_scope:forge_abi.ConsumeAssetTx)
  ))
_sym_db.RegisterMessage(ConsumeAssetTx)

CreateAssetTx = _reflection.GeneratedProtocolMessageType('CreateAssetTx', (_message.Message,), dict(
  DESCRIPTOR = _CREATEASSETTX,
  __module__ = 'tx_pb2'
  # @@protoc_insertion_point(class_scope:forge_abi.CreateAssetTx)
  ))
_sym_db.RegisterMessage(CreateAssetTx)

DeclareTx = _reflection.GeneratedProtocolMessageType('DeclareTx', (_message.Message,), dict(
  DESCRIPTOR = _DECLARETX,
  __module__ = 'tx_pb2'
  # @@protoc_insertion_point(class_scope:forge_abi.DeclareTx)
  ))
_sym_db.RegisterMessage(DeclareTx)

DeclareFileTx = _reflection.GeneratedProtocolMessageType('DeclareFileTx', (_message.Message,), dict(
  DESCRIPTOR = _DECLAREFILETX,
  __module__ = 'tx_pb2'
  # @@protoc_insertion_point(class_scope:forge_abi.DeclareFileTx)
  ))
_sym_db.RegisterMessage(DeclareFileTx)

ExchangeInfo = _reflection.GeneratedProtocolMessageType('ExchangeInfo', (_message.Message,), dict(
  DESCRIPTOR = _EXCHANGEINFO,
  __module__ = 'tx_pb2'
  # @@protoc_insertion_point(class_scope:forge_abi.ExchangeInfo)
  ))
_sym_db.RegisterMessage(ExchangeInfo)

ExchangeTx = _reflection.GeneratedProtocolMessageType('ExchangeTx', (_message.Message,), dict(
  DESCRIPTOR = _EXCHANGETX,
  __module__ = 'tx_pb2'
  # @@protoc_insertion_point(class_scope:forge_abi.ExchangeTx)
  ))
_sym_db.RegisterMessage(ExchangeTx)

stakeForAsset = _reflection.GeneratedProtocolMessageType('stakeForAsset', (_message.Message,), dict(
  DESCRIPTOR = _STAKEFORASSET,
  __module__ = 'tx_pb2'
  # @@protoc_insertion_point(class_scope:forge_abi.stakeForAsset)
  ))
_sym_db.RegisterMessage(stakeForAsset)

stakeForChain = _reflection.GeneratedProtocolMessageType('stakeForChain', (_message.Message,), dict(
  DESCRIPTOR = _STAKEFORCHAIN,
  __module__ = 'tx_pb2'
  # @@protoc_insertion_point(class_scope:forge_abi.stakeForChain)
  ))
_sym_db.RegisterMessage(stakeForChain)

StakeForNode = _reflection.GeneratedProtocolMessageType('StakeForNode', (_message.Message,), dict(
  DESCRIPTOR = _STAKEFORNODE,
  __module__ = 'tx_pb2'
  # @@protoc_insertion_point(class_scope:forge_abi.StakeForNode)
  ))
_sym_db.RegisterMessage(StakeForNode)

stakeForUser = _reflection.GeneratedProtocolMessageType('stakeForUser', (_message.Message,), dict(
  DESCRIPTOR = _STAKEFORUSER,
  __module__ = 'tx_pb2'
  # @@protoc_insertion_point(class_scope:forge_abi.stakeForUser)
  ))
_sym_db.RegisterMessage(stakeForUser)

StakeTx = _reflection.GeneratedProtocolMessageType('StakeTx', (_message.Message,), dict(
  DESCRIPTOR = _STAKETX,
  __module__ = 'tx_pb2'
  # @@protoc_insertion_point(class_scope:forge_abi.StakeTx)
  ))
_sym_db.RegisterMessage(StakeTx)

SysUpgradeTx = _reflection.GeneratedProtocolMessageType('SysUpgradeTx', (_message.Message,), dict(
  DESCRIPTOR = _SYSUPGRADETX,
  __module__ = 'tx_pb2'
  # @@protoc_insertion_point(class_scope:forge_abi.SysUpgradeTx)
  ))
_sym_db.RegisterMessage(SysUpgradeTx)

TransferTx = _reflection.GeneratedProtocolMessageType('TransferTx', (_message.Message,), dict(
  DESCRIPTOR = _TRANSFERTX,
  __module__ = 'tx_pb2'
  # @@protoc_insertion_point(class_scope:forge_abi.TransferTx)
  ))
_sym_db.RegisterMessage(TransferTx)

UpdateAssetTx = _reflection.GeneratedProtocolMessageType('UpdateAssetTx', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEASSETTX,
  __module__ = 'tx_pb2'
  # @@protoc_insertion_point(class_scope:forge_abi.UpdateAssetTx)
  ))
_sym_db.RegisterMessage(UpdateAssetTx)


# @@protoc_insertion_point(module_scope)
