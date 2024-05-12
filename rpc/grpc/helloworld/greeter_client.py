#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @time    : 2023/12/17 9:54
# @author  : CaoChao
# @file    : metadata_client.py
import grpc
from rpc.grpc.helloworld.proto import helloworld_pb2_grpc, helloworld_pb2


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    print("Will try to greet world ...")
    with grpc.insecure_channel("localhost:8051") as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        response: helloworld_pb2.HelloReply = stub.SayHello(helloworld_pb2.HelloRequest(name="CaoChao"))
    print("Greeter client received: " + response.message)


if __name__ == "__main__":
    run()
