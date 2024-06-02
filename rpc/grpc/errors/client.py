import logging

from google.rpc import error_details_pb2
import grpc
from grpc_status import rpc_status

from rpc.grpc.errors.proto import helloworld_pb2_grpc, helloworld_pb2


def process(stub):
    try:
        response = stub.SayHello(helloworld_pb2.HelloRequest(name="Alice2"))
        print("Call success: %s" % response.message)
    except grpc.RpcError as rpc_error:
        print("Call failure: %s", rpc_error)
        print("RPC code: %s" % rpc_error.code())
        print("RPC details: %s" % rpc_error.details())
        status = rpc_status.from_call(rpc_error)

        for detail in status.details:
            if detail.Is(error_details_pb2.QuotaFailure.DESCRIPTOR):
                info = error_details_pb2.QuotaFailure()
                detail.Unpack(info)
                print("Quota failure: %s", info)
            else:
                raise RuntimeError("Unexpected failure: %s" % detail)


def main():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel("localhost:8051") as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        process(stub)


if __name__ == "__main__":
    logging.basicConfig()
    main()
