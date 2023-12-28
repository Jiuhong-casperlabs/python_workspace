import argparse
import json

from pycspr import NodeClient
from pycspr import NodeConnection

file1 = open("myfile.json", "a")

# CLI argument parser.
_ARGS = argparse.ArgumentParser("Demo illustrating how to execute native transfers with pycspr.")

# CLI argument: host address of target node - defaults to NCTL node 1.
_ARGS.add_argument(
    "--node-host",
    default="localhost",
    dest="node_host",
    help="Host address of target node.",
    type=str,
    )

# CLI argument: Node API REST port - defaults to 14101 @ NCTL node 1.
_ARGS.add_argument(
    "--node-port-rest",
    default=8888,
    dest="node_port_rest",
    help="Node API REST port.  Typically 8888 on most nodes.",
    type=int,
    )

# CLI argument: Node API JSON-RPC port - defaults to 11101 @ NCTL node 1.
_ARGS.add_argument(
    "--node-port-rpc",
    default=7777,
    dest="node_port_rpc",
    help="Node API JSON-RPC port.  Typically 7777 on most nodes.",
    type=int,
    )

# CLI argument: Node API SSE port - defaults to 18101 @ NCTL node 1.
_ARGS.add_argument(
    "--node-port-sse",
    default=9999,
    dest="node_port_sse",
    help="Node API SSE port.  Typically 9999 on most nodes.",
    type=int,
    )


def _main(args: argparse.Namespace):
    """Main entry point.

    :param args: Parsed command line arguments.

    """
    # Set client.
    client = _get_client(args)


    # Query 3.2: get_block - by height.
    for height in range(703453, 2299618):

        deploy_hashes = client.get_block(height)["body"]["deploy_hashes"]
        if len(deploy_hashes) > 0:
            # check deploy
            for deploy in deploy_hashes:
                # print(json.dumps(client.get_deploy(deploy)))
                deploy_result = client.get_deploy(deploy)
                # print(deploy_result)

                try:
                    # find the redelegate entry point name
                    if deploy_result["deploy"]["approvals"][0]["signer"] != "015d4d230841ae93139f23124597468f4e9d7f7f68479f5394ccd0079814661504":
                        break
                    deploy_result["execution_results"][0]["result"]["Success"]
                    args= deploy_result["deploy"]["session"]["ModuleBytes"]["args"]
                    hash = deploy_result["deploy"]["hash"]
                    
    
                    # args = deploy_result["deploy"]["session"]["ModuleBytes"]["args"]
                    file1.write("\n")
                    file1.write(hash)
                    file1.write(json.dumps(args))
                    print(hash)
                    print(json.dumps(args))
                except Exception as e:
                    print("error",e)


#    "low": 1898405,
#     "high": 2140607

def _get_client(args: argparse.Namespace) -> NodeClient:
    """Returns a pycspr client instance.

    """
    return NodeClient(NodeConnection(
        host=args.node_host,
        port_rest=args.node_port_rest,
        port_rpc=args.node_port_rpc,
        port_sse=args.node_port_sse
    ))


# Entry point.
if __name__ == "__main__":
    _main(_ARGS.parse_args())



