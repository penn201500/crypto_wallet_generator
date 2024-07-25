import click
from crypto_wallet import generate_wallet, get_balance, generate_mnemonic
from crypto_wallet.utils import save_to_json_file
from termcolor import colored


@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    """Cryptowallet CLI"""
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())


@click.command()
@click.option('-a', '--address', required=True, help='The address to get the balance of')
@click.option('-c', '--chain', required=True, type=click.Choice(['ethereum', 'bsc', 'tron'], case_sensitive=False),
              help='The blockchain to get the balance from (ethereum, bsc, tron)')
def balance(address, chain):
    """Get the balance of an address"""
    balance_value = get_balance(address, chain)
    click.echo(f"The balance of the address {address} on {chain} is {balance_value}.")


def display_wallet_info(wallet_info, index=None, chain="ethereum"):
    if index is not None:
        click.echo(colored(f"Wallet {index + 1}:", "green"))
    click.echo()
    click.echo(colored(wallet_info['mnemonic'], "white"))
    click.echo(colored(wallet_info['address'], "cyan"))
    click.echo(colored(wallet_info['private_key'], "yellow"))
    click.echo()
    if chain == "tron":
        click.echo(colored("💼 You can use this wallet in Tron", "yellow"))
        click.echo(colored("ℹ️ You can import this wallet into TronLink and many other Tron wallet apps", "green"))
    else:
        click.echo(
            colored("💼 You can use this wallet in Ethereum, Binance Smart Chain, Polygon and more networks (EVM compatible)", "yellow"))
        click.echo(
            colored("ℹ️ You can import this wallet into MetaMask, Trust Wallet, Binance Chain Wallet and many other wallet apps", "green"))


def create_multiple_wallets(number, prefix, chain):
    wallets_info = []
    for i in range(number):
        wallet_info = generate_wallet(chain, None)
        wallets_info.append(wallet_info)
        display_wallet_info(wallet_info, index=i, chain=chain)
    save_to_json_file(wallets_info, prefix)


def create_single_wallet(mnemonic, prefix, chain):
    wallet_info = generate_wallet(chain, mnemonic)
    if "error" in wallet_info:
        click.echo(colored(wallet_info["error"], "red"))
    else:
        display_wallet_info(wallet_info, chain=chain)
        save_to_json_file(wallet_info, prefix)


@click.command()
@click.option('-m', '--mnemonic', required=False, help='The mnemonic to create a new wallet')
@click.option('-p', '--prefix', default='wallet', help='The prefix for the JSON filename')
@click.option('-n', '--number', type=int, help='Number of wallets to create')
@click.option('-c', '--chain', default='ethereum', type=click.Choice(['ethereum', 'bsc', 'tron'], case_sensitive=False),
              help='Specify the blockchain (ethereum, bsc, tron)')
def create_wallet(mnemonic, prefix, number, chain):
    """Create a new wallet from a mnemonic and save to a file"""
    if number:
        create_multiple_wallets(number, prefix, chain)
    else:
        create_single_wallet(mnemonic, prefix, chain)


@click.command()
def generate_mnemonic_cmd():
    """Generate a new mnemonic phrase"""
    click.echo(generate_mnemonic())


cli.add_command(balance, "b")
cli.add_command(create_wallet, "c")
cli.add_command(generate_mnemonic_cmd, "m")

# TODO: Add tests for common used functions and files

if __name__ == '__main__':
    cli()
