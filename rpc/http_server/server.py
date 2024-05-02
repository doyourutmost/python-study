#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @time    : 2024/4/27 22:44
# @author  : CaoChao
# @file    : server.py
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qsl
import json

host = ('', 8003)


def add(a, b):
    return a + b


class TodoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse(self.path)
        qs = dict(parse_qsl(parsed_url.query))
        a = int(qs.get("a", 0))
        b = int(qs.get("b", 0))
        self.send_response(200)
        self.send_header('Content-type', "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(
            {
                "result": add(a, b)
            }
        ).encode("utf-8"))


if __name__ == '__main__':
    server = HTTPServer(host, TodoHandler)
    print("Starting server, listen at: %s:%s" % host)
    server.serve_forever()
