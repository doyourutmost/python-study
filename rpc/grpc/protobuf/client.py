#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @time    : 2023/12/17 9:54
# @author  : CaoChao
# @file    : metadata_client.py
import grpc
from rpc.grpc.protobuf.proto import protobuf_pb2_grpc, protobuf_pb2, protobuf_import_pb2


def run():
    print("Will try to greet world ...")
    with grpc.insecure_channel("localhost:8051") as channel:
        stub = protobuf_pb2_grpc.EchoStub(channel)
        address = protobuf_pb2.Address(city="ChangSha", province="HuNam")
        company_address = protobuf_pb2.Address(city="ZhongSan", province="GuangDong")
        company = protobuf_pb2.EchoRequest.Company(name="zsc", address=company_address)
        any = protobuf_pb2.google_dot_protobuf_dot_any__pb2.Any()
        any.Pack(address)
        map = {
            "key1": "value1",
            "key2": "value2"
        }
        req = protobuf_pb2.EchoRequest(
            name="CaoChao",
            hobbies=["basketball", "football"],
            email="123456@qq.com",
            sex=protobuf_import_pb2.MAN,
            address=address,
            company=company,
            any=any,
            map=map,
        )

        response: protobuf_pb2.EchoResponse = stub.TestEcho(req)
        print("Greeter client received: " + str(response))

        # TestEmpty
        req = protobuf_pb2.google_dot_protobuf_dot_empty__pb2.Empty()
        response = stub.TestEmpty(req)
        print("Greeter client received: " + str(response))


if __name__ == "__main__":
    run()
