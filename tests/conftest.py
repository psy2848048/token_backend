import pytest
from src.token import Token


@pytest.fixture
def tokenClass():
    # test mnemonic: do not use in production
    return Token("human fee sting vast car chicken spend distance feature injury toward there")
