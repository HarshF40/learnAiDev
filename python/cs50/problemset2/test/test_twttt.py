import pytest
from twttt import shorten

def test_short_sentence():
    assert shorten("Hello my friend!") == "Hll my frnd!"
    
def test_long_sentence():
    assert shorten("~/learnAiDev/python/cs50/problemset2") == "~/lrnDv/pythn/cs50/prblmst2"
    assert shorten("Green smilies mean your program has passed a test!") == "Grn smls mn yr prgrm hs pssd  tst!"