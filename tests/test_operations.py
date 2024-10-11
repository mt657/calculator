# pylint: disable=redefined-outer-name
"""
Tests for the individual operation functions in the operations module.
Each test verifies the correctness of basic mathematical operations.
"""
import pytest
from app.operations import addition, subtraction, multiplication, division

@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 15),
    (1, 1, 2),
    (-1, -1, -2),
    (0, 0, 0),
])
def test_addition(a, b, expected):
    """
    Test the addition function.
    
    Verifies that the addition function correctly adds two numbers.
    """
    assert addition(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 5),
    (1, 1, 0),
    (-1, -1, 0),
    (0, 0, 0),
])
def test_subtraction(a, b, expected):
    """
    Test the subtraction function.
    
    Verifies that the subtraction function correctly subtracts the second number from the first.
    """
    assert subtraction(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 50),
    (1, 1, 1),
    (-1, -1, 1),
    (0, 10, 0),
])
def test_multiplication(a, b, expected):
    """
    Test the multiplication function.
    
    Verifies that the multiplication function correctly multiplies two numbers.
    """
    assert multiplication(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 2),
    (1, 1, 1),
    (-10, -2, 5),
    (0, 1, 0),
])
def test_division(a, b, expected):
    """
    Test the division function.
    
    Verifies that the division function correctly divides the first number by the second.
    """
    assert division(a, b) == expected

def test_division_by_zero():
    """
    Test the division by zero case.
    
    Verifies that the division function returns an error message when dividing by zero.
    """
    assert division(10, 0) == "Error: Division by zero!"
