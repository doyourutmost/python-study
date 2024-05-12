#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @time    : 2024/5/2 20:09
# @author  : CaoChao
# @file    : client.py
import json
import socket
import itertools


class JSONClient(object):

    def __init__(self, addr):
        self.socket = socket.create_connection(addr)
        self.id_counter = itertools.count()

    def __del__(self):
        self.socket.close()

    def call(self, name, *params):
        request = dict(id=next(self.id_counter),
                       params=list(params),
                       method=name)
        self.socket.sendall(json.dumps(request).encode())

        # This must loop if resp is bigger than 4K
        response = self.socket.recv(4096)
        response = json.loads(response.decode())

        if response.get('id') != request.get('id'):
            raise Exception("expected id=%s, received id=%s: %s"
                            % (request.get('id'), response.get('id'),
                               response.get('error')))

        if response.get('error') is not None:
            raise Exception(response.get('error'))

        return response.get('result')


def close(self):
    self._socket.close()


if __name__ == '__main__':
    rpc = JSONClient(("localhost", 1234))
    print(rpc.call("HelloService.Hello", "hello1"))
    print(rpc.call("HelloService.Hello", "hello2"))
    print(rpc.call("HelloService.Hello", "hello3"))
