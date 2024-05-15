# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from . import protobuf_pb2 as protobuf__pb2


class EchoStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.TestEcho = channel.unary_unary(
                '/Echo/TestEcho',
                request_serializer=protobuf__pb2.EchoRequest.SerializeToString,
                response_deserializer=protobuf__pb2.EchoResponse.FromString,
                )
        self.TestEmpty = channel.unary_unary(
                '/Echo/TestEmpty',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class EchoServicer(object):
    """Missing associated documentation comment in .proto file."""

    def TestEcho(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TestEmpty(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_EchoServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'TestEcho': grpc.unary_unary_rpc_method_handler(
                    servicer.TestEcho,
                    request_deserializer=protobuf__pb2.EchoRequest.FromString,
                    response_serializer=protobuf__pb2.EchoResponse.SerializeToString,
            ),
            'TestEmpty': grpc.unary_unary_rpc_method_handler(
                    servicer.TestEmpty,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Echo', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Echo(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def TestEcho(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Echo/TestEcho',
            protobuf__pb2.EchoRequest.SerializeToString,
            protobuf__pb2.EchoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TestEmpty(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Echo/TestEmpty',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
