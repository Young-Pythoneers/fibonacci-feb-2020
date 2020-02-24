from fibonaci.fibonacci import fibonacci_range
import pytest


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (0, [0]),
        (4, [0, 1, 1, 2, 3]),
        (10, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]),
        (
            20,
            [
                0,
                1,
                1,
                2,
                3,
                5,
                8,
                13,
                21,
                34,
                55,
                89,
                144,
                233,
                377,
                610,
                987,
                1597,
                2584,
                4181,
                6765,
            ],
        ),
    ],
)
def test_fibonacci(test_input, expected):
    assert fibonacci_range(test_input) == expected
