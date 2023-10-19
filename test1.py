import requests
import json

# node_endpoint = 'http://3.14.161.135:7777/rpc'
node_endpoint ="https://rpc.mainnet.casperlabs.io/rpc"

name_list = ["redelegate","delegate","undelegate"]

f = open("errordeploys.txt","r")

lines= f.readlines()

try:
    for line in lines:
        deploy_hash = line.split()[0]
        payload = {
        "id": 1,
        "jsonrpc": "2.0",
        "method": "info_get_deploy",
        "params": [
            deploy_hash
            ]
        }

        print(deploy_hash)
        # print(payload)
        r = requests.post(node_endpoint, json=payload)
        # print(r.text)
        deploy_result = json.loads(r.text)["result"]
        
        try:

            success = deploy_result["execution_results"][0]["result"]["Success"]

            entrypoint_name = deploy_result["deploy"]["session"]["StoredContractByHash"]["entry_point"]
            if entrypoint_name in name_list:
                print(json.dumps(deploy_result["deploy"]["session"],indent=4))
                print()
        except Exception as e:
            print(e)

except Exception as e:
    print(e)