import connexion
from flask import render_template, Flask, jsonify
from fibonaci.fibonacci import fibonacci_recursive, fibonacci_range, fibonacci_loop_max
from typing import List, Optional
import os
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import sqlite3
from fibonaci.models import Fibonacci
from functools import lru_cache

import json

__all__ = [
    "for_index",
    "up_to_including_index",
    "up_to_value",
]

@lru_cache(maxsize=4_000_000_000)
def fibonacci_recursive_with_database(n: int) -> int:
    conn = sqlite3.connect('Fibonacci.db')
    cur = conn.cursor()
    cur.execute(f'SELECT a_value FROM fibonacci where an_index is {n}')
    query_result = cur.fetchall()
    if query_result:
        output = int(query_result[0][0])
        print(str(n) + " found in database")
        return output
    elif n % 2 == 0:
        m = n // 2
        output = (fibonacci_recursive_with_database(m - 1) + fibonacci_recursive_with_database(m + 1)) * fibonacci_recursive_with_database(m)
    else:
        m = (n + 1) // 2
        output = fibonacci_recursive_with_database(m) ** 2 + fibonacci_recursive_with_database(m - 1) ** 2
    print(str(n) + " NOT found in database")
    fib_value = Fibonacci(an_index=n, a_value=str(output))
    db.session.add(fib_value)
    db.session.commit()
    return output

def for_index(n: int) -> str:
    return str(fibonacci_recursive_with_database(n))

def fibonacci_up_to_including_index_database(n: int) -> str:
    # conn = sqlite3.connect('Fibonacci.db')
    # cur = conn.cursor()
    # cur.execute('SELECT an_index FROM fibonacci ORDER BY an_index DESC LIMIT 1')
    # query_result = cur.fetchall()
    # if n <= query_result[0][0]:
    #     cur.execute(f'SELECT a_value FROM fibonacci where an_index <= {n}')
    #     print(str(n) + " found in database")
    #     return cur.fetchall()
    # else:
    #    print(str(n) + " NOT found in database")
    #    return fibonacci_range(n)
    pass
def up_to_including_index(n: int) -> Optional[List[int]]:
    return fibonacci_up_to_including_index_database(n)

def fibonacci_up_to_value_database(n: int) -> str:
    # conn = sqlite3.connect('Fibonacci.db')
    # cur = conn.cursor()
    # cur.execute('SELECT a_value FROM fibonacci ORDER BY a_value DESC LIMIT 1')
    # query_result = cur.fetchall()
    # if n <= int(query_result[0][0]):
    #     cur.execute(f'SELECT a_value FROM fibonacci where a_value <= {n}')
    #     print(str(n) + " found in database")
    #     return cur.fetchall()
    # else:
    #     print(str(n) + " NOT found in database")
    #     return fibonacci_loop_max(n)
    pass

def up_to_value(n: int) -> Optional[List[int]]:
    return fibonacci_up_to_value_database(n)


basedir = os.path.abspath(os.path.dirname(__file__))

# Create the Connexion application instance
app = connexion.App(__name__, specification_dir=basedir)
app.add_api("api/swagger.yml")


# Configure the SQLAlchemy part of the app instance
app.app.config['SQLALCHEMY_ECHO'] = True
app.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.path.join(basedir, 'fibonacci.db')
app.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create the SQLAlchemy db instance
db = SQLAlchemy(app.app)

# Initialize Marshmallow
ma = Marshmallow(app.app)

@app.app.route("/")
def home():
    return render_template("home.html")


def create_app():
    return app.app


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)