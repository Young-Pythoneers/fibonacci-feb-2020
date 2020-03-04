from typing import List, Optional

import connexion
from flask import render_template

from fibonaci.fibonacci import fibonacci_loop_max, fibonacci_range, fibonacci_recursive

__all__ = ["for_index", "up_to_including_index", "up_to_value", "create_app", "home"]


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


def create_app():
    return app.app


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)