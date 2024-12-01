from um import count
import pytest

def test_count():
    assert count('um, actually') == 1
    assert count("um?") == 1
    assert count("um... its easy the sum") == 1
    assert count("um um um") == 3
    