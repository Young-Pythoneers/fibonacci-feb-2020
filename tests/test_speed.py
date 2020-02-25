from fibonaci import speed,fibonacci_closed,fibonacci_loop, fibonacci_recursive
from pathlib import Path

def test_run():
    file_path = Path("./speed_data_test.csv")
    assert speed(
        200,
        file_path,
        [
            fibonacci_closed,
            fibonacci_loop,
            fibonacci_recursive,
        ],
    )