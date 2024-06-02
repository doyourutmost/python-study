import json
import logging

import grpc

from rpc.grpc.retry.proto import retry_pb2_grpc, retry_pb2


def run():
    # The ServiceConfig proto definition can be found:
    # https://github.com/grpc/grpc-proto/blob/ec886024c2f7b7f597ba89d5b7d60c3f94627b17/grpc/service_config/service_config.proto#L377
    service_config_json = json.dumps(
        {
            "methodConfig": [
                {
                    # To apply retry to all methods, put [{}] in the "name" field
                    "name": [
                        {"service": "Greeter", "method": "SayHello"}
                    ],
                    "retryPolicy": {
                        "maxAttempts": 5,
                        "initialBackoff": "0.1s",
                        "maxBackoff": "1s",
                        "backoffMultiplier": 2,
                        "retryableStatusCodes": ["UNAVAILABLE"],
                    },
                }
            ]
        }
    )
    options = []
    # NOTE: the retry feature will be enabled by default >=v1.40.0
    options.append(("grpc.enable_retries", 1))
    options.append(("grpc.service_config", service_config_json))
    with grpc.insecure_channel("localhost:8051", options=options) as channel:
        stub = retry_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(retry_pb2.HelloRequest(name="you"))
    print("Greeter client received: " + response.message)


if __name__ == "__main__":
    logging.basicConfig()
    run()
