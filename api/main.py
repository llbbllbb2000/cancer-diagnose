from gtts import gTTS
from flask import Flask, request, send_file
from flask_cors import CORS
import requests
from predict import predict

app = Flask(__name__)
CORS(app)

whetherCancer = 2
tex = 'I need an image for diagnosing'

gTTS(text=tex,lang='en').save("test.mp3")

@app.route("/images", methods=['POST'])
def uploadImage():
    image = request.files['image']
    will = request.values['will']
    emotiontext = request.values['emotion']
    result = predict(image, will)
    dictToSend = {'result': result}
    requests.post('http://localhost:5000/results', json=dictToSend)
    return " "

@app.route("/results", methods=['POST','GET'])
def Result():
    global whetherCancer, tex
    if request.method == 'POST':
        whetherCancer = request.json['result']
        return " "
    if request.method == 'GET':
        if whetherCancer == 1:
            tex = 'The image implies cancer'
            gTTS(text=tex,lang='en').save("test.mp3")
            print("generated")
        elif whetherCancer == 0 :
            tex = 'The image does not imply cancer'
            gTTS(text=tex,lang='en').save("test.mp3")
            print("generated")
        requests.post('http://localhost:5000/test.mp3', json={})
        return tex

@app.route("/test.mp3", methods=['POST','GET'])
def res():
    if request.method == 'POST':
        return " "
    if request.method == 'GET':
        return send_file(
         "test.mp3", 
         mimetype="audio/wav", 
         as_attachment=True, 
         attachment_filename="test.mp3")