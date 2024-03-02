import pytest
from unittest.mock import patch, Mock
from calculator.calculator import Calculator, AddCommand, SubtractCommand, MultiplyCommand, DivideCommand
from calculator import main



@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 15),
    (2, 3, 5),
    (0, 0, 0),
    (-1, -1, -2),
    (1.5, 2.5, 4)
])
def test_add_command(a, b, expected):
    command = AddCommand()
    assert command.execute(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 5),
    (3, 2, 1),
    (0, 0, 0),
    (-1, 1, -2),
    (2.5, 1.5, 1)
])
def test_subtract_command(a, b, expected):
    command = SubtractCommand()
    assert command.execute(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 50),
    (3, 2, 6),
    (0, 0, 0),
    (-1, -1, 1),
    (1.5, 2, 3)
])
def test_multiply_command(a, b, expected):
    command = MultiplyCommand()
    assert command.execute(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 2),
    (15, 3, 5),
    (0, 1, 0),
    (-4, -2, 2),
    (1.5, 0.5, 3)
])
def test_divide_command(a, b, expected):
    command = DivideCommand()
    if b == 0:
        with pytest.raises(ValueError):
            command.execute(a, b)
    else:
        assert command.execute(a, b) == expected

def run_calculator(input_values):
    outputs = []

    def mock_input(prompt):
        return input_values.pop(0)

    def mock_print(*args, **kwargs):
        # This will join all print arguments into a single string
        print_output = ' '.join(map(str, args))
        outputs.append(print_output)
        # Remove or comment out the following line to prevent recursion
        # print(f"Mock print called with: {print_output}")  # Diagnostic print

    with patch('builtins.input', side_effect=mock_input), patch('builtins.print', side_effect=mock_print):
        main()

    return outputs




def test_repl_addition():
    input_values = ["add 2 3", "exit"]
    expected_output = "Result: 5.0"

    mock_print = Mock()

    with patch('calculator.calculator.Calculator.load_plugins'), \
         patch('builtins.input', side_effect=input_values), \
         patch('builtins.print', mock_print):

        main()

    assert mock_print.call_count > 0
    mock_print.assert_any_call(expected_output)