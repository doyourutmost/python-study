#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @time    : 2024/5/2 11:33
# @author  : CaoChao
# @file    : server.py
import zerorpc


class HelloRPC(object):
    def hello(self, name):
        return "Hello, %s" % name


s = zerorpc.Server(HelloRPC())
s.bind("tcp://0.0.0.0:4242")
s.run()
