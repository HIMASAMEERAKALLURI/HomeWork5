# calculator/calculator.py
# pylint: disable=invalid-name
"""This module provides classes for basic arithmetic operations and calculation history tracking."""

from typing import List, Tuple, Callable


class Calculator:
    """A simple calculator class to perform arithmetic operations."""
    
    @staticmethod
    def add(a: float, b: float) -> float:
        """Add two numbers and return the result.
        
        Args:
            a (float): The first number.
            b (float): The second number.
        
        Returns:
            float: The sum of the numbers.
        """
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        """Subtract two numbers and return the result.
        
        Args:
            a (float): The number to be subtracted from.
            b (float): The number to subtract.
        
        Returns:
            float: The difference of the numbers.
        """
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        """Multiply two numbers and return the result.
        
        Args:
            a (float): The first number.
            b (float): The second number.
        
        Returns:
            float: The product of the numbers.
        """
        return a * b

    @staticmethod
    def divide(a: float, b: float) -> float:
        """Divide the first number by the second and return the result.

        Args:
            a (float): The dividend.
            b (float): The divisor.

        Raises:
            ValueError: If the divisor is zero.

        Returns:
            float: The quotient of the numbers.
        """
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b


class Calculation:
    """A class to perform calculations and store their history."""

    history: List[Tuple[str, float, float, float]] = []

    def __init__(self, a: float, b: float):
        """Initialize the Calculation with two numbers.

        Args:
            a (float): The first number.
            b (float): The second number.
        """
        self.a = a
        self.b = b

    @classmethod
    def add_to_history(cls, operation: str, a: float, b: float, result: float):
        """Add a calculation record to the history.

        Args:
            operation (str): The operation performed.
            a (float): The first operand.
            b (float): The second operand.
            result (float): The result of the operation.
        """
        cls.history.append((operation, a, b, result))

    @classmethod
    def get_history(cls) -> List[Tuple[str, float, float, float]]:
        """Get the history of all calculations.

        Returns:
            List[Tuple[str, float, float, float]]: The history of calculations.
        """
        return cls.history

    def operate(self, operation: Callable[[float, float], float], op_name: str) -> float:
        """Perform an operation and add it to the history.

        Args:
            operation (Callable[[float, float], float]): The operation to perform.
            op_name (str): The name of the operation.

        Returns:
            float: The result of the operation.
        """
        result = operation(self.a, self.b)
        self.add_to_history(op_name, self.a, self.b, result)
        return result

    def add(self) -> float:
        """Perform addition using the stored numbers.

        Returns:
            float: The sum of the numbers.
        """
        return self.operate(Calculator.add, 'add')

    def subtract(self) -> float:
        """Perform subtraction using the stored numbers.

        Returns:
            float: The difference of the numbers.
        """
        return self.operate(Calculator.subtract, 'subtract')

    def multiply(self) -> float:
        """Perform multiplication using the stored numbers.

        Returns:
            float: The product of the numbers.
        """
        return self.operate(Calculator.multiply, 'multiply')

    def divide(self) -> float:
        """Perform division using the stored numbers.

        Returns:
            float: The quotient of the numbers.
        """
        return self.operate(Calculator.divide, 'divide')

