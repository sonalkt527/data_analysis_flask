from flask import Flask, request, jsonify
from backend import find_res as model



app = Flask(__name__)




@app.route('/')
def home():
    return "hello world"


@app.route('/predict', methods=['POST'])
def predict():
    username = request.form.get('result')
    result=model.get_id("s","tseries")
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)