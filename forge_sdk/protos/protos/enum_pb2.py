# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: enum.proto

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
  name='enum.proto',
  package='forge_abi',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\nenum.proto\x12\tforge_abi*\xc8\n\n\nStatusCode\x12\x06\n\x02ok\x10\x00\x12\x11\n\rinvalid_nonce\x10\x01\x12\x15\n\x11invalid_signature\x10\x02\x12\x18\n\x14invalid_sender_state\x10\x03\x12\x1a\n\x16invalid_receiver_state\x10\x04\x12\x15\n\x11insufficient_data\x10\x05\x12\x15\n\x11insufficient_fund\x10\x06\x12\x11\n\rinvalid_owner\x10\x07\x12\x0e\n\ninvalid_tx\x10\x08\x12\x12\n\x0eunsupported_tx\x10\t\x12\x0e\n\nexpired_tx\x10\n\x12\x10\n\x0ctoo_many_txs\x10\x0b\x12\x17\n\x13invalid_lock_status\x10\x0c\x12\x13\n\x0finvalid_request\x10\r\x12\x13\n\x0finvalid_moniker\x10\x10\x12\x16\n\x12invalid_passphrase\x10\x11\x12\x14\n\x10invalid_multisig\x10\x14\x12\x12\n\x0einvalid_wallet\x10\x15\x12\x14\n\x10invalid_chain_id\x10\x16\x12\x17\n\x13\x63onsensus_rpc_error\x10\x18\x12\x15\n\x11storage_rpc_error\x10\x19\x12\t\n\x05noent\x10\x1a\x12\x14\n\x10\x61\x63\x63ount_migrated\x10\x1b\x12\x15\n\x11unsupported_stake\x10\x1e\x12\x16\n\x12insufficient_stake\x10\x1f\x12\x17\n\x13invalid_stake_state\x10 \x12\x18\n\x14\x65xpired_wallet_token\x10!\x12\x12\n\x0e\x62\x61nned_unstake\x10\"\x12\x11\n\rinvalid_asset\x10#\x12\x13\n\x0finvalid_tx_size\x10$\x12\x18\n\x14invalid_signer_state\x10%\x12\x17\n\x13invalid_forge_state\x10&\x12\x11\n\rexpired_asset\x10\'\x12\x19\n\x15untransferrable_asset\x10(\x12\x12\n\x0ereadonly_asset\x10)\x12\x12\n\x0e\x63onsumed_asset\x10*\x12\x19\n\x15invalid_deposit_value\x10+\x12\x16\n\x12\x65xceed_deposit_cap\x10,\x12\x1a\n\x16invalid_deposit_target\x10-\x12\x15\n\x11invalid_depositor\x10.\x12\x16\n\x12invalid_withdrawer\x10/\x12\x14\n\x10\x64uplicate_tether\x10\x30\x12\x17\n\x13invalid_expiry_date\x10\x31\x12\x13\n\x0finvalid_deposit\x10\x32\x12\x15\n\x11invalid_custodian\x10\x33\x12\x14\n\x10insufficient_gas\x10\x34\x12\x10\n\x0cinvalid_swap\x10\x35\x12\x13\n\x0finvalid_hashkey\x10\x36\x12\x16\n\x12invalid_delegation\x10\x37\x12\x1b\n\x17insufficient_delegation\x10\x38\x12\x1b\n\x17invalid_delegation_rule\x10\x39\x12\x1f\n\x1binvalid_delegation_type_url\x10:\x12\x19\n\x15sender_not_authorized\x10;\x12\x18\n\x14protocol_not_running\x10<\x12\x17\n\x13protocol_not_paused\x10=\x12\x1a\n\x16protocol_not_activated\x10>\x12\x18\n\x14invalid_deactivation\x10?\x12\x0e\n\tforbidden\x10\x93\x03\x12\r\n\x08internal\x10\xf4\x03\x12\x0c\n\x07timeout\x10\xf8\x03*%\n\x07KeyType\x12\x0b\n\x07\x65\x64\x32\x35\x35\x31\x39\x10\x00\x12\r\n\tsecp256k1\x10\x01*f\n\x08HashType\x12\n\n\x06keccak\x10\x00\x12\x08\n\x04sha3\x10\x01\x12\x08\n\x04sha2\x10\x02\x12\x0e\n\nkeccak_384\x10\x06\x12\x0c\n\x08sha3_384\x10\x07\x12\x0e\n\nkeccak_512\x10\r\x12\x0c\n\x08sha3_512\x10\x0e*&\n\x0c\x45ncodingType\x12\n\n\x06\x62\x61se16\x10\x00\x12\n\n\x06\x62\x61se58\x10\x01*\xe9\x01\n\x08RoleType\x12\x10\n\x0crole_account\x10\x00\x12\r\n\trole_node\x10\x01\x12\x0f\n\x0brole_device\x10\x02\x12\x14\n\x10role_application\x10\x03\x12\x17\n\x13role_smart_contract\x10\x04\x12\x0c\n\x08role_bot\x10\x05\x12\x0e\n\nrole_asset\x10\x06\x12\x0e\n\nrole_stake\x10\x07\x12\x12\n\x0erole_validator\x10\x08\x12\x0e\n\nrole_group\x10\t\x12\x0b\n\x07role_tx\x10\n\x12\x0f\n\x0brole_tether\x10\x0b\x12\x0c\n\x08role_any\x10?*\xae\x01\n\x0bUpgradeType\x12\x0e\n\nconfig_app\x10\x00\x12\x10\n\x0c\x63onfig_forge\x10\x01\x12\x0e\n\nconfig_dfs\x10\x02\x12\x14\n\x10\x63onfig_consensus\x10\x03\x12\x0e\n\nconfig_p2p\x10\x04\x12\x0b\n\x07\x65xe_app\x10\n\x12\r\n\texe_forge\x10\x0b\x12\x0b\n\x07\x65xe_dfs\x10\x0c\x12\x11\n\rexe_consensus\x10\r\x12\x0b\n\x07\x65xe_p2p\x10\x0e*\xea\x01\n\rUpgradeAction\x12\n\n\x06verify\x10\x00\x12\n\n\x06\x62\x61\x63kup\x10\x01\x12\x0b\n\x07replace\x10\x02\x12\x0f\n\x0brestart_app\x10\n\x12\x0f\n\x0brestart_dfs\x10\x0b\x12\x15\n\x11restart_consensus\x10\x0c\x12\x0f\n\x0brestart_p2p\x10\r\x12\x11\n\rrestart_forge\x10\x0e\x12\x14\n\x10rollback_if_fail\x10\x1e\x12\x17\n\x13restart_all_if_fail\x10\x1f\x12\x11\n\rcrash_if_fail\x10!\x12\x15\n\x11\x64rop_address_book\x10\x32*d\n\tStateType\x12\x11\n\rstate_account\x10\x00\x12\x0f\n\x0bstate_asset\x10\x01\x12\x11\n\rstate_channel\x10\x02\x12\x0f\n\x0bstate_forge\x10\x03\x12\x0f\n\x0bstate_stake\x10\x04*M\n\tStakeType\x12\x0e\n\nstake_node\x10\x00\x12\x0e\n\nstake_user\x10\x01\x12\x0f\n\x0bstake_asset\x10\x02\x12\x0f\n\x0bstake_chain\x10\x03*9\n\x0eProtocolStatus\x12\x0b\n\x07running\x10\x00\x12\n\n\x06paused\x10\x01\x12\x0e\n\nterminated\x10\x02\x62\x06proto3')
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
      name='expired_tx', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='too_many_txs', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='invalid_lock_status', index=12, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='invalid_request', index=13, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='invalid_moniker', index=14, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='invalid_passphrase', index=15, number=17,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='invalid_multisig', index=16, number=20,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='invalid_wallet', index=17, number=21,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='invalid_chain_id', index=18, number=22,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='consensus_rpc_error', index=19, number=24,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='storage_rpc_error', index=20, number=25,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='noent', index=21, number=26,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='account_migrated', index=22, number=27,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='unsupported_stake', index=23, number=30,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='insufficient_stake', index=24, number=31,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='invalid_stake_state', index=25, number=32,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='expired_wallet_token', index=26, number=33,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='banned_unstake', index=27, number=34,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='invalid_asset', index=28, number=35,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='invalid_tx_size', index=29, number=36,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='invalid_signer_state', index=30, number=37,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='invalid_forge_state', index=31, number=38,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='expired_asset', index=32, number=39,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='untransferrable_asset', index=33, number=40,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='readonly_asset', index=34, number=41,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='consumed_asset', index=35, number=42,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='invalid_deposit_value', index=36, number=43,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='exceed_deposit_cap', index=37, number=44,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='invalid_deposit_target', index=38, number=45,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='invalid_depositor', index=39, number=46,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='invalid_withdrawer', index=40, number=47,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='duplicate_tether', index=41, number=48,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='invalid_expiry_date', index=42, number=49,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='invalid_deposit', index=43, number=50,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='invalid_custodian', index=44, number=51,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='insufficient_gas', index=45, number=52,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='invalid_swap', index=46, number=53,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='invalid_hashkey', index=47, number=54,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='invalid_delegation', index=48, number=55,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='insufficient_delegation', index=49, number=56,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='invalid_delegation_rule', index=50, number=57,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='invalid_delegation_type_url', index=51, number=58,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='sender_not_authorized', index=52, number=59,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='protocol_not_running', index=53, number=60,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='protocol_not_paused', index=54, number=61,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='protocol_not_activated', index=55, number=62,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='invalid_deactivation', index=56, number=63,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='forbidden', index=57, number=403,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='internal', index=58, number=500,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='timeout', index=59, number=504,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=26,
  serialized_end=1378,
)
_sym_db.RegisterEnumDescriptor(_STATUSCODE)

