import click
from crypto_wallet import generate_wallet, get_balance


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
def create_wallet(mnemonic):
    """Create a new wallet from a mnemonic"""
    wallet_info = generate_wallet(mnemonic)
    if "error" in wallet_info:
        click.echo(wallet_info["error"])
    else:
        click.echo(f"Mnemonic: {wallet_info['mnemonic']}")
        click.echo(f"Address: {wallet_info['address']}")
        click.echo(f"Private Key: {wallet_info['private_key']}")


if __name__ == '__main__':
    cli()
