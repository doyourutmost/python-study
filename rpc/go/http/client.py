#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @time    : 2024/5/2 20:31
# @author  : CaoChao
# @file    : client.py
import requests

req = {"method": "HelloService.Hello", "params": ['python'], 'id': 0}
rsp = requests.post("http://localhost:1234/json-rpc", json=req)
print(rsp.text)
