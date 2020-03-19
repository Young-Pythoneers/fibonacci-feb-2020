from decimal import Decimal, getcontext
from functools import lru_cache
from typing import List, Optional


@lru_cache(maxsize=4_000_000_000)
def fibonacci_recursive(n: int) -> int:
    """ Function that provides a Fibonacci number given te index, it does so in conjunction with a SQLite database.
    It first looks up the Fibonacci number given te index in the database.
    If it does not exist it calculates it using the recursive Fibonacci equation and adds it to the database.

    Args:
        n (int): The nth index number of the fibonacci sequence.

    Returns:
        int: The nth number in the fibonacci sequence .
    """

    if n < 0:
        return None
    elif n < 3:
        return [0, 1, 1][n]
    elif n % 2 == 0:
        m = n // 2
        return (
            fibonacci_recursive(m - 1) + fibonacci_recursive(m + 1)
        ) * fibonacci_recursive(m)
    else:
        m = (n + 1) // 2
        return fibonacci_recursive(m) ** 2 + fibonacci_recursive(m - 1) ** 2


def fibonacci_closed(n: int) -> int:
    """Function that returns the nth number in the fibonacci sequence
    Args:
        n (int): Return the number of the fibonacci sequence of this n
    Returns:
        int: The nth number in the fibonacci sequence
    """
    getcontext().prec = 1000
    phi = Decimal((1 + Decimal(5).sqrt()) / 2)
    psi = Decimal((1 - Decimal(5).sqrt()) / 2)
    return int((phi ** n - psi ** n) / Decimal(5).sqrt() + Decimal(0.5))


def fibonacci_loop(n: int) -> Optional[int]:
    """Function that returns the nth number in the fibonacci sequence
    Args:
        n (int): Return the number of the fibonacci sequence of this n
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
