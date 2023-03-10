# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from lndgrpc.compiled import peers_pb2 as lndgrpc_dot_compiled_dot_peers__pb2


class PeersStub(object):
    """Peers is a service that can be used to get information and interact
    with the other nodes of the network.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.UpdateNodeAnnouncement = channel.unary_unary(
                '/peersrpc.Peers/UpdateNodeAnnouncement',
                request_serializer=lndgrpc_dot_compiled_dot_peers__pb2.NodeAnnouncementUpdateRequest.SerializeToString,
                response_deserializer=lndgrpc_dot_compiled_dot_peers__pb2.NodeAnnouncementUpdateResponse.FromString,
                )


class PeersServicer(object):
    """Peers is a service that can be used to get information and interact
    with the other nodes of the network.
    """

    def UpdateNodeAnnouncement(self, request, context):
        """lncli: peers updatenodeannouncement
        UpdateNodeAnnouncement allows the caller to update the node parameters
        and broadcasts a new version of the node announcement to its peers.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PeersServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'UpdateNodeAnnouncement': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateNodeAnnouncement,
                    request_deserializer=lndgrpc_dot_compiled_dot_peers__pb2.NodeAnnouncementUpdateRequest.FromString,
                    response_serializer=lndgrpc_dot_compiled_dot_peers__pb2.NodeAnnouncementUpdateResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'peersrpc.Peers', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Peers(object):
    """Peers is a service that can be used to get information and interact
    with the other nodes of the network.
    """

    @staticmethod
    def UpdateNodeAnnouncement(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/peersrpc.Peers/UpdateNodeAnnouncement',
            lndgrpc_dot_compiled_dot_peers__pb2.NodeAnnouncementUpdateRequest.SerializeToString,
            lndgrpc_dot_compiled_dot_peers__pb2.NodeAnnouncementUpdateResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
