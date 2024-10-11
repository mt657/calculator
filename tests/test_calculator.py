# pylint: disable=redefined-outer-name
"""
Tests for the Calculator class, including all basic operations: add, subtract, multiply, and divide.
"""
import pytest
from app.calculator import Calculator

@pytest.fixture
def calculator():
    """
    Fixture to create a Calculator instance.
    Provides a fresh instance for each test.
    """
    return Calculator.create()

@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 15),
    (1, 1, 2),
    (-1, -1, -2),
    (0, 0, 0),
])
def test_add(calculator, a, b, expected):
    """
    Test the addition operation of the calculator.
    
    Verifies that the calculator correctly adds two numbers.
    """
    assert calculator.add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 5),
    (1, 1, 0),
    (-1, -1, 0),
    (0, 0, 0),
])
def test_subtract(calculator, a, b, expected):
    """
    Test the subtraction operation of the calculator.
    
    Verifies that the calculator correctly subtracts the second number from the first.
    """
    assert calculator.subtract(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 50),
    (1, 1, 1),
    (-1, -1, 1),
    (0, 10, 0),
])
def test_multiply(calculator, a, b, expected):
    """
    Test the multiplication operation of the calculator.
    
    Verifies that the calculator correctly multiplies two numbers.
    """
    assert calculator.multiply(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 2),
    (1, 1, 1),
    (-10, -2, 5),
    (0, 1, 0),
])
def test_divide(calculator, a, b, expected):
    """
    Test the division operation of the calculator.
    
    Verifies that the calculator correctly divides the first number by the second.
    """
    assert calculator.divide(a, b) == expected

def test_divide_by_zero(calculator):
    """
    Test the division by zero case.
    
    Verifies that the calculator returns an error message when dividing by zero.
    """
    assert calculator.divide(10, 0) == "Error: Division by zero!"
