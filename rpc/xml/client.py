#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @time    : 2024/5/2 10:11
# @author  : CaoChao
# @file    : client.py
from xmlrpc import client

server = client.ServerProxy("http://localhost:8088")
print(server.add(2, 3))
print(server.multiply(2, 3))
print(server.subtract(2, 3))
print(server.divide(2, 3))
