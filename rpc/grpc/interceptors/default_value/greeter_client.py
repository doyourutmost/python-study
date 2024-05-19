from __future__ import print_function

import logging

import default_value_client_interceptor
import grpc

from rpc.grpc.interceptors.headers import header_manipulator_client_interceptor
from rpc.grpc.interceptors.proto import helloworld_pb2_grpc, helloworld_pb2


def run():
    default_value = helloworld_pb2.HelloReply(
        message="Hello from your local interceptor!"
    )
    default_value_interceptor = (
        default_value_client_interceptor.DefaultValueClientInterceptor(
            default_value
        )
    )
    header_adder_interceptor = (
        header_manipulator_client_interceptor.header_adder_interceptor(
            "one-time-password", "426"
        )
    )
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel("localhost:8051") as channel:
        intercept_channel = grpc.intercept_channel(
            channel, header_adder_interceptor, default_value_interceptor,
        )
        stub = helloworld_pb2_grpc.GreeterStub(intercept_channel)
        response = stub.SayHello(helloworld_pb2.HelloRequest(name="you"))
    print("Greeter client received: " + response.message)


if __name__ == "__main__":
    logging.basicConfig()
    run()
