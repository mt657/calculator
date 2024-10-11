"""
Main calculator functions.

This module contains functions for basic arithmetic operations.
Each function accepts two numeric inputs and returns the result of the corresponding operation.
"""

def addition(a: float, b: float) -> float:
    """Adds two numbers together.

    Args:
        a (float): First operand.
        b (float): Second operand.

    Returns:
        float: Sum of a and b.
    """
    return a + b

def subtraction(a: float, b: float) -> float:
    """Subtracts second number from the first.

    Args:
        a (float): First operand.
        b (float): Second operand.

    Returns:
        float: Difference between a and b.
    """
    return a - b

def multiplication(a: float, b: float) -> float:
    """Multiplies two numbers together.

    Args:
        a (float): First operand.
        b (float): Second operand.

    Returns:
        float: Product of a and b.
    """
    return a * b

def division(a: float, b: float) -> float:
    """Divides first number by second.

    Args:
        a (float): First operand.
        b (float): Second operand.

    Returns:
        float: Quotient of a divided by b, or
        str: Error message if division by zero occurs.
    """
    if b == 0:
        return "Error: Division by zero!"
    return a / b
