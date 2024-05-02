#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @time    : 2024/4/27 22:52
# @author  : CaoChao
# @file    : client.py
import requests

# 通过http协议调用rpc服务
# 1、每个函数调用我们都需要记住 url 地址，参数是如何传递的，返回值是如何解析的
rsp = requests.get(f"http://127.0.0.1:8003/?a=1&b=2")
print(rsp.text)


