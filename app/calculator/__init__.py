# app/calculator/__init__.py

from app.operations import addition, subtraction, multiplication, division  # Import the operation functions

class Calculator:
    """Calculator class to perform arithmetic operations."""

    @classmethod
    def create(cls):
        """Create a new Calculator instance."""
        return cls()

    def add(self, a, b):
        """Perform addition operation."""
        return addition(a, b)

    def subtract(self, a, b):
        """Perform subtraction operation."""
        return subtraction(a, b)

    def multiply(self, a, b):
        """Perform multiplication operation."""
        return multiplication(a, b)

    def divide(self, a, b):
        """Perform division operation."""
        return division(a, b)