StatusCode = enum_type_wrapper.EnumTypeWrapper(_STATUSCODE)
_KEYTYPE = _descriptor.EnumDescriptor(
  name='KeyType',
  full_name='forge_abi.KeyType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ed25519', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='secp256k1', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1380,
  serialized_end=1417,
)
_sym_db.RegisterEnumDescriptor(_KEYTYPE)

KeyType = enum_type_wrapper.EnumTypeWrapper(_KEYTYPE)
_HASHTYPE = _descriptor.EnumDescriptor(
  name='HashType',
  full_name='forge_abi.HashType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='keccak', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='sha3', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='sha2', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='keccak_384', index=3, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='sha3_384', index=4, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='keccak_512', index=5, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='sha3_512', index=6, number=14,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1419,
  serialized_end=1521,
)
_sym_db.RegisterEnumDescriptor(_HASHTYPE)

HashType = enum_type_wrapper.EnumTypeWrapper(_HASHTYPE)
_ENCODINGTYPE = _descriptor.EnumDescriptor(
  name='EncodingType',
  full_name='forge_abi.EncodingType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='base16', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='base58', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1523,
  serialized_end=1561,
)
_sym_db.RegisterEnumDescriptor(_ENCODINGTYPE)

EncodingType = enum_type_wrapper.EnumTypeWrapper(_ENCODINGTYPE)
_ROLETYPE = _descriptor.EnumDescriptor(
  name='RoleType',
  full_name='forge_abi.RoleType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='role_account', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='role_node', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='role_device', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='role_application', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='role_smart_contract', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='role_bot', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='role_asset', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='role_stake', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='role_validator', index=8, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='role_group', index=9, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='role_tx', index=10, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='role_tether', index=11, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='role_any', index=12, number=63,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1564,
  serialized_end=1797,
)
_sym_db.RegisterEnumDescriptor(_ROLETYPE)

