import os

from fibonaci.config import db
from fibonaci.fibonacci import fibonacci_recursive
from fibonaci.models import Fibonacci

# Delete database file if it exists currently
if os.path.exists("fibonacci_database.db"):
    os.remove("fibonacci_database.db")

# Create the database
db.create_all()

# Fill the database with Fibonacci index 0,1,2
# This is all you need to calculate the other Fibonacci numbers
n = 3
for x in range(n):
    fib_value = Fibonacci(an_index = x, a_value = str(fibonacci_recursive(x)))
    db.session.add(fib_value)

db.session.commit()

