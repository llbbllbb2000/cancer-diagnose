from tensorflow.keras.models import load_model
import tensorflow as tf
import tensorflow_text as text
import numpy as np
from PIL import Image

def predict(file_image, will):
    model = load_model("CNNs.h5")
    image = Image.open(file_image)
    resized_image = image.convert('RGB').resize((96, 96), Image.BILINEAR)
    img = np.array(resized_image)
    if will == "true":
        print("saved to db")
    # 1：cancer   0:no cancer
    return int(np.round(model.predict(img[np.newaxis,:]))[0][0])

def predict_bert(s):
    model = lode_model("BERT.h5")
    res = tf.sigmoid(model.predict([s]))
    return res >= 0.5
