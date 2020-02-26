import pytest

from fibonaci import fibonacci_closed, fibonacci_recursive


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
def test_fibonacci(test_input, expected):
    assert fibonacci_recursive(test_input) == expected


def test_range():
    for i in range(3000):
        assert fibonacci_recursive(int(i)) == fibonacci_closed(int(i))