RoleType = enum_type_wrapper.EnumTypeWrapper(_ROLETYPE)
_UPGRADETYPE = _descriptor.EnumDescriptor(
  name='UpgradeType',
  full_name='forge_abi.UpgradeType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='config_app', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='config_forge', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='config_dfs', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='config_consensus', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='config_p2p', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='exe_app', index=5, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='exe_forge', index=6, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='exe_dfs', index=7, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='exe_consensus', index=8, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='exe_p2p', index=9, number=14,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1800,
  serialized_end=1974,
)
_sym_db.RegisterEnumDescriptor(_UPGRADETYPE)

UpgradeType = enum_type_wrapper.EnumTypeWrapper(_UPGRADETYPE)
_UPGRADEACTION = _descriptor.EnumDescriptor(
  name='UpgradeAction',
  full_name='forge_abi.UpgradeAction',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='verify', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='backup', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='replace', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='restart_app', index=3, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='restart_dfs', index=4, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='restart_consensus', index=5, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='restart_p2p', index=6, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='restart_forge', index=7, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='rollback_if_fail', index=8, number=30,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='restart_all_if_fail', index=9, number=31,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='crash_if_fail', index=10, number=33,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='drop_address_book', index=11, number=50,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1977,
  serialized_end=2211,
)
_sym_db.RegisterEnumDescriptor(_UPGRADEACTION)

UpgradeAction = enum_type_wrapper.EnumTypeWrapper(_UPGRADEACTION)
_STATETYPE = _descriptor.EnumDescriptor(
  name='StateType',
  full_name='forge_abi.StateType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='state_account', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='state_asset', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='state_channel', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='state_forge', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='state_stake', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2213,
  serialized_end=2313,
)
_sym_db.RegisterEnumDescriptor(_STATETYPE)

