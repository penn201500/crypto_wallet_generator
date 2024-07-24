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


@cli.command()
@click.option('--address', required=True, help='The address to get the balance of')
def balance(address):
    """Get the balance of an address"""
    click.echo(get_balance(address))


@cli.command(name='create-wallet')
@click.option('--mnemonic', required=False, help='The mnemonic to create a new wallet')
@click.option('--prefix', default='wallet', help='The prefix for the JSON filename')
def create_wallet(mnemonic, prefix):
    """Create a new wallet from a mnemonic and save to a file"""
    wallet_info = generate_wallet(mnemonic)
    if "error" in wallet_info:
        click.echo(colored(wallet_info["error"], "red"))
    else:
        click.echo(colored("✨ Done! Here is your brand new ERC-like wallet:", "green"))
        click.echo()
        click.echo(colored(wallet_info['mnemonic'], "white"))
        click.echo(colored(wallet_info['address'], "cyan"))
        click.echo(colored(wallet_info['private_key'], "yellow"))
        click.echo()
        click.echo(
            colored("💼 You can use this wallet in Ethereum, Binance Smart Chain, Polygon and more networks (EVM compatible)", "yellow"))
        click.echo(
            colored("ℹ️ You can import this wallet into MetaMask, Trust Wallet, Binance Chain Wallet and many other wallet apps", "green"))
        save_to_json_file(wallet_info, prefix)


@cli.command(name='generate-mnemonic')
def generate_mnemonic_cmd():
    """Generate a new mnemonic phrase"""
    click.echo(generate_mnemonic())


# TODO: Add tests for common used functions and files


if __name__ == '__main__':
    cli()
