# tests/test_calculator.py
import pytest
from calculator.calculator import Calculation

@pytest.fixture
def calculation_fixture():
    return Calculation(10, 5)

@pytest.mark.parametrize("a, b, expected", [(10, 5, 15), (2, 3, 5), (0, 0, 0)])
def test_add(a, b, expected):
    calc = Calculation(a, b)
    assert calc.add() == expected

@pytest.mark.parametrize("a, b, expected", [(10, 5, 5), (3, 2, 1), (0, 0, 0)])
def test_subtract(a, b, expected):
    calc = Calculation(a, b)
    assert calc.subtract() == expected

@pytest.mark.parametrize("a, b, expected", [(10, 5, 50), (3, 2, 6), (0, 0, 0)])
def test_multiply(a, b, expected):
    calc = Calculation(a, b)
    assert calc.multiply() == expected

@pytest.mark.parametrize("a, b, expected", [(10, 5, 2), (15, 3, 5)])
def test_divide(a, b, expected):
    calc = Calculation(a, b)
    assert calc.divide() == expected

def test_divide_by_zero():
    calc = Calculation(10,0) # Setting b to zero
    with pytest.raises(ValueError):
        calc.divide()

def test_history(calculation_fixture):
    Calculation.history.clear()
    calculation_fixture.add()
    calculation_fixture.subtract()
    history = Calculation.get_history()
    assert len(history) == 2  # Check if two operations were added to the history