StateType = enum_type_wrapper.EnumTypeWrapper(_STATETYPE)
_STAKETYPE = _descriptor.EnumDescriptor(
  name='StakeType',
  full_name='forge_abi.StakeType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='stake_node', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='stake_user', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='stake_asset', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='stake_chain', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2315,
  serialized_end=2392,
)
_sym_db.RegisterEnumDescriptor(_STAKETYPE)

StakeType = enum_type_wrapper.EnumTypeWrapper(_STAKETYPE)
_PROTOCOLSTATUS = _descriptor.EnumDescriptor(
  name='ProtocolStatus',
  full_name='forge_abi.ProtocolStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='running', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='paused', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='terminated', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2394,
  serialized_end=2451,
)
_sym_db.RegisterEnumDescriptor(_PROTOCOLSTATUS)

ProtocolStatus = enum_type_wrapper.EnumTypeWrapper(_PROTOCOLSTATUS)
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
expired_tx = 10
too_many_txs = 11
invalid_lock_status = 12
invalid_request = 13
invalid_moniker = 16
invalid_passphrase = 17
invalid_multisig = 20
invalid_wallet = 21
invalid_chain_id = 22
consensus_rpc_error = 24
storage_rpc_error = 25
noent = 26
account_migrated = 27
unsupported_stake = 30
insufficient_stake = 31
invalid_stake_state = 32
expired_wallet_token = 33
banned_unstake = 34
invalid_asset = 35
invalid_tx_size = 36
invalid_signer_state = 37
invalid_forge_state = 38
expired_asset = 39
untransferrable_asset = 40
readonly_asset = 41
consumed_asset = 42
invalid_deposit_value = 43
exceed_deposit_cap = 44
invalid_deposit_target = 45
invalid_depositor = 46
invalid_withdrawer = 47
duplicate_tether = 48
invalid_expiry_date = 49
invalid_deposit = 50
invalid_custodian = 51
insufficient_gas = 52
invalid_swap = 53
invalid_hashkey = 54
invalid_delegation = 55
insufficient_delegation = 56
invalid_delegation_rule = 57
invalid_delegation_type_url = 58
sender_not_authorized = 59
protocol_not_running = 60
protocol_not_paused = 61
protocol_not_activated = 62
invalid_deactivation = 63
forbidden = 403
internal = 500
timeout = 504
ed25519 = 0
secp256k1 = 1
keccak = 0
sha3 = 1
sha2 = 2
keccak_384 = 6
sha3_384 = 7
keccak_512 = 13
sha3_512 = 14
base16 = 0
base58 = 1
role_account = 0
role_node = 1
role_device = 2
role_application = 3
role_smart_contract = 4
role_bot = 5
role_asset = 6
role_stake = 7
role_validator = 8
role_group = 9
role_tx = 10
role_tether = 11
role_any = 63
config_app = 0
config_forge = 1
config_dfs = 2
config_consensus = 3
config_p2p = 4
exe_app = 10
exe_forge = 11
exe_dfs = 12
exe_consensus = 13
exe_p2p = 14
verify = 0
backup = 1
replace = 2
restart_app = 10
restart_dfs = 11
restart_consensus = 12
restart_p2p = 13
restart_forge = 14
rollback_if_fail = 30
restart_all_if_fail = 31
crash_if_fail = 33
drop_address_book = 50
state_account = 0
state_asset = 1
state_channel = 2
state_forge = 3
state_stake = 4
stake_node = 0
stake_user = 1
stake_asset = 2
stake_chain = 3
running = 0
paused = 1
terminated = 2


DESCRIPTOR.enum_types_by_name['StatusCode'] = _STATUSCODE
DESCRIPTOR.enum_types_by_name['KeyType'] = _KEYTYPE
DESCRIPTOR.enum_types_by_name['HashType'] = _HASHTYPE
DESCRIPTOR.enum_types_by_name['EncodingType'] = _ENCODINGTYPE
DESCRIPTOR.enum_types_by_name['RoleType'] = _ROLETYPE
DESCRIPTOR.enum_types_by_name['UpgradeType'] = _UPGRADETYPE
DESCRIPTOR.enum_types_by_name['UpgradeAction'] = _UPGRADEACTION
DESCRIPTOR.enum_types_by_name['StateType'] = _STATETYPE
DESCRIPTOR.enum_types_by_name['StakeType'] = _STAKETYPE
DESCRIPTOR.enum_types_by_name['ProtocolStatus'] = _PROTOCOLSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
