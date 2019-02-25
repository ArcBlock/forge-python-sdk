# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: enum.proto
import sys

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import enum_type_wrapper
_b = sys.version_info[0] < 3 and (
    lambda x: x
) or (lambda x: x.encode('latin1'))
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name='enum.proto',
    package='forge_abi',
    syntax='proto3',
    serialized_options=None,
    serialized_pb=_b('\n\nenum.proto\x12\tforge_abi*\xee\x05\n\nStatusCode\x12\x06\n\x02ok\x10\x00\x12\x11\n\rinvalid_nonce\x10\x01\x12\x15\n\x11invalid_signature\x10\x02\x12\x18\n\x14invalid_sender_state\x10\x03\x12\x1a\n\x16invalid_receiver_state\x10\x04\x12\x15\n\x11insufficient_data\x10\x05\x12\x15\n\x11insufficient_fund\x10\x06\x12\x11\n\rinvalid_owner\x10\x07\x12\x0e\n\ninvalid_tx\x10\x08\x12\x12\n\x0eunsupported_tx\x10\t\x12\x0e\n\nexpired_tx\x10\n\x12\x13\n\x0finvalid_moniker\x10\x10\x12\x16\n\x12invalid_passphrase\x10\x11\x12\x14\n\x10invalid_multisig\x10\x14\x12\x12\n\x0einvalid_wallet\x10\x15\x12\x14\n\x10invalid_chain_id\x10\x16\x12\x17\n\x13\x63onsensus_rpc_error\x10\x18\x12\x15\n\x11storage_rpc_error\x10\x19\x12\t\n\x05noent\x10\x1a\x12\x14\n\x10\x61\x63\x63ount_migrated\x10\x1b\x12\x15\n\x11unsupported_stake\x10\x1e\x12\x16\n\x12insufficient_stake\x10\x1f\x12\x17\n\x13invalid_stake_state\x10 \x12\x18\n\x14\x65xpired_wallet_token\x10!\x12\x12\n\x0e\x62\x61nned_unstake\x10\"\x12\x11\n\rinvalid_asset\x10#\x12\x13\n\x0finvalid_tx_size\x10$\x12\x18\n\x14invalid_signer_state\x10%\x12\x17\n\x13invalid_forge_state\x10&\x12\x11\n\rexpired_asset\x10\'\x12\x19\n\x15untransferrable_asset\x10(\x12\x12\n\x0ereadonly_asset\x10)\x12\x13\n\x0f\x61\x63tivated_asset\x10*\x12\x0e\n\tforbidden\x10\x93\x03\x12\r\n\x08internal\x10\xf4\x03*\xc1\x02\n\tTopicType\x12\x0c\n\x08transfer\x10\x00\x12\x0c\n\x08\x65xchange\x10\x01\x12\x0b\n\x07\x64\x65\x63lare\x10\x02\x12\x10\n\x0c\x63reate_asset\x10\x03\x12\x10\n\x0cupdate_asset\x10\x04\x12\t\n\x05stake\x10\x05\x12\x13\n\x0f\x61\x63\x63ount_migrate\x10\x06\x12\x0f\n\x0b\x62\x65gin_block\x10\x10\x12\r\n\tend_block\x10\x11\x12\x15\n\x11\x63onsensus_upgrade\x10\x15\x12\x10\n\x0c\x64\x65\x63lare_file\x10\x16\x12\x0f\n\x0bsys_upgrade\x10\x17\x12\x0f\n\x0b\x61pplication\x10\x18\x12\x12\n\x0e\x61\x63tivate_asset\x10\x19\x12\x12\n\raccount_state\x10\x81\x01\x12\x10\n\x0b\x61sset_state\x10\x82\x01\x12\x10\n\x0b\x66orge_state\x10\x83\x01\x12\x10\n\x0bstake_state\x10\x84\x01*%\n\x07KeyType\x12\x0b\n\x07\x65\x64\x32\x35\x35\x31\x39\x10\x00\x12\r\n\tsecp256k1\x10\x01*\\\n\x08HashType\x12\n\n\x06keccak\x10\x00\x12\x08\n\x04sha3\x10\x01\x12\x0e\n\nkeccak_384\x10\x06\x12\x0c\n\x08sha3_384\x10\x07\x12\x0e\n\nkeccak_512\x10\r\x12\x0c\n\x08sha3_512\x10\x0e*&\n\x0c\x45ncodingType\x12\n\n\x06\x62\x61se16\x10\x00\x12\n\n\x06\x62\x61se58\x10\x01*\xad\x01\n\x08RoleType\x12\x10\n\x0crole_account\x10\x00\x12\r\n\trole_node\x10\x01\x12\x0f\n\x0brole_device\x10\x02\x12\x14\n\x10role_application\x10\x03\x12\x17\n\x13role_smart_contract\x10\x04\x12\x0c\n\x08role_bot\x10\x05\x12\x0e\n\nrole_asset\x10\x06\x12\x0e\n\nrole_stake\x10\x07\x12\x12\n\x0erole_validator\x10\x08*\xae\x01\n\x0bUpgradeType\x12\x0e\n\nconfig_app\x10\x00\x12\x10\n\x0c\x63onfig_forge\x10\x01\x12\x0e\n\nconfig_dfs\x10\x02\x12\x14\n\x10\x63onfig_consensus\x10\x03\x12\x0e\n\nconfig_p2p\x10\x04\x12\x0b\n\x07\x65xe_app\x10\n\x12\r\n\texe_forge\x10\x0b\x12\x0b\n\x07\x65xe_dfs\x10\x0c\x12\x11\n\rexe_consensus\x10\r\x12\x0b\n\x07\x65xe_p2p\x10\x0e*\xea\x01\n\rUpgradeAction\x12\n\n\x06verify\x10\x00\x12\n\n\x06\x62\x61\x63kup\x10\x01\x12\x0b\n\x07replace\x10\x02\x12\x0f\n\x0brestart_app\x10\n\x12\x0f\n\x0brestart_dfs\x10\x0b\x12\x15\n\x11restart_consensus\x10\x0c\x12\x0f\n\x0brestart_p2p\x10\r\x12\x11\n\rrestart_forge\x10\x0e\x12\x14\n\x10rollback_if_fail\x10\x1e\x12\x17\n\x13restart_all_if_fail\x10\x1f\x12\x11\n\rcrash_if_fail\x10!\x12\x15\n\x11\x64rop_address_book\x10\x32*d\n\tStateType\x12\x11\n\rstate_account\x10\x00\x12\x0f\n\x0bstate_asset\x10\x01\x12\x11\n\rstate_channel\x10\x02\x12\x0f\n\x0bstate_forge\x10\x03\x12\x0f\n\x0bstate_stake\x10\x04*M\n\tStakeType\x12\x0e\n\nstake_node\x10\x00\x12\x0e\n\nstake_user\x10\x01\x12\x0f\n\x0bstake_asset\x10\x02\x12\x0f\n\x0bstake_chain\x10\x03\x62\x06proto3'),
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
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='invalid_nonce', index=1, number=1,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='invalid_signature', index=2, number=2,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='invalid_sender_state', index=3, number=3,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='invalid_receiver_state', index=4, number=4,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='insufficient_data', index=5, number=5,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='insufficient_fund', index=6, number=6,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='invalid_owner', index=7, number=7,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='invalid_tx', index=8, number=8,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='unsupported_tx', index=9, number=9,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='expired_tx', index=10, number=10,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='invalid_moniker', index=11, number=16,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='invalid_passphrase', index=12, number=17,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='invalid_multisig', index=13, number=20,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='invalid_wallet', index=14, number=21,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='invalid_chain_id', index=15, number=22,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='consensus_rpc_error', index=16, number=24,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='storage_rpc_error', index=17, number=25,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='noent', index=18, number=26,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='account_migrated', index=19, number=27,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='unsupported_stake', index=20, number=30,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='insufficient_stake', index=21, number=31,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='invalid_stake_state', index=22, number=32,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='expired_wallet_token', index=23, number=33,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='banned_unstake', index=24, number=34,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='invalid_asset', index=25, number=35,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='invalid_tx_size', index=26, number=36,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='invalid_signer_state', index=27, number=37,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='invalid_forge_state', index=28, number=38,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='expired_asset', index=29, number=39,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='untransferrable_asset', index=30, number=40,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='readonly_asset', index=31, number=41,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='activated_asset', index=32, number=42,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='forbidden', index=33, number=403,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='internal', index=34, number=500,
            serialized_options=None,
            type=None,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=26,
    serialized_end=776,
)
_sym_db.RegisterEnumDescriptor(_STATUSCODE)

