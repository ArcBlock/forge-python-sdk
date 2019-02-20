# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from . import rpc_pb2 as rpc__pb2


class ChainRpcStub(object):
    """forge RPC definition

    Notice: when you define a new RPC, please follow the naming convention. Your
    function name is snake case, and req / req are PASCAL case of the function
    name, prefixed with Request / Response. e.g. rpc get_abc(RequestGetAbc)
    returns (ResponseGetAbc). If you break this, RPC builder would complain.

    """

    def __init__(self, channel):
        """Constructor.

        Args:
          channel: A grpc.Channel.
        """
        self.create_tx = channel.unary_unary(
            '/forge_abi.ChainRpc/create_tx',
            request_serializer=rpc__pb2.RequestCreateTx.SerializeToString,
            response_deserializer=rpc__pb2.ResponseCreateTx.FromString,
        )
        self.multisig = channel.unary_unary(
            '/forge_abi.ChainRpc/multisig',
            request_serializer=rpc__pb2.RequestMultisig.SerializeToString,
            response_deserializer=rpc__pb2.ResponseMultisig.FromString,
        )
        self.send_tx = channel.unary_unary(
            '/forge_abi.ChainRpc/send_tx',
            request_serializer=rpc__pb2.RequestSendTx.SerializeToString,
            response_deserializer=rpc__pb2.ResponseSendTx.FromString,
        )
        self.get_tx = channel.stream_stream(
            '/forge_abi.ChainRpc/get_tx',
            request_serializer=rpc__pb2.RequestGetTx.SerializeToString,
            response_deserializer=rpc__pb2.ResponseGetTx.FromString,
        )
        self.get_block = channel.stream_stream(
            '/forge_abi.ChainRpc/get_block',
            request_serializer=rpc__pb2.RequestGetBlock.SerializeToString,
            response_deserializer=rpc__pb2.ResponseGetBlock.FromString,
        )
        self.get_blocks = channel.unary_unary(
            '/forge_abi.ChainRpc/get_blocks',
            request_serializer=rpc__pb2.RequestGetBlocks.SerializeToString,
            response_deserializer=rpc__pb2.ResponseGetBlocks.FromString,
        )
        self.get_unconfirmed_txs = channel.unary_unary(
            '/forge_abi.ChainRpc/get_unconfirmed_txs',
            request_serializer=rpc__pb2.RequestGetUnconfirmedTxs.SerializeToString,
            response_deserializer=rpc__pb2.ResponseGetUnconfirmedTxs.FromString,
        )
        self.get_chain_info = channel.unary_unary(
            '/forge_abi.ChainRpc/get_chain_info',
            request_serializer=rpc__pb2.RequestGetChainInfo.SerializeToString,
            response_deserializer=rpc__pb2.ResponseGetChainInfo.FromString,
        )
        self.search = channel.unary_unary(
            '/forge_abi.ChainRpc/search',
            request_serializer=rpc__pb2.RequestSearch.SerializeToString,
            response_deserializer=rpc__pb2.ResponseSearch.FromString,
        )
        self.get_net_info = channel.unary_unary(
            '/forge_abi.ChainRpc/get_net_info',
            request_serializer=rpc__pb2.RequestGetNetInfo.SerializeToString,
            response_deserializer=rpc__pb2.ResponseGetNetInfo.FromString,
        )
        self.get_validators_info = channel.unary_unary(
            '/forge_abi.ChainRpc/get_validators_info',
            request_serializer=rpc__pb2.RequestGetValidatorsInfo.SerializeToString,
            response_deserializer=rpc__pb2.ResponseGetValidatorsInfo.FromString,
        )
        self.get_config = channel.unary_unary(
            '/forge_abi.ChainRpc/get_config',
            request_serializer=rpc__pb2.RequestGetConfig.SerializeToString,
            response_deserializer=rpc__pb2.ResponseGetConfig.FromString,
        )
        self.get_asset_address = channel.unary_unary(
            '/forge_abi.ChainRpc/get_asset_address',
            request_serializer=rpc__pb2.RequestGetAssetAddress.SerializeToString,
            response_deserializer=rpc__pb2.ResponseGetAssetAddress.FromString,
        )
        self.sign_data = channel.unary_unary(
            '/forge_abi.ChainRpc/sign_data',
            request_serializer=rpc__pb2.RequestSignData.SerializeToString,
            response_deserializer=rpc__pb2.ResponseSignData.FromString,
        )


