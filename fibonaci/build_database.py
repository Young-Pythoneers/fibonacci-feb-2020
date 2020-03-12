import os

from fibonaci.config import db
from fibonaci.fibonacci import fibonacci_recursive
from fibonaci.models import Fibonacci

# Data to initialize database with

# Delete database file if it exists currently
if os.path.exists("fibonacci_database.db"):
    os.remove("fibonacci_database.db")

# Create the database
db.create_all()

n = 3
for x in range(n):
    fib_value = Fibonacci(an_index = x, a_value = str(fibonacci_recursive(x)))
    db.session.add(fib_value)

db.session.commit()

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