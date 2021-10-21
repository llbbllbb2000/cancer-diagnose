import tensorflow as tf
from tensorflow.keras.models import Sequential, load_model

import matplotlib.image as mpig
import numpy as np
from PIL import Image

def predict(file_image):
    model = load_model("CNNs.h5")
    image = Image.open(file_image)
    resized_image = image.convert('RGB').resize((96, 96), Image.BILINEAR)
    img = np.array(resized_image)

    # 1：cancer   0:no cancer
    return np.round(model.predict(img[np.newaxis,:]))