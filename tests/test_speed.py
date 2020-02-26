from pathlib import Path

from fibonaci import fibonacci_closed, fibonacci_loop, fibonacci_recursive, speed


def test_run():
    file_path = Path("./speed_data_test.csv")
    assert speed(
        200, file_path, [fibonacci_closed, fibonacci_loop, fibonacci_recursive,],
    )
