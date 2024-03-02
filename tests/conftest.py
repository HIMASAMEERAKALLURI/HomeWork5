# tests/conftest.py
import pytest
from faker import Faker
from calculator.calculator import Calculator

# Command line option for number of records
def pytest_addoption(parser):
    parser.addoption(
        "--num_records", action="store", default=10, type=int, help="Number of records to generate"
    )

# Fixture to access the number of records option
@pytest.fixture
def num_records(request):
    return request.config.getoption("--num_records")

# Fixture for generating calculation records
@pytest.fixture
def calculation_records(faker, num_records):
    records = []
    calc = Calculator()
    for _ in range(num_records):
        a = faker.random_number(digits=2, fix_len=True)
        b = faker.random_number(digits=2, fix_len=True)
        operation = faker.random_element(elements=('add', 'subtract', 'multiply', 'divide'))
        expected = None
        try:
            expected = calc.execute_command(operation, a, b)
        except ValueError:
            expected = 'ValueError'
        records.append((a, b, operation, expected))
    return records
