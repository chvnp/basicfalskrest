import json
from flask import Flask,session, jsonify, request, abort
from flask_cors import CORS, cross_origin

from math_api.math_test import add_test,sub_test

app = Flask(__name__)
CORS(app)



@app.route('/', methods=['GET'])
def index():
    return "hello you are connected basic flask rest app"

@app.route('/add', methods=['POST'])
def add_fun():
    response_message = ""
    try:
        a = request.json['a']
        b = request.json['b']
        out = add_test(a,b)
        response_message = out
    except Exception as ex:
        response_message = str(ex)
    finally:
        return jsonify({'response':response_message})

@app.route('/sub', methods=['POST'])
def add_sub():
    response_message = ""
    try:
        a = request.json['a']
        b = request.json['b']
        out = sub_test(a,b)
        response_message = out
    except Exception as ex:
        response_message = str(ex)
    finally:
        return jsonify({'response':response_message})
    
if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True, port = 8000)
