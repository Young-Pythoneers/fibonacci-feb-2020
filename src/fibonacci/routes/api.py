from typing import List, Optional

from fibonacci.services import (
    fibonacci_recursive_with_database,
    fibonacci_up_to_index,
    fibonacci_up_to_value,
)


def up_to_including_index(n: int) -> List[int]:
    """ This function calls the fibonacci_up_to_including_index_database function using the given n (Fibonacci index).
    This function is created for code readability.
    """
    return fibonacci_up_to_index(n)


def up_to_value(n: int) -> Optional[List[str]]:
    """ This function calls the fibonacci_up_to_value_database function using the given n (random integer).
    This function is created for code readability.
    """
    return fibonacci_up_to_value(n)


def for_index(n: int) -> str:
    return str(fibonacci_recursive_with_database(n))
