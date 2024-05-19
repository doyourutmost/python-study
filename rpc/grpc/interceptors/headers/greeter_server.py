from concurrent import futures
import logging

import grpc
from rpc.grpc.interceptors.proto import helloworld_pb2_grpc, helloworld_pb2

from request_header_validator_interceptor import (
    RequestHeaderValidatorInterceptor,
)


class Greeter(helloworld_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return helloworld_pb2.HelloReply(message="Hello, %s!" % request.name)


def serve():
    header_validator = RequestHeaderValidatorInterceptor(
        "one-time-password",
        "42",
        grpc.StatusCode.UNAUTHENTICATED,
        "Access denied!",
    )
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10),
        interceptors=(header_validator,),
    )
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port("[::]:8051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
