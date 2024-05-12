from concurrent import futures
import asyncio
import logging

import grpc

from rpc.grpc.stream.proto.stream_pb2_grpc import MultiGreeterServicer, add_MultiGreeterServicer_to_server
from rpc.grpc.stream.proto.stream_pb2 import HelloRequest, HelloReply

NUMBER_OF_REPLY = 10


class Greeter(MultiGreeterServicer):
    def sayHello(
            self, request: HelloRequest, context: grpc.aio.ServicerContext
    ) -> HelloReply:
        logging.info("Serving sayHello request %s", request)
        number_of_reply = request.num_greetings
        if number_of_reply <= 0:
            number_of_reply = NUMBER_OF_REPLY
        for i in range(number_of_reply):
            yield HelloReply(message=f"Hello number {i}, {request.name}!")
        # 返回响应介绍信息
        yield HelloReply(message=f"{request.name},响应结束!")


def serve() -> None:
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_MultiGreeterServicer_to_server(Greeter(), server)
    listen_addr = "[::]:8051"
    server.add_insecure_port(listen_addr)
    logging.info("Starting server on %s", listen_addr)
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    serve()
