# Copyright 2021 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python AsyncIO implementation of the GRPC hellostreamingworld.MultiGreeter server."""

import asyncio
import logging

import grpc
from rpc.grpc.hellostreamingworld.proto import helloworld_pb2_grpc, helloworld_pb2

NUMBER_OF_REPLY = 10


class Greeter(helloworld_pb2_grpc.MultiGreeterServicer):
    async def sayHello(
            self, request: helloworld_pb2.HelloRequest, context: grpc.aio.ServicerContext
    ) -> helloworld_pb2.HelloReply:
        logging.info("Serving sayHello request %s", request)
        for i in range(NUMBER_OF_REPLY):
            yield helloworld_pb2.HelloReply(message=f"Hello number {i}, {request.name}!")


async def serve() -> None:
    server = grpc.aio.server()
    helloworld_pb2_grpc.add_MultiGreeterServicer_to_server(Greeter(), server)
    listen_addr = "[::]:50051"
    server.add_insecure_port(listen_addr)
    logging.info("Starting server on %s", listen_addr)
    await server.start()
    await server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(serve())
