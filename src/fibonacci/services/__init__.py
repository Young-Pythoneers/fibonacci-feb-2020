from functools import lru_cache
from typing import List, Optional

from fibonacci.models import Fibonacci, db


@lru_cache(maxsize=4_000_000_000)
def fibonacci_recursive(n: int) -> Optional[int]:
    """Function that returns the nth number in the fibonacci sequence.

    Args:
        n (int): Return the number of the fibonacci sequence of this n.

    Returns:
        int: The nth number in the fibonacci sequence.

    Idea of method found at:
    https://codereview.stackexchange.com/questions/183231/python-3-fibonacci-implementation
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


def _add_fibonacci_values(values: List[Fibonacci], start_index: int, end_index: int):
    for i in range(start_index, end_index + 1):
        fib = Fibonacci(i, str(fibonacci_recursive(i)))
        db.session.add(fib)  # Add to database session
        values.append(fib)  # Add to existing values list


def fibonacci_up_to_index(n: int) -> List[Fibonacci]:
    """Function that provides a Fibonacci range up to and including the given n (index),
    it does so in conjunction with a SQLite database.
    It looks up the range given the index in the database.
    If there are numbers missing from the range this function will calculate those and add them to the database.

    Args:
        n: The nth index number of the fibonacci sequence.

    Returns:
        The range of Fibonacci numbers up to and including the given index.
    """
    values: List[Fibonacci] = (
        Fibonacci.query.filter(Fibonacci.index <= n).order_by(Fibonacci.index).all()
    )

    max_index = max(v.index for v in values) if len(values) else 0

    if max_index == n:
        return values

    if not len(values):
        _add_fibonacci_values(values, 0, n)
    else:
        _add_fibonacci_values(values, max_index + 1, n)

    db.session.commit()

    return values
