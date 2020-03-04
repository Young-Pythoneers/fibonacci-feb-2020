import connexion
from flask import render_template, Flask, jsonify
from fibonaci import fibonacci_recursive, fibonacci_range, fibonacci_loop_max
from typing import List, Optional
import os
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import sqlite3

__all__ = [
    "for_index",
    "up_to_including_index",
    "up_to_value",
]

def for_index(n: int) -> int:
    #return fibonacci_recursive(n)
    conn = sqlite3.connect('fibonacci.db')
    cur = conn.cursor()
    cur.execute(f'SELECT single_value FROM fibonacci where index_value is {n}')
    output = cur.fetchall()
    return output[0][0]


def up_to_including_index(n: int) -> Optional[List[int]]:
    return fibonacci_range(n)

def up_to_value(n: int) -> Optional[List[int]]:
    return fibonacci_loop_max(n)


basedir = os.path.abspath(os.path.dirname(__file__))

# Create the Connexion application instance
connex_app = connexion.App(__name__, specification_dir=basedir)
connex_app.add_api("api/swagger.yml")

app = connex_app.app


# Configure the SQLAlchemy part of the app instance
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.path.join(basedir, 'fibonacci.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create the SQLAlchemy db instance
db = SQLAlchemy(app)

# Initialize Marshmallow
ma = Marshmallow(app)

@app.route("/")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)