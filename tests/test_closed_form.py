from fibonaci.fibonacci import fibonacci_closed, fibonacci_recursive
import pytest


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (0, 0),
        (-1, None),
        (20, 6765),
        (75, 2111485077978050)
        (150, 9969216677189303386214405760200),
        (300, 222232244629420445529739893461909967206666939096499764990979600),

    ])

def test_fibonacci(test_input, expected):
    assert fibonacci_recursive(test_input) == expected


def test_range():
    for i in range(300):
        assert closed_form.fibonacci_recursive(int(i)) == closed_form.fibonacci_closed(int(i))
