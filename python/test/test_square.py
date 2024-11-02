#to test the square function 
#to run the test > pytest test_square.
#if one statement fails then the ones below it are not even executed
#so we make different functions which will be all executed to some extent

from square import square
import pytest

def test_positive():
    assert square(2) == 4
    assert square(3) == 9
    assert square(4) == 16
    
def test_negative():
    assert square(-2) == 4
    
def test_zero():
    assert square(0) == 0
    
def test_str():
    with pytest.raises(TypeError):
        square("cat")