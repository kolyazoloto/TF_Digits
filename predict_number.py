import tensorflow as tf
import cv2 as cv
import numpy as np
categories = ["1","9"]


def prepare(filepath):
    IMG_SIZE = 30
    img_array = cv.imread(filepath,cv.IMREAD_GRAYSCALE)
    new_img = cv.resize(img_array,(IMG_SIZE,IMG_SIZE))
    return np.array(new_img).reshape(-1, IMG_SIZE, IMG_SIZE, 1)


img_array = prepare('C:/Users/Nikolay/Desktop/Screenshot_4.jpg')

model = tf.keras.models.load_model('model.model')

prediction = model.predict([img_array])

print(prediction)
print(categories[int(prediction[0][0])])