class ChainRpcServicer(object):
    """forge RPC definition

    Notice: when you define a new RPC, please follow the naming convention. Your
    function name is snake case, and req / req are PASCAL case of the function
    name, prefixed with Request / Response. e.g. rpc get_abc(RequestGetAbc)
    returns (ResponseGetAbc). If you break this, RPC builder would complain.

    """

    def create_tx(self, request, context):
        """tx related
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def multisig(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def send_tx(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_tx(self, request_iterator, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_block(self, request_iterator, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_blocks(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_unconfirmed_txs(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_chain_info(self, request, context):
        """utility
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def search(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_net_info(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_validators_info(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_config(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_asset_address(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def sign_data(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ChainRpcServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'create_tx': grpc.unary_unary_rpc_method_handler(
            servicer.create_tx,
            request_deserializer=rpc__pb2.RequestCreateTx.FromString,
            response_serializer=rpc__pb2.ResponseCreateTx.SerializeToString,
        ),
        'multisig': grpc.unary_unary_rpc_method_handler(
            servicer.multisig,
            request_deserializer=rpc__pb2.RequestMultisig.FromString,
            response_serializer=rpc__pb2.ResponseMultisig.SerializeToString,
        ),
        'send_tx': grpc.unary_unary_rpc_method_handler(
            servicer.send_tx,
            request_deserializer=rpc__pb2.RequestSendTx.FromString,
            response_serializer=rpc__pb2.ResponseSendTx.SerializeToString,
        ),
        'get_tx': grpc.stream_stream_rpc_method_handler(
            servicer.get_tx,
            request_deserializer=rpc__pb2.RequestGetTx.FromString,
            response_serializer=rpc__pb2.ResponseGetTx.SerializeToString,
        ),
        'get_block': grpc.stream_stream_rpc_method_handler(
            servicer.get_block,
            request_deserializer=rpc__pb2.RequestGetBlock.FromString,
            response_serializer=rpc__pb2.ResponseGetBlock.SerializeToString,
        ),
        'get_blocks': grpc.unary_unary_rpc_method_handler(
            servicer.get_blocks,
            request_deserializer=rpc__pb2.RequestGetBlocks.FromString,
            response_serializer=rpc__pb2.ResponseGetBlocks.SerializeToString,
        ),
        'get_unconfirmed_txs': grpc.unary_unary_rpc_method_handler(
            servicer.get_unconfirmed_txs,
            request_deserializer=rpc__pb2.RequestGetUnconfirmedTxs.FromString,
            response_serializer=rpc__pb2.ResponseGetUnconfirmedTxs.SerializeToString,
        ),
        'get_chain_info': grpc.unary_unary_rpc_method_handler(
            servicer.get_chain_info,
            request_deserializer=rpc__pb2.RequestGetChainInfo.FromString,
            response_serializer=rpc__pb2.ResponseGetChainInfo.SerializeToString,
        ),
        'search': grpc.unary_unary_rpc_method_handler(
            servicer.search,
            request_deserializer=rpc__pb2.RequestSearch.FromString,
            response_serializer=rpc__pb2.ResponseSearch.SerializeToString,
        ),
        'get_net_info': grpc.unary_unary_rpc_method_handler(
            servicer.get_net_info,
            request_deserializer=rpc__pb2.RequestGetNetInfo.FromString,
            response_serializer=rpc__pb2.ResponseGetNetInfo.SerializeToString,
        ),
        'get_validators_info': grpc.unary_unary_rpc_method_handler(
            servicer.get_validators_info,
            request_deserializer=rpc__pb2.RequestGetValidatorsInfo.FromString,
            response_serializer=rpc__pb2.ResponseGetValidatorsInfo.SerializeToString,
        ),
        'get_config': grpc.unary_unary_rpc_method_handler(
            servicer.get_config,
            request_deserializer=rpc__pb2.RequestGetConfig.FromString,
            response_serializer=rpc__pb2.ResponseGetConfig.SerializeToString,
        ),
        'get_asset_address': grpc.unary_unary_rpc_method_handler(
            servicer.get_asset_address,
            request_deserializer=rpc__pb2.RequestGetAssetAddress.FromString,
            response_serializer=rpc__pb2.ResponseGetAssetAddress.SerializeToString,
        ),
        'sign_data': grpc.unary_unary_rpc_method_handler(
            servicer.sign_data,
            request_deserializer=rpc__pb2.RequestSignData.FromString,
            response_serializer=rpc__pb2.ResponseSignData.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'forge_abi.ChainRpc', rpc_method_handlers,
    )
    server.add_generic_rpc_handlers((generic_handler,))


class EventRpcStub(object):
    # missing associated documentation comment in .proto file
    pass

    def __init__(self, channel):
        """Constructor.

        Args:
          channel: A grpc.Channel.
        """
        self.subscribe = channel.unary_stream(
            '/forge_abi.EventRpc/subscribe',
            request_serializer=rpc__pb2.RequestSubscribe.SerializeToString,
            response_deserializer=rpc__pb2.ResponseSubscribe.FromString,
        )
        self.unsubscribe = channel.unary_unary(
            '/forge_abi.EventRpc/unsubscribe',
            request_serializer=rpc__pb2.RequestUnsubscribe.SerializeToString,
            response_deserializer=rpc__pb2.ResponseUnsubscribe.FromString,
        )


class EventRpcServicer(object):
    # missing associated documentation comment in .proto file
    pass

    def subscribe(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def unsubscribe(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EventRpcServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'subscribe': grpc.unary_stream_rpc_method_handler(
            servicer.subscribe,
            request_deserializer=rpc__pb2.RequestSubscribe.FromString,
            response_serializer=rpc__pb2.ResponseSubscribe.SerializeToString,
        ),
        'unsubscribe': grpc.unary_unary_rpc_method_handler(
            servicer.unsubscribe,
            request_deserializer=rpc__pb2.RequestUnsubscribe.FromString,
            response_serializer=rpc__pb2.ResponseUnsubscribe.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'forge_abi.EventRpc', rpc_method_handlers,
    )
    server.add_generic_rpc_handlers((generic_handler,))


class FileRpcStub(object):
    # missing associated documentation comment in .proto file
    pass

    def __init__(self, channel):
        """Constructor.

        Args:
          channel: A grpc.Channel.
        """
        self.store_file = channel.stream_unary(
            '/forge_abi.FileRpc/store_file',
            request_serializer=rpc__pb2.RequestStoreFile.SerializeToString,
            response_deserializer=rpc__pb2.ResponseStoreFile.FromString,
        )
        self.load_file = channel.unary_stream(
            '/forge_abi.FileRpc/load_file',
            request_serializer=rpc__pb2.RequestLoadFile.SerializeToString,
            response_deserializer=rpc__pb2.ResponseLoadFile.FromString,
        )
        self.pin_file = channel.unary_unary(
            '/forge_abi.FileRpc/pin_file',
            request_serializer=rpc__pb2.RequestPinFile.SerializeToString,
            response_deserializer=rpc__pb2.ResponsePinFile.FromString,
        )


class FileRpcServicer(object):
    # missing associated documentation comment in .proto file
    pass

    def store_file(self, request_iterator, context):
        """filesystem related
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def load_file(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def pin_file(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FileRpcServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'store_file': grpc.stream_unary_rpc_method_handler(
            servicer.store_file,
            request_deserializer=rpc__pb2.RequestStoreFile.FromString,
            response_serializer=rpc__pb2.ResponseStoreFile.SerializeToString,
        ),
        'load_file': grpc.unary_stream_rpc_method_handler(
            servicer.load_file,
            request_deserializer=rpc__pb2.RequestLoadFile.FromString,
            response_serializer=rpc__pb2.ResponseLoadFile.SerializeToString,
        ),
        'pin_file': grpc.unary_unary_rpc_method_handler(
            servicer.pin_file,
            request_deserializer=rpc__pb2.RequestPinFile.FromString,
            response_serializer=rpc__pb2.ResponsePinFile.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'forge_abi.FileRpc', rpc_method_handlers,
    )
    server.add_generic_rpc_handlers((generic_handler,))


class StateRpcStub(object):
    # missing associated documentation comment in .proto file
    pass

    def __init__(self, channel):
        """Constructor.

        Args:
          channel: A grpc.Channel.
        """
        self.get_account_state = channel.stream_stream(
            '/forge_abi.StateRpc/get_account_state',
            request_serializer=rpc__pb2.RequestGetAccountState.SerializeToString,
            response_deserializer=rpc__pb2.ResponseGetAccountState.FromString,
        )
        self.get_asset_state = channel.stream_stream(
            '/forge_abi.StateRpc/get_asset_state',
            request_serializer=rpc__pb2.RequestGetAssetState.SerializeToString,
            response_deserializer=rpc__pb2.ResponseGetAssetState.FromString,
        )
        self.get_stake_state = channel.stream_stream(
            '/forge_abi.StateRpc/get_stake_state',
            request_serializer=rpc__pb2.RequestGetStakeState.SerializeToString,
            response_deserializer=rpc__pb2.ResponseGetStakeState.FromString,
        )
        self.get_forge_state = channel.unary_unary(
            '/forge_abi.StateRpc/get_forge_state',
            request_serializer=rpc__pb2.RequestGetForgeState.SerializeToString,
            response_deserializer=rpc__pb2.ResponseGetForgeState.FromString,
        )


class StateRpcServicer(object):
    # missing associated documentation comment in .proto file
    pass

    def get_account_state(self, request_iterator, context):
        """state related
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_asset_state(self, request_iterator, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_stake_state(self, request_iterator, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_forge_state(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StateRpcServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'get_account_state': grpc.stream_stream_rpc_method_handler(
            servicer.get_account_state,
            request_deserializer=rpc__pb2.RequestGetAccountState.FromString,
            response_serializer=rpc__pb2.ResponseGetAccountState.SerializeToString,
        ),
        'get_asset_state': grpc.stream_stream_rpc_method_handler(
            servicer.get_asset_state,
            request_deserializer=rpc__pb2.RequestGetAssetState.FromString,
            response_serializer=rpc__pb2.ResponseGetAssetState.SerializeToString,
        ),
        'get_stake_state': grpc.stream_stream_rpc_method_handler(
            servicer.get_stake_state,
            request_deserializer=rpc__pb2.RequestGetStakeState.FromString,
            response_serializer=rpc__pb2.ResponseGetStakeState.SerializeToString,
        ),
        'get_forge_state': grpc.unary_unary_rpc_method_handler(
            servicer.get_forge_state,
            request_deserializer=rpc__pb2.RequestGetForgeState.FromString,
            response_serializer=rpc__pb2.ResponseGetForgeState.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'forge_abi.StateRpc', rpc_method_handlers,
    )
    server.add_generic_rpc_handlers((generic_handler,))


class WalletRpcStub(object):
    # missing associated documentation comment in .proto file
    pass

    def __init__(self, channel):
        """Constructor.

        Args:
          channel: A grpc.Channel.
        """
        self.create_wallet = channel.unary_unary(
            '/forge_abi.WalletRpc/create_wallet',
            request_serializer=rpc__pb2.RequestCreateWallet.SerializeToString,
            response_deserializer=rpc__pb2.ResponseCreateWallet.FromString,
        )
        self.load_wallet = channel.unary_unary(
            '/forge_abi.WalletRpc/load_wallet',
            request_serializer=rpc__pb2.RequestLoadWallet.SerializeToString,
            response_deserializer=rpc__pb2.ResponseLoadWallet.FromString,
        )
        self.recover_wallet = channel.unary_unary(
            '/forge_abi.WalletRpc/recover_wallet',
            request_serializer=rpc__pb2.RequestRecoverWallet.SerializeToString,
            response_deserializer=rpc__pb2.ResponseRecoverWallet.FromString,
        )
        self.list_wallet = channel.unary_stream(
            '/forge_abi.WalletRpc/list_wallet',
            request_serializer=rpc__pb2.RequestListWallet.SerializeToString,
            response_deserializer=rpc__pb2.ResponseListWallet.FromString,
        )
        self.remove_wallet = channel.unary_unary(
            '/forge_abi.WalletRpc/remove_wallet',
            request_serializer=rpc__pb2.RequestRemoveWallet.SerializeToString,
            response_deserializer=rpc__pb2.ResponseRemoveWallet.FromString,
        )
        self.declare_node = channel.unary_unary(
            '/forge_abi.WalletRpc/declare_node',
            request_serializer=rpc__pb2.RequestDeclareNode.SerializeToString,
            response_deserializer=rpc__pb2.ResponseDeclareNode.FromString,
        )


class WalletRpcServicer(object):
    # missing associated documentation comment in .proto file
    pass

    def create_wallet(self, request, context):
        """wallet related
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def load_wallet(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def recover_wallet(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def list_wallet(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def remove_wallet(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def declare_node(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_WalletRpcServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'create_wallet': grpc.unary_unary_rpc_method_handler(
            servicer.create_wallet,
            request_deserializer=rpc__pb2.RequestCreateWallet.FromString,
            response_serializer=rpc__pb2.ResponseCreateWallet.SerializeToString,
        ),
        'load_wallet': grpc.unary_unary_rpc_method_handler(
            servicer.load_wallet,
            request_deserializer=rpc__pb2.RequestLoadWallet.FromString,
            response_serializer=rpc__pb2.ResponseLoadWallet.SerializeToString,
        ),
        'recover_wallet': grpc.unary_unary_rpc_method_handler(
            servicer.recover_wallet,
            request_deserializer=rpc__pb2.RequestRecoverWallet.FromString,
            response_serializer=rpc__pb2.ResponseRecoverWallet.SerializeToString,
        ),
        'list_wallet': grpc.unary_stream_rpc_method_handler(
            servicer.list_wallet,
            request_deserializer=rpc__pb2.RequestListWallet.FromString,
            response_serializer=rpc__pb2.ResponseListWallet.SerializeToString,
        ),
        'remove_wallet': grpc.unary_unary_rpc_method_handler(
            servicer.remove_wallet,
            request_deserializer=rpc__pb2.RequestRemoveWallet.FromString,
            response_serializer=rpc__pb2.ResponseRemoveWallet.SerializeToString,
        ),
        'declare_node': grpc.unary_unary_rpc_method_handler(
            servicer.declare_node,
            request_deserializer=rpc__pb2.RequestDeclareNode.FromString,
            response_serializer=rpc__pb2.ResponseDeclareNode.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'forge_abi.WalletRpc', rpc_method_handlers,
    )
    server.add_generic_rpc_handlers((generic_handler,))


class StatisticRpcStub(object):
    # missing associated documentation comment in .proto file
    pass

    def __init__(self, channel):
        """Constructor.

        Args:
          channel: A grpc.Channel.
        """
        self.get_forge_statistics = channel.unary_unary(
            '/forge_abi.StatisticRpc/get_forge_statistics',
            request_serializer=rpc__pb2.RequestGetForgeStatistics.SerializeToString,
            response_deserializer=rpc__pb2.ResponseGetForgeStatistics.FromString,
        )
        self.list_transactions = channel.unary_unary(
            '/forge_abi.StatisticRpc/list_transactions',
            request_serializer=rpc__pb2.RequestListTransactions.SerializeToString,
            response_deserializer=rpc__pb2.ResponseListTransactions.FromString,
        )


class StatisticRpcServicer(object):
    # missing associated documentation comment in .proto file
    pass

    def get_forge_statistics(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def list_transactions(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StatisticRpcServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'get_forge_statistics': grpc.unary_unary_rpc_method_handler(
            servicer.get_forge_statistics,
            request_deserializer=rpc__pb2.RequestGetForgeStatistics.FromString,
            response_serializer=rpc__pb2.ResponseGetForgeStatistics.SerializeToString,
        ),
        'list_transactions': grpc.unary_unary_rpc_method_handler(
            servicer.list_transactions,
            request_deserializer=rpc__pb2.RequestListTransactions.FromString,
            response_serializer=rpc__pb2.ResponseListTransactions.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'forge_abi.StatisticRpc', rpc_method_handlers,
    )
    server.add_generic_rpc_handlers((generic_handler,))
