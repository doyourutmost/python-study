#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @time    : 2024/5/2 11:33
# @author  : CaoChao
# @file    : client.py
import zerorpc

c = zerorpc.Client()
c.connect("tcp://127.0.0.1:4242")

for item in c.streaming_range(10, 20, 2):
    print(item)
