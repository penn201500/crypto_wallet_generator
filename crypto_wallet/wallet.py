from web3 import Web3
from tronpy import Tron  # ref doc: https://tronpy.readthedocs.io/
from tronpy.providers import HTTPProvider
from mnemonic import Mnemonic
from eth_account import Account as EthAccount
from tronpy.keys import PrivateKey as TronPrivateKey
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Connect to BSC node
# bsc_provider_testnet = 'https://data-seed-prebsc-1-s1.binance.org:8545/'  # Testnet
# w3 = Web3(Web3.HTTPProvider(bsc_provider_testnet))
# Ethereum/BSC configuration
INFURA_URL = os.getenv('INFURA_URL')
web3 = Web3(Web3.HTTPProvider(INFURA_URL))
# Enable mnemonic features
EthAccount.enable_unaudited_hdwallet_features()

# Tron configuration
# get trongrid API key, ref:https://www.trongrid.io/price
TRON_API_KEY = os.getenv('TRON_API_KEY')
tron = Tron(HTTPProvider(api_key=TRON_API_KEY))


def generate_eth_wallet(mnemonic=None):
    if not mnemonic:
        mnemo = Mnemonic("english")
        mnemonic = mnemo.generate(strength=128)  # 12 words

    acct = EthAccount.from_mnemonic(mnemonic)
    return {
        'mnemonic': mnemonic,
        'address': acct.address,
        'private_key': acct.key.hex()
    }


def generate_tron_wallet(mnemonic=None):
    if not mnemonic:
        mnemo = Mnemonic("english")
        mnemonic = mnemo.generate(strength=128)

    # Generate a Tron private key from a mnemonic
    eth_account = EthAccount.from_mnemonic(mnemonic)
    private_key = TronPrivateKey(bytes.fromhex(eth_account.key.hex()[2:]))
    address = private_key.public_key.to_base58check_address()

    return {
        'mnemonic': mnemonic,
        'address': address,
        'private_key': private_key.hex()
    }


def generate_wallet(chain, mnemonic=None):
    if chain == "ethereum" or chain == "bsc":
        return generate_eth_wallet(mnemonic)
    elif chain == "tron":
        return generate_tron_wallet(mnemonic)
    else:
        raise ValueError("Unsupported blockchain type")


def generate_mnemonic(strength=128):
    """Generate a new mnemonic phrase"""
    mnemo = Mnemonic("english")
    return mnemo.generate(strength=strength)


def get_eth_balance(address):
    balance_wei = web3.eth.get_balance(address)
    balance_eth = web3.from_wei(balance_wei, 'ether')
    return balance_eth


def get_tron_balance(address):
    balance_trx = tron.get_account_balance(address)
    return balance_trx


def get_balance(address, chain):
    if chain == "ethereum" or chain == "bsc":
        return get_eth_balance(address)
    elif chain == "tron":
        return get_tron_balance(address)
    else:
        raise ValueError("Unsupported blockchain type")
