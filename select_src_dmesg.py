import requests

src_list = {}
my_list=[]
peer_addresses=[]

def get_src_list():

    with open("dmesg.txt","r") as f:
        lines = f.readlines()

    for line in lines:
        x=line.split()

        for field in x:
            if field.startswith("SRC"):
                try:
                    src_list[field] +=1
                except KeyError:
                    src_list[field] = 1

    [my_list.append(src[4:]) for src in sorted(src_list.keys())]


def get_node_addresses():
    try:
        payload = {
            "id": 1,
            "jsonrpc": "2.0",
            "method": "info_get_status",
            "params": []
        }

        rpc_result = requests.post('https://rpc.testnet.casperlabs.io/rpc', json=payload)
        peers = rpc_result.json()["result"]["peers"]

        [peer_addresses.append(peer["address"].split(":")[0]) for peer in peers]
        
    except Exception as err:
        # print(peer, err)
        pass

get_node_addresses()
print("peer_addresses",peer_addresses)
print()
get_src_list()
print()
print("my_list",my_list)

print("src in peer_addresses?")

[print(src,"yes") if src in peer_addresses else print(src,"not in peers") for src in my_list]

