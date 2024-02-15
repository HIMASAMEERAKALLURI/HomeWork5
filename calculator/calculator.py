# calculator/calculator.py
# pylint: disable=invalid-name
"""This module provides a Calculator class with basic arithmetic operations."""
class Calculator:
    """A simple calculator class to perform arithmetic operations."""
    @staticmethod
    def add(a: float, b: float) -> float:
        """Add two numbers and return the result."""
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        """Subtract two numbers and return the result."""
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        """Multiply two numbers and return the result."""
        return a * b

    @staticmethod
    def divide(a: float, b: float) -> float:
        """Divide the first number by the second and return the result.

        Raises:
            ValueError: If the second number (divisor) is zero.
        """
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b


class Calculation:
    """Calculation class that stores two numbers and performs operations with them."""
    def __init__(self, a: float, b: float):
        """Initialize the Calculation with two numbers."""
        self.a = a
        self.b = b

    def add(self) -> float:
        """Perform addition using the stored numbers."""
        return Calculator.add(self.a, self.b)

    def subtract(self) -> float:
        """Perform substraction using the stored numbers."""
        return Calculator.subtract(self.a, self.b)

    def multiply(self) -> float:
        """Perform multiplication using the stored numbers."""
        return Calculator.multiply(self.a, self.b)

    def divide(self) -> float:
        """Perform division using the stored numbers."""
        return Calculator.divide(self.a, self.b)

