from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return jsonify({"Go to http://127.0.0.1:5000/multi_values/" : "then insert an index value to obtain a fibonacci range !"})

@app.route('/multi_values/<int:index>', methods=['GET'])
def fibonaci_range(index):
    fibonacci_start = [0, 1]

    if index == 0:
        return 0
    elif index == 1:
        return 1

    else:
        for single_number in range(index-1):
            fibonacci_start.extend([fibonacci_start[-1] + fibonacci_start[-2]])
        return str(fibonacci_start[:-1])

if __name__ == '__main__':
    app.run(debug=True)
