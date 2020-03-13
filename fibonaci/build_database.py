import os

from fibonaci.config import db
from fibonaci.fibonacci import fibonacci_recursive
from fibonaci.models import Fibonacci

# Data to initialize database with

def create_new_database(database_name):
    # Delete database file if it exists currently
    if os.path.exists(database_name):
        os.remove(database_name)

    # Create the database
    db.create_all()

    n = 3
    for x in range(n):
        fib_value = Fibonacci(an_index = x, a_value = str(fibonacci_recursive(x)))
        db.session.add(fib_value)

    db.session.commit()

if __name__ == '__main__':
    create_new_database("fibonacci_database.db")

## TEST SCRIPT FOR DB
# import sqlite3
#
# conn = sqlite3.connect('fibonacci.db')
# cur = conn.cursor()
# cur.execute('SELECT * FROM fibonacci')
# fizz_buzz = cur.fetchall()
# print(fizz_buzz)
# for Fizz in fizz_buzz:
#     print(Fizz)