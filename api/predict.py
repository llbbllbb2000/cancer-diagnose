from tensorflow.keras.models import load_model

import numpy as np
from PIL import Image

def predict(file_image):
    model = load_model("CNNs.h5")
    image = Image.open(file_image)
    resized_image = image.convert('RGB').resize((96, 96), Image.BILINEAR)
    img = np.array(resized_image)

    # 1：cancer   0:no cancer
    return int(np.round(model.predict(img[np.newaxis,:]))[0][0])