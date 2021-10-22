from gtts import gTTS
from flask import Flask, request, send_file
from flask_cors import CORS
import requests
from predict import predict, predict_bert

app = Flask(__name__)
CORS(app)

whetherCancer = 2
emotionCondition = False
tex = 'I need an image for diagnosing'

gTTS(text=tex,lang='en').save("test.mp3")

@app.route("/images", methods=['POST'])
def uploadImage():
    image = request.files['image']
    will = request.values['will']
    emotiontext = request.values['emotion']
    result = predict(image, will)
    dictToSend = {'result': result, 'emotiontext': emotiontext}
    requests.post('http://localhost:5000/results', json=dictToSend)
    return " "

@app.route("/results", methods=['POST','GET'])
def Result():
    global whetherCancer, tex, emotionCondition
    if request.method == 'POST':
        whetherCancer = request.json['result']
        emotionCondition = predict_bert(request.json['emotiontext'])
        return " "
    if request.method == 'GET':
        if whetherCancer == 1 and emotionCondition:
            tex = 'The image implies cancer and I think it is Ok to tell you about that.'
            gTTS(text=tex,lang='en').save("test.mp3")
            print("generated")
        elif whetherCancer == 1 and not(emotionCondition):
            tex = 'The image implies cancer, but do not worry, everything will go better.'
            gTTS(text=tex,lang='en').save("test.mp3")
            print("generated")
        elif whetherCancer == 0 and emotionCondition:
            tex = 'The image does not imply cancer and I think you have already knew that.'
            gTTS(text=tex,lang='en').save("test.mp3")
            print("generated")
        elif whetherCancer == 0 and not(emotionCondition):
            tex = 'Congratulations! The image does not imply cancer.'
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