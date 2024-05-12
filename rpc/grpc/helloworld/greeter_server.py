#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @time    : 2023/12/17 9:56
# @author  : CaoChao
# @file    : metadata_server.py
from concurrent import futures

import grpc

from rpc.grpc.helloworld.proto import helloworld_pb2_grpc, helloworld_pb2


class Greeter(helloworld_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return helloworld_pb2.HelloReply(message="Hello, %s!" % request.name)


def serve():
    port = "8051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port("127.0.0.1:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
