from gtts import gTTS
from flask import Flask, request, send_file
from flask_cors import CORS
import requests
import json

app = Flask(__name__)
CORS(app)

@app.route("/api/posts", methods=['POST'])
def uploadImage():
    image = request.files['image']
    will = request.values['will']
    emotiontext = request.values['emotion']
    dictToSend = {'result':True}
    print("posts posted")
    res = requests.post('http://localhost:5000/api/results', json=dictToSend)
    print("results")
    return " "

@app.route("/api/results", methods=['POST','GET'])
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
        audio = gTTS(text='fuck you',lang='en')
        audio.save("test.mp3")
        # with open('data.json') as f:
        #     result = json.load(f)
        return send_file(
         "test.mp3", 
         mimetype="audio/wav", 
         as_attachment=True, 
         attachment_filename="test.mp3")