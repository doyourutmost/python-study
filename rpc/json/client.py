#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @time    : 2024/5/2 10:49
# @author  : CaoChao
# @file    : client.py
import jsonrpclib

server = jsonrpclib.ServerProxy('http://localhost:8000')
print(server.add(5, 6))
print(server.pow(5, 6))
print(server.ping('hello world~'))
