from flask import Flask, request, jsonify
from backend import find_res as model



app = Flask(__name__)




@app.route('/')
def home():
    return "hello world"


@app.route('/predict', methods=['POST'])
def predict():
    username = request.form.get('username')
    result=model.get_id('s',username)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=3000)
