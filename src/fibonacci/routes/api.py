from typing import Optional, List

from fibonacci.models import Fibonacci, db
from fibonacci.services import fibonacci_up_to_index, fibonacci_up_to_value


def up_to_including_index(n: int) -> List[int]:
    """ This function calls the fibonacci_up_to_including_index_database function using the given n (Fibonacci index).
    This function is created for code readability.
    """
    return [int(f.value) for f in fibonacci_up_to_index(n)]


def up_to_value(n: int) -> Optional[List[str]]:
    """ This function calls the fibonacci_up_to_value_database function using the given n (random integer).
    This function is created for code readability.
    """
    return [int(f.value) for f in fibonacci_up_to_value(n)]
