# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: service.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import rpc_pb2 as rpc__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='service.proto',
  package='forge_abi',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\rservice.proto\x12\tforge_abi\x1a\trpc.proto2\xf1\x07\n\x08\x43hainRpc\x12\x44\n\tcreate_tx\x12\x1a.forge_abi.RequestCreateTx\x1a\x1b.forge_abi.ResponseCreateTx\x12\x43\n\x08multisig\x12\x1a.forge_abi.RequestMultisig\x1a\x1b.forge_abi.ResponseMultisig\x12>\n\x07send_tx\x12\x18.forge_abi.RequestSendTx\x1a\x19.forge_abi.ResponseSendTx\x12?\n\x06get_tx\x12\x17.forge_abi.RequestGetTx\x1a\x18.forge_abi.ResponseGetTx(\x01\x30\x01\x12H\n\tget_block\x12\x1a.forge_abi.RequestGetBlock\x1a\x1b.forge_abi.ResponseGetBlock(\x01\x30\x01\x12G\n\nget_blocks\x12\x1b.forge_abi.RequestGetBlocks\x1a\x1c.forge_abi.ResponseGetBlocks\x12`\n\x13get_unconfirmed_txs\x12#.forge_abi.RequestGetUnconfirmedTxs\x1a$.forge_abi.ResponseGetUnconfirmedTxs\x12Q\n\x0eget_chain_info\x12\x1e.forge_abi.RequestGetChainInfo\x1a\x1f.forge_abi.ResponseGetChainInfo\x12=\n\x06search\x12\x18.forge_abi.RequestSearch\x1a\x19.forge_abi.ResponseSearch\x12K\n\x0cget_net_info\x12\x1c.forge_abi.RequestGetNetInfo\x1a\x1d.forge_abi.ResponseGetNetInfo\x12`\n\x13get_validators_info\x12#.forge_abi.RequestGetValidatorsInfo\x1a$.forge_abi.ResponseGetValidatorsInfo\x12G\n\nget_config\x12\x1b.forge_abi.RequestGetConfig\x1a\x1c.forge_abi.ResponseGetConfig\x12Z\n\x11get_asset_address\x12!.forge_abi.RequestGetAssetAddress\x1a\".forge_abi.ResponseGetAssetAddress2\xa2\x01\n\x08\x45ventRpc\x12H\n\tsubscribe\x12\x1b.forge_abi.RequestSubscribe\x1a\x1c.forge_abi.ResponseSubscribe0\x01\x12L\n\x0bunsubscribe\x12\x1d.forge_abi.RequestUnsubscribe\x1a\x1e.forge_abi.ResponseUnsubscribe2\xdf\x01\n\x07\x46ileRpc\x12I\n\nstore_file\x12\x1b.forge_abi.RequestStoreFile\x1a\x1c.forge_abi.ResponseStoreFile(\x01\x12\x46\n\tload_file\x12\x1a.forge_abi.RequestLoadFile\x1a\x1b.forge_abi.ResponseLoadFile0\x01\x12\x41\n\x08pin_file\x12\x19.forge_abi.RequestPinFile\x1a\x1a.forge_abi.ResponsePinFile2\xf4\x02\n\x08StateRpc\x12^\n\x11get_account_state\x12!.forge_abi.RequestGetAccountState\x1a\".forge_abi.ResponseGetAccountState(\x01\x30\x01\x12X\n\x0fget_asset_state\x12\x1f.forge_abi.RequestGetAssetState\x1a .forge_abi.ResponseGetAssetState(\x01\x30\x01\x12X\n\x0fget_stake_state\x12\x1f.forge_abi.RequestGetStakeState\x1a .forge_abi.ResponseGetStakeState(\x01\x30\x01\x12T\n\x0fget_forge_state\x12\x1f.forge_abi.RequestGetForgeState\x1a .forge_abi.ResponseGetForgeState2\xed\x03\n\tWalletRpc\x12P\n\rcreate_wallet\x12\x1e.forge_abi.RequestCreateWallet\x1a\x1f.forge_abi.ResponseCreateWallet\x12J\n\x0bload_wallet\x12\x1c.forge_abi.RequestLoadWallet\x1a\x1d.forge_abi.ResponseLoadWallet\x12S\n\x0erecover_wallet\x12\x1f.forge_abi.RequestRecoverWallet\x1a .forge_abi.ResponseRecoverWallet\x12L\n\x0blist_wallet\x12\x1c.forge_abi.RequestListWallet\x1a\x1d.forge_abi.ResponseListWallet0\x01\x12P\n\rremove_wallet\x12\x1e.forge_abi.RequestRemoveWallet\x1a\x1f.forge_abi.ResponseRemoveWallet\x12M\n\x0c\x64\x65\x63lare_node\x12\x1d.forge_abi.RequestDeclareNode\x1a\x1e.forge_abi.ResponseDeclareNode2\xd1\x01\n\x0cStatisticRpc\x12\x63\n\x14get_forge_statistics\x12$.forge_abi.RequestGetForgeStatistics\x1a%.forge_abi.ResponseGetForgeStatistics\x12\\\n\x11list_transactions\x12\".forge_abi.RequestListTransactions\x1a#.forge_abi.ResponseListTransactionsb\x06proto3')
  ,
  dependencies=[rpc__pb2.DESCRIPTOR,])



_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_CHAINRPC = _descriptor.ServiceDescriptor(
  name='ChainRpc',
  full_name='forge_abi.ChainRpc',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=40,
  serialized_end=1049,
  methods=[
  _descriptor.MethodDescriptor(
    name='create_tx',
    full_name='forge_abi.ChainRpc.create_tx',
    index=0,
    containing_service=None,
    input_type=rpc__pb2._REQUESTCREATETX,
    output_type=rpc__pb2._RESPONSECREATETX,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='multisig',
    full_name='forge_abi.ChainRpc.multisig',
    index=1,
    containing_service=None,
    input_type=rpc__pb2._REQUESTMULTISIG,
    output_type=rpc__pb2._RESPONSEMULTISIG,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='send_tx',
    full_name='forge_abi.ChainRpc.send_tx',
    index=2,
    containing_service=None,
    input_type=rpc__pb2._REQUESTSENDTX,
    output_type=rpc__pb2._RESPONSESENDTX,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='get_tx',
    full_name='forge_abi.ChainRpc.get_tx',
    index=3,
    containing_service=None,
    input_type=rpc__pb2._REQUESTGETTX,
    output_type=rpc__pb2._RESPONSEGETTX,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='get_block',
    full_name='forge_abi.ChainRpc.get_block',
    index=4,
    containing_service=None,
    input_type=rpc__pb2._REQUESTGETBLOCK,
    output_type=rpc__pb2._RESPONSEGETBLOCK,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='get_blocks',
    full_name='forge_abi.ChainRpc.get_blocks',
    index=5,
    containing_service=None,
    input_type=rpc__pb2._REQUESTGETBLOCKS,
    output_type=rpc__pb2._RESPONSEGETBLOCKS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='get_unconfirmed_txs',
    full_name='forge_abi.ChainRpc.get_unconfirmed_txs',
    index=6,
    containing_service=None,
    input_type=rpc__pb2._REQUESTGETUNCONFIRMEDTXS,
    output_type=rpc__pb2._RESPONSEGETUNCONFIRMEDTXS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='get_chain_info',
    full_name='forge_abi.ChainRpc.get_chain_info',
    index=7,
    containing_service=None,
    input_type=rpc__pb2._REQUESTGETCHAININFO,
    output_type=rpc__pb2._RESPONSEGETCHAININFO,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='search',
    full_name='forge_abi.ChainRpc.search',
    index=8,
    containing_service=None,
    input_type=rpc__pb2._REQUESTSEARCH,
    output_type=rpc__pb2._RESPONSESEARCH,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='get_net_info',
    full_name='forge_abi.ChainRpc.get_net_info',
    index=9,
    containing_service=None,
    input_type=rpc__pb2._REQUESTGETNETINFO,
    output_type=rpc__pb2._RESPONSEGETNETINFO,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='get_validators_info',
    full_name='forge_abi.ChainRpc.get_validators_info',
    index=10,
    containing_service=None,
    input_type=rpc__pb2._REQUESTGETVALIDATORSINFO,
    output_type=rpc__pb2._RESPONSEGETVALIDATORSINFO,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='get_config',
    full_name='forge_abi.ChainRpc.get_config',
    index=11,
    containing_service=None,
    input_type=rpc__pb2._REQUESTGETCONFIG,
    output_type=rpc__pb2._RESPONSEGETCONFIG,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='get_asset_address',
    full_name='forge_abi.ChainRpc.get_asset_address',
    index=12,
    containing_service=None,
    input_type=rpc__pb2._REQUESTGETASSETADDRESS,
    output_type=rpc__pb2._RESPONSEGETASSETADDRESS,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CHAINRPC)

DESCRIPTOR.services_by_name['ChainRpc'] = _CHAINRPC


_EVENTRPC = _descriptor.ServiceDescriptor(
  name='EventRpc',
  full_name='forge_abi.EventRpc',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  serialized_start=1052,
  serialized_end=1214,
  methods=[
  _descriptor.MethodDescriptor(
    name='subscribe',
    full_name='forge_abi.EventRpc.subscribe',
    index=0,
    containing_service=None,
    input_type=rpc__pb2._REQUESTSUBSCRIBE,
    output_type=rpc__pb2._RESPONSESUBSCRIBE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='unsubscribe',
    full_name='forge_abi.EventRpc.unsubscribe',
    index=1,
    containing_service=None,
    input_type=rpc__pb2._REQUESTUNSUBSCRIBE,
    output_type=rpc__pb2._RESPONSEUNSUBSCRIBE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_EVENTRPC)

DESCRIPTOR.services_by_name['EventRpc'] = _EVENTRPC


_FILERPC = _descriptor.ServiceDescriptor(
  name='FileRpc',
  full_name='forge_abi.FileRpc',
  file=DESCRIPTOR,
  index=2,
  serialized_options=None,
  serialized_start=1217,
  serialized_end=1440,
  methods=[
  _descriptor.MethodDescriptor(
    name='store_file',
    full_name='forge_abi.FileRpc.store_file',
    index=0,
    containing_service=None,
    input_type=rpc__pb2._REQUESTSTOREFILE,
    output_type=rpc__pb2._RESPONSESTOREFILE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='load_file',
    full_name='forge_abi.FileRpc.load_file',
    index=1,
    containing_service=None,
    input_type=rpc__pb2._REQUESTLOADFILE,
    output_type=rpc__pb2._RESPONSELOADFILE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='pin_file',
    full_name='forge_abi.FileRpc.pin_file',
    index=2,
    containing_service=None,
    input_type=rpc__pb2._REQUESTPINFILE,
    output_type=rpc__pb2._RESPONSEPINFILE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_FILERPC)

DESCRIPTOR.services_by_name['FileRpc'] = _FILERPC


_STATERPC = _descriptor.ServiceDescriptor(
  name='StateRpc',
  full_name='forge_abi.StateRpc',
  file=DESCRIPTOR,
  index=3,
  serialized_options=None,
  serialized_start=1443,
  serialized_end=1815,
  methods=[
  _descriptor.MethodDescriptor(
    name='get_account_state',
    full_name='forge_abi.StateRpc.get_account_state',
    index=0,
    containing_service=None,
    input_type=rpc__pb2._REQUESTGETACCOUNTSTATE,
    output_type=rpc__pb2._RESPONSEGETACCOUNTSTATE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='get_asset_state',
    full_name='forge_abi.StateRpc.get_asset_state',
    index=1,
    containing_service=None,
    input_type=rpc__pb2._REQUESTGETASSETSTATE,
    output_type=rpc__pb2._RESPONSEGETASSETSTATE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='get_stake_state',
    full_name='forge_abi.StateRpc.get_stake_state',
    index=2,
    containing_service=None,
    input_type=rpc__pb2._REQUESTGETSTAKESTATE,
    output_type=rpc__pb2._RESPONSEGETSTAKESTATE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='get_forge_state',
    full_name='forge_abi.StateRpc.get_forge_state',
    index=3,
    containing_service=None,
    input_type=rpc__pb2._REQUESTGETFORGESTATE,
    output_type=rpc__pb2._RESPONSEGETFORGESTATE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_STATERPC)

DESCRIPTOR.services_by_name['StateRpc'] = _STATERPC


_WALLETRPC = _descriptor.ServiceDescriptor(
  name='WalletRpc',
  full_name='forge_abi.WalletRpc',
  file=DESCRIPTOR,
  index=4,
  serialized_options=None,
  serialized_start=1818,
  serialized_end=2311,
  methods=[
  _descriptor.MethodDescriptor(
    name='create_wallet',
    full_name='forge_abi.WalletRpc.create_wallet',
    index=0,
    containing_service=None,
    input_type=rpc__pb2._REQUESTCREATEWALLET,
    output_type=rpc__pb2._RESPONSECREATEWALLET,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='load_wallet',
    full_name='forge_abi.WalletRpc.load_wallet',
    index=1,
    containing_service=None,
    input_type=rpc__pb2._REQUESTLOADWALLET,
    output_type=rpc__pb2._RESPONSELOADWALLET,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='recover_wallet',
    full_name='forge_abi.WalletRpc.recover_wallet',
    index=2,
    containing_service=None,
    input_type=rpc__pb2._REQUESTRECOVERWALLET,
    output_type=rpc__pb2._RESPONSERECOVERWALLET,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='list_wallet',
    full_name='forge_abi.WalletRpc.list_wallet',
    index=3,
    containing_service=None,
    input_type=rpc__pb2._REQUESTLISTWALLET,
    output_type=rpc__pb2._RESPONSELISTWALLET,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='remove_wallet',
    full_name='forge_abi.WalletRpc.remove_wallet',
    index=4,
    containing_service=None,
    input_type=rpc__pb2._REQUESTREMOVEWALLET,
    output_type=rpc__pb2._RESPONSEREMOVEWALLET,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='declare_node',
    full_name='forge_abi.WalletRpc.declare_node',
    index=5,
    containing_service=None,
    input_type=rpc__pb2._REQUESTDECLARENODE,
    output_type=rpc__pb2._RESPONSEDECLARENODE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_WALLETRPC)

DESCRIPTOR.services_by_name['WalletRpc'] = _WALLETRPC


_STATISTICRPC = _descriptor.ServiceDescriptor(
  name='StatisticRpc',
  full_name='forge_abi.StatisticRpc',
  file=DESCRIPTOR,
  index=5,
  serialized_options=None,
  serialized_start=2314,
  serialized_end=2523,
  methods=[
  _descriptor.MethodDescriptor(
    name='get_forge_statistics',
    full_name='forge_abi.StatisticRpc.get_forge_statistics',
    index=0,
    containing_service=None,
    input_type=rpc__pb2._REQUESTGETFORGESTATISTICS,
    output_type=rpc__pb2._RESPONSEGETFORGESTATISTICS,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='list_transactions',
    full_name='forge_abi.StatisticRpc.list_transactions',
    index=1,
    containing_service=None,
    input_type=rpc__pb2._REQUESTLISTTRANSACTIONS,
    output_type=rpc__pb2._RESPONSELISTTRANSACTIONS,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_STATISTICRPC)

DESCRIPTOR.services_by_name['StatisticRpc'] = _STATISTICRPC

# @@protoc_insertion_point(module_scope)
