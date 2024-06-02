from concurrent import futures

import collections
import logging
import random

import grpc

from rpc.grpc.retry.proto import retry_pb2_grpc, retry_pb2


class ErrorInjectingGreeter(retry_pb2_grpc.GreeterServicer):
    def __init__(self):
        self._counter = collections.defaultdict(int)

    def SayHello(
            self,
            request: retry_pb2.HelloRequest,
            context: grpc.ServicerContext,
    ) -> retry_pb2.HelloReply:
        self._counter[context.peer()] += 1
        if self._counter[context.peer()] < 5:
            if random.random() < 0.75:
                logging.info("Injecting error to RPC from %s", context.peer())
                context.abort(
                    grpc.StatusCode.UNAVAILABLE, "injected error"
                )
        logging.info("Successfully responding to RPC from %s", context.peer())
        return retry_pb2.HelloReply(message="Hello, %s!" % request.name)


def serve() -> None:
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    retry_pb2_grpc.add_GreeterServicer_to_server(
        ErrorInjectingGreeter(), server
    )
    listen_addr = "[::]:8051"
    server.add_insecure_port(listen_addr)
    logging.info("Starting flaky server on %s", listen_addr)
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    serve()
