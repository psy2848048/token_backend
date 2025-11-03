from src.token import Token


token = Token("human fee sting vast car chicken spend distance feature injury toward there")


def get_balance(address: str): 
    value = token.balanceOf(address)
    return value


def transfer(to, value):
    tx_hash = token.transfer(to, value)
    return tx_hash
