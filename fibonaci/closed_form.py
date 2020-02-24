import math
from functools import lru_cache
import time
import multiprocessing as mp


def fibonacci_closed(n: int) -> int:
    """Function that returns the nth number in the fibonacci sequence

    Args:
        n (int): Return the number of the fibonacci sequence of this index

    Returns:
        int: The nth number in the fibonacci sequence
    """
    phi = (1 + math.sqrt(5)) / 2
    return int(round((phi ** n) / math.sqrt(5)))


def fibonacci_loop(n: int) -> int:
    """Function that returns the nth number in the fibonacci sequence

    Args:
        n (int): Return the number of the fibonacci sequence of this index

    Returns:
        int: The nth number in the fibonacci sequence
    """
    if n <= 1:
        return [0, 1][n]
    else:
        min1, min2 = 1, 0
        for i in range(n - 1):
            min1, min2 = min1 + min2, min1
        return min1


def fibonacci_loop_n(n: int) -> list:
    """Function that returns the first n numbers of the fibonacci sequence

    Args:
        n (int): Return the fibonacci sequence up to n numbers

    Returns:
        list: The fibonacci sequence up to n numbers
    """
    fib = [0, 1]
    if n < 2:
        return fib[0:n + 1]
    else:
        for i in range(n - 1):
            fib.append(fib[-1] + fib[-2])
        return fib


def fibonaci_loop_max(n: int) -> list:
    """

    Args:
        n (int): Return the fibonacci sequence with with number smaller than n

    Returns:
        list: The fibonacci sequence with numbers smaller than n
    """
    fib = [0, 1]
    if n < 1:
        return fib[0:1]
    else:
        while True:
            num = fib[-1] + fib[-2]
            if num > n:
                break
            else:
                fib.append(num)
        return fib


@lru_cache(maxsize=4_000_000_000)
def fibonacci_recursive(n: int) -> int:
    """Function that returns the nth number in the fibonacci sequence

        Args:
            n (int): Return the number of the fibonacci sequence of this index

        Returns:
            int: The nth number in the fibonacci sequence

        Idea of method found at:
        https://codereview.stackexchange.com/questions/183231/python-3-fibonacci-implementation
        """
    if n < 0:
        raise ValueError("n must be >= 0")
        return None
    elif n < 3:
        return [0, 1, 1][n]
    elif n % 2 == 0:
        m = n // 2
        return (fibonacci_recursive(m - 1) + fibonacci_recursive(m + 1)) * fibonacci_recursive(m)
    else:
        m = (n + 1) // 2
        return fibonacci_recursive(m) ** 2 + fibonacci_recursive(m - 1) ** 2

@lru_cache(maxsize=4_000_000_000)
def fibonacci_recursive_multithreaded(n: int) -> int:
    """Function that returns the nth number in the fibonacci sequence

            Args:
                n (int): Return the number of the fibonacci sequence of this index

            Returns:
                int: The nth number in the fibonacci sequence

            Idea of method found at:
            https://codereview.stackexchange.com/questions/183231/python-3-fibonacci-implementation
            """
    if n < 0:
        raise ValueError("n must be >= 0")
        return None
    elif n < 3:
        return [0, 1, 1][n]
    elif n % 2 == 0:
        m = n // 2
        pool = mp.Pool(processes=3)
        results = [pool.apply(fibonacci_recursive_multithreaded, args=(x,)) for x in [m-1,m+1,m]]
        return (results[0]+results[1])*results[2]
    else:
        m = (n + 1) // 2
        pool = mp.Pool(processes=2)
        results = [pool.apply(fibonacci_recursive_multithreaded, args=(x,)) for x in [m, m - 1]]
        return results[0] ** 2 + results[1] ** 2

if __name__ == '__main__':

    for n in range(1000000, 10000000, 1000000):
        # print(fibonacci_closed(n))
        # timer_start: float = time.time()
        # fib_loop = fibonacci_loop(n)
        # print(fib_loop)
        # timer_stop = time.time()
        # loop_time = timer_stop-timer_start
        # print("fibonacci_loop(" + str(n) + ") took " + str(loop_time)+ " seconds.")

        timer_start = time.time()
        fib_rec = fibonacci_recursive(n)
        print(fib_rec)
        timer_stop = time.time()
        rec_time = timer_stop - timer_start
        print("fibonacci_recursive(" + str(n) + ") took " + str(rec_time) + " seconds.")
