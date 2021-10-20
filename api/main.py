import re
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import json

app = Flask(__name__)
CORS(app)

@app.route("/api/posts",methods=['POST'])
def uploadImage():
    image = request.files['image']
    willingness = request.files['willingness']
    emotiontext = request.files['emotion']
    dictToSend = {'result':True}
    print("posts posted")
    res = requests.post('http://localhost:5000/api/results', json=dictToSend)
    print("results")
    return " "

@app.route("/api/results",methods=['POST','GET'])
def Result():
    result = {}
    if request.method == 'POST':
        print("results posted")
        result = request.json
        with open('data.json', 'w') as f:
            json.dump(result, f)
        return " "
    if request.method == 'GET':
        print("get")
        with open('data.json') as f:
            result = json.load(f)
        return result