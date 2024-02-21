import pycspr

def _main():
    """Main entry point.
    """
    print("-" * 74)
    print("PYCSPR :: Public Key to AccountHash")
    print("-" * 74)
    _TEST_ACCOUNT_KEY = \
    bytes.fromhex("01e91a79bff5627d48b0c1575eb984cea44323f806de65c2539da56616a20de3ba")
    public_key = pycspr.factory.create_public_key_from_account_key(_TEST_ACCOUNT_KEY)
    account_hash = public_key.account_hash.hex()
    print("account_hash", account_hash)
    
if __name__ == "__main__":
    _main()