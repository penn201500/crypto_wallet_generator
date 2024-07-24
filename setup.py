from setuptools import setup, find_packages

setup(
    name='crypto-wallet-cli',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'click',
        'web3',
        'mnemonic',
        'termcolor',
    ],
    entry_points={
        'console_scripts': [
            'cw=main:cli',
        ],
    },
)