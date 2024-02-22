import pytest
from calculator.calculator import Calculation

# Test using the 'calculation_records' fixture
def test_generated_operations(calculation_records):
    for a, b, operation, expected in calculation_records:
        calc = Calculation(a, b)
        if operation == 'add':
            result = calc.add()
        elif operation == 'subtract':
            result = calc.subtract()
        elif operation == 'multiply':
            result = calc.multiply()
        elif operation == 'divide':
            if expected == 'ValueError':
                with pytest.raises(ValueError):
                    calc.divide()
                continue
            result = calc.divide()
        assert result == expected
# Tests for specific cases for each operation
@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 15), 
    (2, 3, 5), 
    (0, 0, 0),
    (-1, -1, -2),
    (1.5, 2.5, 4)
])
def test_add(a, b, expected):
    calc = Calculation(a, b)
    assert calc.add() == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 5), 
    (3, 2, 1), 
    (0, 0, 0),
    (-1, 1, -2),
    (2.5, 1.5, 1)
])
def test_subtract(a, b, expected):
    calc = Calculation(a, b)
    assert calc.subtract() == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 50), 
    (3, 2, 6), 
    (0, 0, 0),
    (-1, -1, 1),
    (1.5, 2, 3)
])
def test_multiply(a, b, expected):
    calc = Calculation(a, b)
    assert calc.multiply() == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 2), 
    (15, 3, 5),
    (0, 1, 0),
    (-4, -2, 2),
    (1.5, 0.5, 3)
])
def test_divide(a, b, expected):
    calc = Calculation(a, b)
    assert calc.divide() == expected

# Test for division by zero
def test_divide_by_zero():
    calc = Calculation(10, 0)
    with pytest.raises(ValueError):
        calc.divide()

# Test for calculation history
def test_history():
    Calculation.history.clear()
    calc = Calculation(5, 3)
    calc.add()
    calc.subtract()
    history = Calculation.get_history()
    assert len(history) == 2
    assert history[0][0] == 'add'
    assert history[1][0] == 'subtract'
