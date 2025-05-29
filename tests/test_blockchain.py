import pytest
from src.blockchain_verification import connect_to_ethereum

def test_ethereum_connection():
    w3 = connect_to_ethereum()
    assert w3.is_connected()  # Note: Requires a valid Infura key to pass
