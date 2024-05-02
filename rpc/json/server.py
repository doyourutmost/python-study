#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @time    : 2024/5/2 10:49
# @author  : CaoChao
# @file    : server.py
from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer

server = SimpleJSONRPCServer(('localhost', 8000))
server.register_function(pow)
server.register_function(lambda x, y: x + y, 'add')
server.register_function(lambda x: x, 'ping')
server.serve_forever()
