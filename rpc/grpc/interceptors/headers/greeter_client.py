import logging

import grpc
import header_manipulator_client_interceptor
from rpc.grpc.interceptors.proto import helloworld_pb2_grpc, helloworld_pb2


def run():
    header_adder_interceptor = (
        header_manipulator_client_interceptor.header_adder_interceptor(
            "one-time-password", "42"
        )
    )
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel("localhost:8051") as channel:
        intercept_channel = grpc.intercept_channel(
            channel, header_adder_interceptor
        )
        stub = helloworld_pb2_grpc.GreeterStub(intercept_channel)
        response = stub.SayHello(helloworld_pb2.HelloRequest(name="you"))
    print("Greeter client received: " + response.message)


if __name__ == "__main__":
    logging.basicConfig()
    run()
