import requests
import json

# deploy_hash = "3b4064812e3956d0792da81c961f8e6cd4c38efe169478cc7edaff8f4927ca1a"
# node_endpoint = 'http://3.14.161.135:7777/rpc'
node_endpoint ="https://rpc.mainnet.casperlabs.io/rpc"

name_list = ["redelegate","delegate","undelegate"]


try:
    account = "01eb04224095b98f40a7bbc41a1e19a7c11b0281100f46650cc500816cf2fbca36"
    make_url = f"https://api.cspr.live/accounts/{account}/deploys?page=1&limit=300"
    r = requests.get(make_url)

    pages = r.json()["pages"]

    deploy_hashes=[]
    for page in pages:
        make_url = f'https://api.cspr.live{page["url"].replace("limit=10", "limit=900")}'
        r = requests.get(make_url)
        for cell in r.json()["data"]:
            deploy_hashes.append(cell["deployHash"])

    for deploy_hash in deploy_hashes:
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
                print(deploy_hash)
                print(json.dumps(deploy_result["deploy"]["session"],indent=4))
                print()
        except Exception as e:
            print(e)

except Exception as e:
    print(e)