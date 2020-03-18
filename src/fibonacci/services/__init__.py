from functools import lru_cache
from typing import List, Optional
import sqlite3
from fibonacci.models import Fibonacci, db


@lru_cache(maxsize=4_000_000_000)
def fibonacci_recursive_with_database(n: int) -> int:
    """ Function that provides a Fibonacci number given te index, it does so in conjunction with a SQLite database.
    It first looks up the Fibonacci number given te index in the database.
    If it does not exist it calculates it using the recursive Fibonacci equation and adds it to the database.

    Args:
        n (int): The nth index number of the fibonacci sequence.

    Returns:
        int: The nth number in the fibonacci sequence .
    """
    conn = sqlite3.connect("fibonacci_database.db")
    cur = conn.cursor()
    cur.execute(f"SELECT a_value FROM fibonacci where an_index is {n}")
    query_result = cur.fetchall()
    if query_result:
        output = int(query_result[0][0])
        return output
    if n % 2 == 0:
        m = n // 2
        output = (
            fibonacci_recursive_with_database(m - 1)
            + fibonacci_recursive_with_database(m + 1)
        ) * fibonacci_recursive_with_database(m)
    else:
        m = (n + 1) // 2
        output = (
            fibonacci_recursive_with_database(m) ** 2
            + fibonacci_recursive_with_database(m - 1) ** 2
        )
    print(str(n) + " NOT found in database")
    fib_value = Fibonacci(an_index=n, a_value=str(output))
    db.session.add(fib_value)
    db.session.commit()
    conn.close()
    return output

def fibonacci_up_to_index(n: int) -> List[Fibonacci]:
    """ Function that provides a Fibonacci range up to and including the given n (index), it does so in conjunction with a SQLite database.
        It looks up the range given the index in the database.
        If there are numbers missing from the range this function will calculate those and add them to the database.

        Args:
            n (int): The nth index number of the fibonacci sequence.

        Returns:
            output (List): The range of Fibonacci numbers up to and including the given index.
        """
    output = []
    conn = sqlite3.connect("fibonacci_database.db")
    for i in range(n + 1):
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
        output.append(fibonacci_number)
    conn.close()
    return output

def fibonacci_up_to_value(n: int) -> List[Fibonacci]:
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

