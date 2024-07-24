from web3 import Web3
from mnemonic import Mnemonic
from eth_account import Account

# Connect to BSC node
bsc_provider_testnet = 'https://data-seed-prebsc-1-s1.binance.org:8545/'  # Testnet
w3 = Web3(Web3.HTTPProvider(bsc_provider_testnet))

# Enable mnemonic features
Account.enable_unaudited_hdwallet_features()


def generate_wallet(mnemonic_phrase=None):
    """Create a new wallet from a mnemonic or generate a new one"""
    if mnemonic_phrase is None:
        mnemo = Mnemonic("english")
        mnemonic_phrase = mnemo.generate(strength=128)
    else:
        mnemo = Mnemonic("english")
        if not mnemo.check(mnemonic_phrase):
            return {"error": "Invalid mnemonic phrase"}

    # Generate private key from mnemonic
    acct = Account.from_mnemonic(mnemonic_phrase)
    private_key = acct._private_key.hex()
    address = acct.address

    return {
        "mnemonic": mnemonic_phrase,
        "address": address,
        "private_key": private_key
    }


def get_balance(address):
    """Get the balance of an address in BNB"""
    balance_wei = w3.eth.get_balance(address)
    balance_bnb = w3.from_wei(balance_wei, 'ether')
    return balance_bnb
