from fibonacci.timed_Fibonacci_func.Functions_for_speed_test import fibonacci_recursive, fibonacci_closed

def test_range():
    for i in range(4000):
        assert fibonacci_recursive(int(i)) == fibonacci_closed(int(i))
