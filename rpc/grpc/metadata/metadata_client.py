import logging

import grpc
from rpc.grpc.helloworld.proto import helloworld_pb2_grpc, helloworld_pb2


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel("localhost:8051") as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        response, call = stub.SayHello.with_call(
            helloworld_pb2.HelloRequest(name="you"),
            metadata=(
                ("initial-metadata-1", "The value should be str"),
                (
                    "binary-metadata-bin",
                    b"With -bin surffix, the value can be bytes",
                ),
                ("accesstoken", "gRPC Python is great"),
            ),
        )

    print("Greeter client received: " + response.message)
    for key, value in call.trailing_metadata():
        print(
            "Greeter client received trailing metadata: key=%s value=%s"
            % (key, value)
        )


if __name__ == "__main__":
    logging.basicConfig()
    run()
