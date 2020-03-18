from fibonacci.services import fibonacci_recursive_with_database, fibonacci_up_to_index, fibonacci_up_to_value
import pytest

@pytest.mark.parametrize(
    "test_input,expected",
    [
        (0, 0),
        (-1, None),
        (20, 6765),
        (75, 2111485077978050),
        (150, 9969216677189303386214405760200),
        (300, 222232244629420445529739893461909967206666939096499764990979600),
    ],
)
def test_fibonacci_recursive_with_database(test_input, expected):
    assert fibonacci_recursive_with_database(test_input) == expected

def test_fibonacci_up_to_index_length():
    result = fibonacci_up_to_index(5)

    assert len(result) == 6

@pytest.mark.parametrize(
    "test_input,expected",
    [
        # fmt: off
        (0, ["0"]),
        (4, ["0", "1", "1", "2", "3"]),
        (10, ["0", "1", "1", "2", "3", "5", "8", "13", "21", "34", "55"]),
        (20, ["0", "1", "1", "2", "3", "5", "8", "13", "21", "34", "55", "89", "144", "233", "377", "610", "987", "1597", "2584", "4181", "6765"]),
        # fmt: on
    ],
)
def test_fibonacci_up_to_index_values(test_input, expected):
    assert fibonacci_up_to_index(test_input) == expected

def test_fibonacci_up_to_value_length():
    result = fibonacci_up_to_value(5)

    assert len(result) == 6

@pytest.mark.parametrize(
    "test_input,expected",
    [
        (1, ["0", "1", "1"]),
        (6, ["0", "1", "1", "2", "3", "5"]),
        (15, ["0", "1", "1", "2", "3", "5", "8", "13"]),
        (75, ["0", "1", "1", "2", "3", "5", "8", "13", "21", "34", "55"]),
        (89, ["0", "1", "1", "2", "3", "5", "8", "13", "21", "34", "55", "89"]),
    ],
)
def test_fibonacci_up_to_value(test_input, expected):
    assert fibonacci_up_to_value(test_input) == expected

def test_fobonacci():
    assert "fobonacci" != "fibonacci"