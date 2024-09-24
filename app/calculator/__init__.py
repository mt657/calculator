#Import your operations module functions
from app.operations import addition, subtraction, multiplication, division

class Calculator:

    @staticmethod
    def create():
        return Calculator()
    
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero!"
        return a / b