from plates import is_valid
import pytest

def test_valid():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False 