from tensorflow.keras.models import load_model

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

def perdict_bert(s) :
    model = tf.saved_model.load("BERT")
    res = tf.sigmoid(model(tf.constant([s])))
    return res >= 0.5
