# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from lndgrpc.compiled import chainkit_pb2 as lndgrpc_dot_compiled_dot_chainkit__pb2


class ChainKitStub(object):
    """ChainKit is a service that can be used to get information from the
    chain backend.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetBlock = channel.unary_unary(
                '/chainrpc.ChainKit/GetBlock',
                request_serializer=lndgrpc_dot_compiled_dot_chainkit__pb2.GetBlockRequest.SerializeToString,
                response_deserializer=lndgrpc_dot_compiled_dot_chainkit__pb2.GetBlockResponse.FromString,
                )
        self.GetBestBlock = channel.unary_unary(
                '/chainrpc.ChainKit/GetBestBlock',
                request_serializer=lndgrpc_dot_compiled_dot_chainkit__pb2.GetBestBlockRequest.SerializeToString,
                response_deserializer=lndgrpc_dot_compiled_dot_chainkit__pb2.GetBestBlockResponse.FromString,
                )
        self.GetBlockHash = channel.unary_unary(
                '/chainrpc.ChainKit/GetBlockHash',
                request_serializer=lndgrpc_dot_compiled_dot_chainkit__pb2.GetBlockHashRequest.SerializeToString,
                response_deserializer=lndgrpc_dot_compiled_dot_chainkit__pb2.GetBlockHashResponse.FromString,
                )


class ChainKitServicer(object):
    """ChainKit is a service that can be used to get information from the
    chain backend.
    """

    def GetBlock(self, request, context):
        """lncli: `chain getblock`
        GetBlock returns a block given the corresponding block hash.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBestBlock(self, request, context):
        """lncli: `chain getbestblock`
        GetBestBlock returns the block hash and current height from the valid
        most-work chain.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBlockHash(self, request, context):
        """lncli: `chain getblockhash`
        GetBlockHash returns the hash of the block in the best blockchain
        at the given height.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ChainKitServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetBlock': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBlock,
                    request_deserializer=lndgrpc_dot_compiled_dot_chainkit__pb2.GetBlockRequest.FromString,
                    response_serializer=lndgrpc_dot_compiled_dot_chainkit__pb2.GetBlockResponse.SerializeToString,
            ),
            'GetBestBlock': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBestBlock,
                    request_deserializer=lndgrpc_dot_compiled_dot_chainkit__pb2.GetBestBlockRequest.FromString,
                    response_serializer=lndgrpc_dot_compiled_dot_chainkit__pb2.GetBestBlockResponse.SerializeToString,
            ),
            'GetBlockHash': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBlockHash,
                    request_deserializer=lndgrpc_dot_compiled_dot_chainkit__pb2.GetBlockHashRequest.FromString,
                    response_serializer=lndgrpc_dot_compiled_dot_chainkit__pb2.GetBlockHashResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'chainrpc.ChainKit', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ChainKit(object):
    """ChainKit is a service that can be used to get information from the
    chain backend.
    """

    @staticmethod
    def GetBlock(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/chainrpc.ChainKit/GetBlock',
            lndgrpc_dot_compiled_dot_chainkit__pb2.GetBlockRequest.SerializeToString,
            lndgrpc_dot_compiled_dot_chainkit__pb2.GetBlockResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetBestBlock(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/chainrpc.ChainKit/GetBestBlock',
            lndgrpc_dot_compiled_dot_chainkit__pb2.GetBestBlockRequest.SerializeToString,
            lndgrpc_dot_compiled_dot_chainkit__pb2.GetBestBlockResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetBlockHash(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/chainrpc.ChainKit/GetBlockHash',
            lndgrpc_dot_compiled_dot_chainkit__pb2.GetBlockHashRequest.SerializeToString,
            lndgrpc_dot_compiled_dot_chainkit__pb2.GetBlockHashResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
