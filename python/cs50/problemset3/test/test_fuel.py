from fuel import convert
import pytest 

def test_fuel():
    assert convert("4/4") == "F"
    assert convert("1/4") == "25.0%"
    assert convert("0/4") == "E"