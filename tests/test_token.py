def test_token_balanceOf(tokenClass):
    print(tokenClass.balanceOfMe())
    assert tokenClass.balanceOfMe() > 0

def test_token_transfer(tokenClass):
    transfer_value = int(10 ** 18 / 10)
    assert tokenClass.balanceOfMe() > transfer_value

    before_balance = tokenClass.balanceOf("0xb9F872e5ba2b7fE26200e6811Dc2E69FB7fbB006")
    print("before_balance: ", before_balance)
    assert tokenClass.transfer("0xb9F872e5ba2b7fE26200e6811Dc2E69FB7fbB006", transfer_value) != ""
    after_balance = tokenClass.balanceOf("0xb9F872e5ba2b7fE26200e6811Dc2E69FB7fbB006")

    assert after_balance - before_balance == transfer_value