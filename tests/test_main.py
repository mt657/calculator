'''My Calculator Test'''
import pytest
from app.main import addition, divison, multiplication, subtraction

def test_addition():
    '''Addition function'''
    assert addition(1,1) == 2

def test_subtraction():
    '''Subtraction function'''
    assert subtraction(1,1) == 0


def test_multiplication():
    '''Multiplication function'''
    assert multiplication(1,2) == 2

def test_postive_divison():
    '''Postive Divison test'''
    assert divison(1,1) == 1

def test_negative_divison():
    '''Negative Divison test'''
    with pytest.raises(ZeroDivisionError):
        divison (1,0)
