import json
import re

import requests


def _main():
    f = open("accounts_to_see.txt","r")
    accounts=f.readlines()
    for account in accounts:
        print(account)

        url = f"https://api.cspr.live/accounts/{account.strip()}/deploys?page=1&limit=100"
        print(url)
        r = requests.get(url)
        # print(r.json())
        itemCount = r.json()["itemCount"]

        print(itemCount)
    



# Entry point.
if __name__ == "__main__":
    _main()

