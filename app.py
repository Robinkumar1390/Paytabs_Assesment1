from flask import Flask, render_template, request, jsonify
from system1 import process_transaction

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/transaction", methods=["POST"])
def transaction():
    data = request.json
    result, status = process_transaction(data)
    return jsonify(result), status

if __name__ == "__main__":
    app.run(debug=True)
