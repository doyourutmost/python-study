import asyncio
import logging

import grpc
from rpc.grpc.stream.proto import stream_pb2_grpc, stream_pb2


def run() -> None:
    with grpc.insecure_channel("localhost:8051") as channel:
        stub = stream_pb2_grpc.MultiGreeterStub(channel)

        # Direct read from the stub
        hello_stream = stub.sayHello(
            stream_pb2.HelloRequest(name="you", num_greetings=5)
        )
        for response in hello_stream:
            print(
                "Greeter client received from direct read: " + response.message
            )


if __name__ == "__main__":
    run()
