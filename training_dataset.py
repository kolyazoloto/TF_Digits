import numpy as np
import matplotlib.pyplot as plt
import random
import pickle
import os,cv2 as cv
DATADIR = "C:/Users/Nikolay/PycharmProjects/TensorFlow/examples"
categories = ["1","9"]
IMG_SIZE = 30
training_data = []
def create_training_data():
    for category in categories:
        path = os.path.join(DATADIR,category)
        class_num = categories.index(category)
        for img in os.listdir(path):
            try:
                img_array = cv.imread(os.path.join(path,img),cv.IMREAD_GRAYSCALE)
                resize_img = cv.resize(img_array,(IMG_SIZE,IMG_SIZE))
                training_data.append([resize_img,class_num])
            except Exception as e:
                pass
create_training_data()
random.shuffle(training_data)
##################################################################
x = []
y = []
for features, label in training_data:
    x.append(features)
    y.append(label)
x = np.array(x).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
y = np.array(y)
pickle_out = open("x.pickle","wb")
pickle.dump(x,pickle_out)
pickle_out.close()

pickle_out = open("y.pickle","wb")
pickle.dump(y,pickle_out)
pickle_out.close()