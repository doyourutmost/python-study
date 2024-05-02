#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @time    : 2024/4/27 22:55
# @author  : CaoChao
# @file    : rpc_client.py

import requests


class Client:
    def __init__(self, url):
        self.url = url

    def add(self, a, b):
        rsp = requests.get(f"{self.url}/?a={a}&b={b}")
        return rsp.json().get("result", 0)


client = Client("http://localhost:8003/")
print(client.add(1, 2))
print(client.add(22, 33))
print(client.add(33, 44))
