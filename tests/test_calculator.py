import pytest
from app.calculator import Calculator  # Assuming the class is in a file named calculator.py

# Fixture to create a Calculator instance for each test
@pytest.fixture
def calc():
    return Calculator()

@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 15),
    (1, 1, 2),
    (-1, -1, -2),
    (0, 0, 0),
])
def test_add(calc, a, b, expected):
    assert calc.add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 5),
    (1, 1, 0),
    (-1, -1, 0),
    (0, 0, 0),
])
def test_subtract(calc, a, b, expected):
    assert calc.subtract(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 50),
    (1, 1, 1),
    (-1, -1, 1),
    (0, 10, 0),
])
def test_multiply(calc, a, b, expected):
    assert calc.multiply(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 2),
    (1, 1, 1),
    (-10, -2, 5),
    (0, 1, 0),
])
def test_divide(calc, a, b, expected):
    assert calc.divide(a, b) == expected

# Test for division by zero
def test_divide_by_zero(calc):
    assert calc.divide(10, 0) == "Error: Division by zero!"
