import os

from config import db
from fibonacci import fibonacci_recursive
from models import Fibonacci

# Data to initialize database with

# Delete database file if it exists currently
if os.path.exists("fibonacci.db"):
    os.remove("fibonacci.db")

# Create the database
db.create_all()

n = 3000
for x in range(n):
    fib_value = Fibonacci(index_value= x, single_value = str(fibonacci_recursive(x)))
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