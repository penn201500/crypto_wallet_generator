import click
from crypto_wallet import generate_wallet, get_balance, generate_mnemonic
from crypto_wallet.utils import save_to_json_file


@click.group()
def cli():
    """Cryptowallet CLI"""
    pass


@cli.command()
@click.option('--address', required=True, help='The address to get the balance of')
def balance(address):
    """Get the balance of an address"""
    click.echo(get_balance(address))


@cli.command()
@click.option('--mnemonic', required=False, help='The mnemonic to create a new wallet')
@click.option('--prefix', default='wallet', help='The prefix for the JSON filename')
def create_wallet(mnemonic, prefix):
    """Create a new wallet from a mnemonic"""
    wallet_info = generate_wallet(mnemonic)
    if "error" in wallet_info:
        click.echo(wallet_info["error"])
    else:
        click.echo(f"Mnemonic: {wallet_info['mnemonic']}")
        click.echo(f"Address: {wallet_info['address']}")
        click.echo(f"Private Key: {wallet_info['private_key']}")
        save_to_json_file(wallet_info, prefix)


@cli.command(name='generate-mnemonic')
def create_mnemonic():
    """Generate a new mnemonic phrase"""
    click.echo(generate_mnemonic())


# TODO: Add tests for common used functions and files


if __name__ == '__main__':
    cli()
