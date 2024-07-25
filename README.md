# Crypto Wallet CLI

Crypto Wallet CLI is a command-line tool for generating and managing Binance Smart Chain (BSC) wallets. It allows you to create new wallets from a mnemonic phrase, retrieve the balance of a given address, and more.

## Features

- Generate a BSC wallet from a mnemonic or create a new one
- Retrieve the balance of a given BSC address
- Save wallet details (mnemonic, address, private key) to a JSON file with a timestamped filename

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
   pip install -e .
   ```

## Usage

### Generate a Wallet

To create a new wallet, run:

```bash
cw c
```

To create a wallet from an existing mnemonic, run:

```bash
cw c -m "your twelve word mnemonic here"
```

To specify a custom filename prefix for saving the wallet details, run:

```bash
cw c -m "your twelve word mnemonic here" -p mywallet
```

### Get Balance

To get the balance of a BSC address, run:

```bash
cw b -a 0xYourBSCAddress
```

### Generate Mnemonic

To generate a new mnemonic phrase, run:

```bash
cw m
```

## Options

```bash
c, –create-wallet: Create a new wallet from a mnemonic and save to a file.
m, –generate-mnemonic: Generate a new mnemonic phrase.
b, –balance: Get the balance of an address.
-m, --mnemonic [value]: The mnemonic to create a new wallet.
-p, --prefix [value]: The prefix for the JSON filename.
-a, --address [value]: The address to get the balance of.
```

## Running Tests

To run the tests for the utility functions, use the following command:

```bash
python -m unittest discover -s tests -v
```

## Acknowledgments

This project is inspired by [yerofey/cryptowallet-cli](https://github.com/yerofey/cryptowallet-cli). If you need a JavaScript version, please check out their project.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
