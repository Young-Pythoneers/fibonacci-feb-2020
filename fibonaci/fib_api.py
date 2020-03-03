import connexion
from flask import Flask, jsonify, request
from fibonaci import fibonacci_recursive

app = connexion.App(__name__, specification_dir="./")

app.add_api("api/swagger.yml")

def api_fibonacci(n):
    return fibonacci_recursive(n)

@app.route("/", methods=["GET", "POST"])
def index():
    return jsonify(
        {
            "Go to http://127.0.0.1:5000/multi_values/": "then insert an index value to obtain a fibonacci range !"
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
