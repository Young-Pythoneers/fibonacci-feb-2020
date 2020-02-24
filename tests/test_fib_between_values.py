from fibonaci.fibonacci import fibonaci_loop_max
import pytest


@pytest.mark.parametrize(
    "test_input,expected",
    [
        (1, [0, 1, 1]),
        (6, [0, 1, 1, 2, 3, 5]),
        (15, [0, 1, 1, 2, 3, 5, 8, 13]),
        (75, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]),
        (89, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]),
    ],
)
def test_fibonacci(test_input, expected):
    assert fibonaci_loop_max(test_input) == expected
