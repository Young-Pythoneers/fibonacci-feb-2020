import connexion
from flask import render_template, Flask, jsonify
from fibonaci import fibonacci_recursive, fibonacci_range, fibonacci_loop_max

app = connexion.App(__name__, specification_dir="./")

app.add_api("api/swagger.yml")

@app.route("/")
def home():

    return jsonify(
        {
            "Go to http://127.0.0.1:5000/multi_values/": "then insert an index value to obtain a fibonacci range !"
        }
    )

    #return render_template("home.html")

#@app.route("/fibonacci/for_index/<int:n>/", methods=["GET", "POST"])
def for_index(n):
    return str(fibonacci_recursive(n))

#@app.route("/fibonacci/up-to-including-index", methods=["GET", "POST"])
def up_to_including_index(n):
    fibonacci_range(n)

#@app.route("/fibonacci/up-to-value", methods=["GET", "POST"])
def up_to_value(n):
    fibonacci_loop_max(n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

