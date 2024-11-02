import pytest
from bank import value

def test_banks():
    assert value("hello") == 0
    assert value("bye") == 100
    assert value("hey") == 20