StatusCode = enum_type_wrapper.EnumTypeWrapper(_STATUSCODE)
_TOPICTYPE = _descriptor.EnumDescriptor(
    name='TopicType',
    full_name='forge_abi.TopicType',
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name='transfer', index=0, number=0,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='exchange', index=1, number=1,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='declare', index=2, number=2,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='create_asset', index=3, number=3,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='update_asset', index=4, number=4,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='stake', index=5, number=5,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='account_migrate', index=6, number=6,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='begin_block', index=7, number=16,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='end_block', index=8, number=17,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='consensus_upgrade', index=9, number=21,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='declare_file', index=10, number=22,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='sys_upgrade', index=11, number=23,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='application', index=12, number=24,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='activate_asset', index=13, number=25,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='account_state', index=14, number=129,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='asset_state', index=15, number=130,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='forge_state', index=16, number=131,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='stake_state', index=17, number=132,
            serialized_options=None,
            type=None,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=779,
    serialized_end=1100,
)
_sym_db.RegisterEnumDescriptor(_TOPICTYPE)

TopicType = enum_type_wrapper.EnumTypeWrapper(_TOPICTYPE)
_KEYTYPE = _descriptor.EnumDescriptor(
    name='KeyType',
    full_name='forge_abi.KeyType',
    filename=None,
    file=DESCRIPTOR,
    values=[
        _descriptor.EnumValueDescriptor(
            name='ed25519', index=0, number=0,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='secp256k1', index=1, number=1,
            serialized_options=None,
            type=None,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=1102,
    serialized_end=1139,
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
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='sha3', index=1, number=1,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='keccak_384', index=2, number=6,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='sha3_384', index=3, number=7,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='keccak_512', index=4, number=13,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='sha3_512', index=5, number=14,
            serialized_options=None,
            type=None,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=1141,
    serialized_end=1233,
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
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='base58', index=1, number=1,
            serialized_options=None,
            type=None,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=1235,
    serialized_end=1273,
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
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='role_node', index=1, number=1,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='role_device', index=2, number=2,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='role_application', index=3, number=3,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='role_smart_contract', index=4, number=4,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='role_bot', index=5, number=5,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='role_asset', index=6, number=6,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='role_stake', index=7, number=7,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='role_validator', index=8, number=8,
            serialized_options=None,
            type=None,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=1276,
    serialized_end=1449,
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
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='config_forge', index=1, number=1,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='config_dfs', index=2, number=2,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='config_consensus', index=3, number=3,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='config_p2p', index=4, number=4,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='exe_app', index=5, number=10,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='exe_forge', index=6, number=11,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='exe_dfs', index=7, number=12,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='exe_consensus', index=8, number=13,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='exe_p2p', index=9, number=14,
            serialized_options=None,
            type=None,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=1452,
    serialized_end=1626,
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
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='backup', index=1, number=1,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='replace', index=2, number=2,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='restart_app', index=3, number=10,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='restart_dfs', index=4, number=11,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='restart_consensus', index=5, number=12,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='restart_p2p', index=6, number=13,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='restart_forge', index=7, number=14,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='rollback_if_fail', index=8, number=30,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='restart_all_if_fail', index=9, number=31,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='crash_if_fail', index=10, number=33,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='drop_address_book', index=11, number=50,
            serialized_options=None,
            type=None,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=1629,
    serialized_end=1863,
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
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='state_asset', index=1, number=1,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='state_channel', index=2, number=2,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='state_forge', index=3, number=3,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='state_stake', index=4, number=4,
            serialized_options=None,
            type=None,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=1865,
    serialized_end=1965,
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
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='stake_user', index=1, number=1,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='stake_asset', index=2, number=2,
            serialized_options=None,
            type=None,
        ),
        _descriptor.EnumValueDescriptor(
            name='stake_chain', index=3, number=3,
            serialized_options=None,
            type=None,
        ),
    ],
    containing_type=None,
    serialized_options=None,
    serialized_start=1967,
    serialized_end=2044,
)
_sym_db.RegisterEnumDescriptor(_STAKETYPE)

