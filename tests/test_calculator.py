# tests/test_calculator.py
import pytest

from calculator.calculator import Calculator, Calculation

# Tests for Calculation class using instance methods

def test_calculation_add():
    calc = Calculation(1, 2)
    assert calc.add() == 3

def test_calculation_subtract():
    calc = Calculation(5, 3)
    assert calc.subtract() == 2

def test_calculation_multiply():
    calc = Calculation(4, 3)
    assert calc.multiply() == 12

def test_calculation_divide():
    calc = Calculation(10, 2)
    assert calc.divide() == 5

def test_calculation_divide_by_zero():
    calc = Calculation(10, 0)
    with pytest.raises(ValueError):
        calc.divide()

