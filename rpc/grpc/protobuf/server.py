#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @time    : 2023/12/17 9:56
# @author  : CaoChao
# @file    : metadata_server.py
from concurrent import futures

import grpc

from rpc.grpc.protobuf.proto import protobuf_pb2_grpc, protobuf_pb2


class Echoer(protobuf_pb2_grpc.EchoServicer):
    def TestEcho(self, request, context):
        resp = protobuf_pb2.EchoResponse()
        resp.name = request.name
        resp.hobbies.extend(request.hobbies)
        resp.email = request.email
        resp.sex = request.sex
        resp.address.city = request.address.city
        resp.address.province = request.address.province
        resp.company.name = request.company.name
        resp.company.address.city = request.company.address.city
        resp.company.address.province = request.company.address.province
        # 解压Any
        if request.any.Is(protobuf_pb2.Address.DESCRIPTOR):
            address = protobuf_pb2.Address()
            request.any.Unpack(address)
            print("Any解压: %s" % address)
        for key, value in request.map.items():
            resp.map[key] = value
        resp.timestamp.seconds = request.timestamp.seconds
        resp.timestamp.nanos = request.timestamp.nanos
        return resp

    def TestEmpty(self, request, context):
        return protobuf_pb2.google_dot_protobuf_dot_empty__pb2.Empty()


def serve():
    port = "8051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    protobuf_pb2_grpc.add_EchoServicer_to_server(Echoer(), server)
    server.add_insecure_port("127.0.0.1:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
