# tests/test_calculator.py
import pytest

from calculator.calculator import add, subtract, multiply, divide

# Tests for addition
def test_add():
    assert add(1, 2) == 3
    assert add(4.5, 5.5) == 10

# Tests for subtraction
def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(10, 5.5) == 4.5

# Tests for multiplication
def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(2.5, 4) == 10

# Tests for division
def test_divide():
    assert divide(8, 4) == 2
    assert divide(9, 3) == 3

# Test for division by zero should raise an error
def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)

