#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @time    : 2024/5/2 10:10
# @author  : CaoChao
# @file    : server.py
from xmlrpc.server import SimpleXMLRPCServer


class Calculate:
    def add(self, x, y):
        return x + y

    def multiply(self, x, y):
        return x * y

    def subtract(self, x, y):
        return x - y

    def divide(self, x, y):
        return x / y


obj = Calculate()
server = SimpleXMLRPCServer(("localhost", 8088))
# 将实例注册给rpc server
server.register_instance(obj)
print("Listening on port 8088")
server.serve_forever()
