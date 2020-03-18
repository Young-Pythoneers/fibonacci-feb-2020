from pathlib import Path
import os

from fibonacci.timed_Fibonacci_func.Functions_for_speed_test import fibonacci_closed, fibonacci_loop, fibonacci_recursive
from fibonacci.timed_Fibonacci_func.speed import speed

def test_run():
    file_path = Path("./speed_data_test.csv")
    output = speed(
        200, file_path, [fibonacci_closed, fibonacci_loop, fibonacci_recursive,],
    )
    os.remove(file_path)
    assert output
