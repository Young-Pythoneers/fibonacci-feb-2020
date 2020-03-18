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

def fibonacci_up_to_index(n: int) -> List[Fibonacci]:
    """ Function that provides a Fibonacci range up to and including the given n (index), it does so in conjunction with a SQLite database.
        It looks up the range given the index in the database.
        If there are numbers missing from the range this function will calculate those and add them to the database.

        Args:
            n (int): The nth index number of the fibonacci sequence.

        Returns:
            output (List): The range of Fibonacci numbers up to and including the given index.
        """
    fibonacci_start = [0, 1]
    if n < 0:
        return None
    elif n < 2:
        return fibonacci_start[0 : n + 1]
    else:
        for single_number in range(n - 1):
            fibonacci_start.extend([fibonacci_start[-1] + fibonacci_start[-2]])
        return fibonacci_start

def fibonacci_up_to_value(n: int) -> List[Fibonacci]:
    """ Function that provides a Fibonacci range based on a random integer, it does so in conjunction with a SQLite database.
    It looks sequentially when the given n is smaller than a Fibonacci number and returns that range..
    If there are numbers missing from the range this function will calculate those and add them to the database.

    Args:
        n (int): The nth index number of the fibonacci sequence.

    Returns:
        output (List): The range of Fibonacci numbers based on a given random integer.
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
