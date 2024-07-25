from setuptools import setup, find_packages

setup(
    name='crypto-wallet-cli',
    version='0.2',
    packages=find_packages(),
    install_requires=[
        'click',
        'web3',
        'mnemonic',
        'termcolor',
        'tronpy',
        'python-dotenv'
    ],
    entry_points={
        'console_scripts': [
            'cw=main:cli',
        ],
    },
)