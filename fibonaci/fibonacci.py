import math
from functools import lru_cache
import decimal


def fibonacci_closed(n: int) -> int:
    """Function that returns the nth number in the fibonacci sequence

    Args:
        n (int): Return the number of the fibonacci sequence of this index

    Returns:
        int: The nth number in the fibonacci sequence
    """
    decimal.getcontext().prec = 1_000_000
    phi = decimal.Decimal((1 + math.sqrt(5)) / 2)
    return int(round((phi ** n) / decimal.Decimal(math.sqrt(5))))


def fibonacci_loop(n: int) -> int:
    """Function that returns the nth number in the fibonacci sequence

    Args:
        n (int): Return the number of the fibonacci sequence of this index

    Returns:
        int: The nth number in the fibonacci sequence
    """
    if n < 0:
        return None
    elif n <= 1:
        return [0, 1][n]
    else:
        min1, min2 = 1, 0
        for i in range(n - 1):
            min1, min2 = min1 + min2, min1
        return min1

def fibonacci_range(index : int) -> list:

    """This function is used to calculate the fibonacci range up to and including the given index

    Args:
        index (int): The index is used for calculating the fibonacci range up to and including that index

    Returns:
        A fibonacci range given the index

    """

    fibonacci_start = [0, 1]
    if n < 0:
        return None
    elif n < 2:
        return fibonacci_start[0:index + 1]
    else:
        for single_number in range(index-1):
            fibonacci_start.extend([fibonacci_start[-1] + fibonacci_start[-2]])
        return fibonacci_start

def fibonaci_loop_max(n: int) -> list:
    """

    Args:
        n (int): Return the fibonacci sequence with with number smaller than n

    Returns:
        list: The fibonacci sequence with numbers smaller than n
    """
    fib = [0, 1]
    if n < 0:
        return None
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
        return None
    elif n < 3:
        return [0, 1, 1][n]
    elif n % 2 == 0:
        m = n // 2
        return (fibonacci_recursive(m - 1) + fibonacci_recursive(m + 1)) * fibonacci_recursive(m)
    else:
        m = (n + 1) // 2
        return fibonacci_recursive(m) ** 2 + fibonacci_recursive(m - 1) ** 2

if __name__ == '__main__':
    print(fibonacci_closed(2_000_000))