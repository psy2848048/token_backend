from web3 import Web3
from web3.contract import Contract
from eth_account.signers import local
from . import const


ETHEREUM_RPC = "https://0xrpc.io/sep"
CHAIN_ID = 11155111

class Token:
    __web3: Web3
    __mnemonics: str
    __account: local.LocalAccount
    __contract: Contract

    def __init__(self, _mnemonics: str):
        self.__web3 = Web3(Web3.HTTPProvider(ETHEREUM_RPC))
        self.__web3.eth.account.enable_unaudited_hdwallet_features()

        self.__mnemonics = _mnemonics
        self.__account = self.__web3.eth.account.from_mnemonic(self.__mnemonics, account_path="m/44'/60'/0'/0/0")
        self.__contract = self.__web3.eth.contract(address=const.TOKEN_ADDRESS, abi=const.TOKEN_ABI)

    def address(self) -> str:
        return self.__account.address

    def balanceOf(self, address) -> int:
        return self.__contract.functions.balanceOf(address).call()
    
    def balanceOfMe(self) -> int:
        return self.balanceOf(self.__account.address)
    
    def transfer(self, to_address, value) -> str:
        nonce = self.__web3.eth.get_transaction_count(self.__account.address)
        tx = self.__contract.functions.transferFrom(self.__account.address, to_address, value).\
            build_transaction({
                'chainId': self.__web3.eth.chain_id,
                'gasPrice': self.__web3.eth.gas_price,
                'nonce': nonce,
            })

        rawTx = self.__account.sign_transaction(tx)
        tx_hash = self.__web3.eth.send_raw_transaction(rawTx.raw_transaction)
        print(f"tx sent as {tx_hash}, waiting for confirmation...")

        receipt = self.__web3.eth.wait_for_transaction_receipt(tx_hash, timeout=180)
        return receipt
