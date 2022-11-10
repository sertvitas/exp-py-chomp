import one
import pytest

@pytest.mark.experimental
def test_always_passes():
    assert True
def test_always_fails():
    assert False

def test_one():
#    ugh = one.blah()
    assert one.blah() == 'Mondays, amirite?'

def test_calc_addition():
    output = one.calc_addition(2,4)
    assert output == 6

def test_calc_substraction():
    output = one.calc_substraction(2, 4)
    assert output == -2

def test_calc_multiply():
    output = one.calc_multiply(2,4)
    assert output == 8