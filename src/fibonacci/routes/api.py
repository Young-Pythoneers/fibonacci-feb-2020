from typing import Optional, List

from fibonacci.models import Fibonacci, db
from fibonacci.services import fibonacci_up_to_index


def up_to_including_index(n: int) -> List[int]:
    """ This function calls the fibonacci_up_to_including_index_database function using the given n (Fibonacci index).
    This function is created for code readability.
    """
    return [int(f.value) for f in fibonacci_up_to_index(n)]


def fibonacci_up_to_value_database(n: int) -> List[str]:
    """ Function that provides a Fibonacci range based on a random integer, it does so in conjunction with a SQLite database.
    It looks sequentially when the given n is smaller than a Fibonacci number and returns that range..
    If there are numbers missing from the range this function will calculate those and add them to the database.

    Args:
        n (int): The nth index number of the fibonacci sequence.

    Returns:
        output (List): The range of Fibonacci numbers based on a given random integer.
    """
    output = []
    conn = sqlite3.connect("fibonacci_database.db")
    i = 0
    while True:
        cur = conn.cursor()
        cur.execute(f"SELECT a_value FROM fibonacci where an_index is {i}")
        query_result = cur.fetchall()
        if query_result:
            fibonacci_number = query_result[0][0]
        else:
            fibonacci_number = str(int(output[-1]) + int(output[-2]))
            print(str(i) + " NOT found in database")
            database_entry = Fibonacci(an_index=i, a_value=fibonacci_number)
            db.session.add(database_entry)
            db.session.commit()
        if int(fibonacci_number) > n:
            break
        output.append(fibonacci_number)
        i += 1
    conn.close()
    return output


def up_to_value(n: int) -> Optional[List[str]]:
    """ This function calls the fibonacci_up_to_value_database function using the given n (random integer).
    This function is created for code readability.
    """
    return fibonacci_up_to_value_database(n)
