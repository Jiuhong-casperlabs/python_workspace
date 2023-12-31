import argparse
import json

from pycspr import NodeClient
from pycspr import NodeConnection

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
    for height in range(2014081, 2140604):

        deploy_hashes = client.get_block(height)["body"]["deploy_hashes"]
        if len(deploy_hashes) > 0:
            # check deploy
            for deploy in deploy_hashes:
                # print(json.dumps(client.get_deploy(deploy)))
                deploy_result = client.get_deploy(deploy)
                try:
                    # find the redelegate entry point name
                    entrypoint_name = deploy_result["deploy"]["session"]["StoredContractByHash"]["entry_point"]
                    if entrypoint_name == "redelegate":
                        print(deploy_result["deploy"]["hash"])
                        print()
                except Exception as e:
                    print(e)


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


# block_height  era_id
# 2014081	    10554
# 2014080	    10553	=> 1.5.2 takes effect
# For this upgrade to protocol version , the activation point is Era 10553

# current 
# 2140604

