# app/calculator/__init__.py

from app.operations import addition, subtraction, multiplication, division  # Import the operation functions

class Calculator:
    """Calculator class to perform arithmetic operations."""

    @classmethod
    def create(cls):
        """Create a new Calculator instance."""
        return cls()

    def add(self, a, b):
        '''adds two numbers together'''
        return addition(a,b)

    def subtract(self, a, b):
        '''subtracts two numbers together'''
        return subtraction(a,b)

    def multiply(self, a, b):
        '''multiplies two numbers together'''
        return multiplication(a,b)

    def divide(self, a, b):
        '''divides two numbers together'''
        if b == 0:
            return "Error: Division by zero!"
        return division(a,b)
      