StakeType = enum_type_wrapper.EnumTypeWrapper(_STAKETYPE)
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
activated_asset = 42
forbidden = 403
internal = 500
transfer = 0
exchange = 1
declare = 2
create_asset = 3
update_asset = 4
stake = 5
account_migrate = 6
begin_block = 16
end_block = 17
consensus_upgrade = 21
declare_file = 22
sys_upgrade = 23
application = 24
activate_asset = 25
account_state = 129
asset_state = 130
forge_state = 131
stake_state = 132
ed25519 = 0
secp256k1 = 1
keccak = 0
sha3 = 1
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


DESCRIPTOR.enum_types_by_name['StatusCode'] = _STATUSCODE
DESCRIPTOR.enum_types_by_name['TopicType'] = _TOPICTYPE
DESCRIPTOR.enum_types_by_name['KeyType'] = _KEYTYPE
DESCRIPTOR.enum_types_by_name['HashType'] = _HASHTYPE
DESCRIPTOR.enum_types_by_name['EncodingType'] = _ENCODINGTYPE
DESCRIPTOR.enum_types_by_name['RoleType'] = _ROLETYPE
DESCRIPTOR.enum_types_by_name['UpgradeType'] = _UPGRADETYPE
DESCRIPTOR.enum_types_by_name['UpgradeAction'] = _UPGRADEACTION
DESCRIPTOR.enum_types_by_name['StateType'] = _STATETYPE
DESCRIPTOR.enum_types_by_name['StakeType'] = _STAKETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
