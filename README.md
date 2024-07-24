# Crypto Wallet CLI

Crypto Wallet CLI is a command-line tool for generating and managing Binance Smart Chain (BSC) wallets. It allows you to create new wallets from a mnemonic phrase, retrieve the balance of a given address, and more.

## Features

- Generate a BSC wallet from a mnemonic or create a new one
- Retrieve the balance of a given BSC address

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/penn201500/crypto_wallet_generator
   cd crypto-wallet-cli
   ```
2. Create a conda environment and install dependencies:

   ```bash
   conda create -n cryptowallet-cli python=3.12
   conda activate cryptowallet-cli
   pip install -r requirements.txt
   ```

## Usage

### Generate a Wallet

To create a new wallet, run:

```bash
python main.py create-wallet
```

To create a wallet from an existing mnemonic, run:

```bash
python main.py create-wallet --mnemonic "your twelve word mnemonic here"
```

### Get Balance

To get the balance of a BSC address, run:

```bash
python main.py balance --address 0xYourBSCAddress
```

## Acknowledgments

This project is inspired by [yerofey/cryptowallet-cli](https://github.com/yerofey/cryptowallet-cli). If you need a JavaScript version, please check out their project.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
