from fibonacci.services import fibonacci_up_to_index


def test_fibonacci_up_to_index():
    result = fibonacci_up_to_index(5)

    assert len(result) == 6
