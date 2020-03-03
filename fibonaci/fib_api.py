import connexion
from flask import render_template, Flask, jsonify
from fibonaci import fibonacci_recursive, fibonacci_range, fibonacci_loop_max
from typing import List, Optional

__all__ = [
    "for_index",
    "up_to_including_index",
    "up_to_value",
]

def for_index(n: int) -> int:
    return fibonacci_recursive(n)

def up_to_including_index(n: int) -> Optional[List[int]]:
    return fibonacci_range(n)

def up_to_value(n: int) -> Optional[List[int]]:
    return fibonacci_loop_max(n)

app = connexion.App(__name__, specification_dir="./")

app.add_api("api/swagger.yml")

@app.route("/")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
