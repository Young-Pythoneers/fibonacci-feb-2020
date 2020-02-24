from fibonaci import closed_form
import time


def test_1():
    assert closed_form.fibonacci_recursive(0) == 0


def test_2():
    assert closed_form.fibonacci_recursive(-1) is None


def test_3():
    for i in range(300):
        assert closed_form.fibonacci_recursive(int(i)) == closed_form.fibonacci_loop(int(i))


def test_4():
    for i in range(300):
        assert closed_form.fibonacci_recursive(int(i)) == closed_form.fibonacci_closed(int(i))


def test_5():
    start = time.time()
    closed_form.fibonacci_recursive(4_000_000)
    stop = time.time()
    assert stop - start <= 10


def test_6():
    start = time.time()
    closed_form.fibonacci_loop(4_000_000)
    stop = time.time()
    assert stop - start <= 10
