import argparse
import json
from time import sleep
import requests
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

    account = "01b87e2765aa53c6c92aae6853bea9f434c905de0fbc4097058770620eced644ef"
    url = f"https://api.cspr.live/accounts/{account}/deploys?page=1&limit=300"
    r = requests.get(url)

    pages = r.json()["pages"]
    # print(pages)
    deploy_hashes=[]
    for page in pages:
        url = f'https://api.cspr.live{page["url"].replace("limit=10", "limit=900")}'
        r = requests.get(url)
        for cell in r.json()["data"]:
            deploy_hashes.append(cell["deployHash"])

    print("account",account)
    [print(deploy_hash) for deploy_hash in deploy_hashes]
    print(len(deploy_hashes))

    name_list = ["redelegate","delegate","undelegate"]
    # check deploy
    for deploy in deploy_hashes:
        # print(json.dumps(client.get_deploy(deploy)))
        
        try:
            deploy_result = client.get_deploy(deploy)
            if not deploy_result["execution_results"][0]["result"]["Success"]:
                continue
            # find the redelegate entry point name
            entrypoint_name = deploy_result["deploy"]["session"]["StoredContractByHash"]["entry_point"]
            if entrypoint_name in name_list:
                print(deploy)
                print(json.dumps(deploy_result["deploy"]["session"],indent=4))
                print()
        except Exception as e:
            print(deploy,e)


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

