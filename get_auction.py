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
    # for height in range(2014081, 2140604):

# ============= get deploy info
    f = open("result1.json", "r")
    for deploy_hash in f:
        deploy_result = client.get_deploy(deploy_hash) # deployhash is from input file
        # print(json.dumps(deploy_result))
        # return
        
        try:
            deploy_result["execution_results"][0]["result"]["Success"]
        except:
            print("failed deploy:",deploy_hash)
            continue

        block_hash = deploy_result["execution_results"][0]["block_hash"]
        # parm_delegator = 
        args = deploy_result["deploy"]["session"]["StoredContractByHash"]["args"]

        for arg in args:
            if arg[0] == "delegator":
                arg_delegator = arg[1]["parsed"]

            if arg[0] == "validator":
                arg_old_validator = arg[1]["parsed"]

            if arg[0] == "amount":
                arg_amount = arg[1]["parsed"]

            if arg[0] == "new_validator":
                arg_new_validator = arg[1]["parsed"]

    # ==============get block info ========
        block_result = client.get_block(block_hash)
        # print(json.dumps(block_result))
        # return

        before_era_id = block_result["header"]["era_id"]
        before_height = block_result["header"]["height"]

        temp_after_height = before_height + 200 * 7

        if temp_after_height > 2141045:
            continue
        temp_block_result = client.get_block(temp_after_height)
        temp_after_era_id = temp_block_result["header"]["era_id"]

        while (temp_after_era_id - before_era_id !=8):
            temp_after_height = temp_after_height + 200 
            if temp_after_height > 2141045:
               print("hello")
               return
            temp_block_result = client.get_block(temp_after_height)
            temp_after_era_id = temp_block_result["header"]["era_id"]

        after_era_id = temp_after_era_id
        after_height = temp_after_height

            
        print("========================")
        print("Process deploy_hash:\n",deploy_hash)
        before_bids = my_get_auction_info(client,before_height,arg_new_validator)
        old_staked_amount = 0
        for bid_cell in before_bids:
                    if bid_cell["public_key"] == arg_new_validator:
                        old_delegators = bid_cell["bid"]["delegators"]
                        for pk in old_delegators:
                            if pk == arg_delegator:
                               
                               old_staked_amount =  pk["staked_amount"]

        after_bids = my_get_auction_info(client,after_height,arg_new_validator)
        count = 0
        for bid_cell in after_bids:
                    if bid_cell["public_key"] == arg_new_validator:
                        delegators = bid_cell["bid"]["delegators"]
                        print("arg_delegator",arg_delegator)
                        for pk in delegators:
                            if pk["public_key"] == arg_delegator:
                                #  new_staked_amount: staked_amount after 7 eras
                               new_staked_amount =  pk["staked_amount"]
                               #  delta staked_amount between new and old era
                               delta_staked_amount = int(new_staked_amount) - old_staked_amount
                               # get amount_from_deploy from deploy
                               if delta_staked_amount > int(arg_amount):
                                  count += 1
                                  # that should be okay.
                                  print("TO SEE:", deploy_hash)
                                  print("delta_staked_amount",delta_staked_amount)
                                  print("arg_amount",arg_amount)
                                #   if old era the staked amount is 0 then equal is okay.
                               elif old_staked_amount == 0 and delta_staked_amount == int(arg_amount):
                                  count += 1
                                  print("good:", deploy_hash)
                                  print("delta_staked_amount",delta_staked_amount)
                                  print("arg_amount",arg_amount)

                               else:
                                # Otherwise the redelegated amount is not good.
                                # print deploy hash, block height before and after
                                  print("bad:",deploy_hash)
                                  print("delta_staked_amount",delta_staked_amount)
                                  print("arg_amount",arg_amount)
        if count == 0:
            print("bad:", deploy_hash)

        print("========================")

           
    # ============== get auction info
def my_get_auction_info(client, block_height,new_validator):
    auction_result = client.get_auction_info(block_height)
    bids = auction_result["auction_state"]["bids"]

    return bids
            

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

