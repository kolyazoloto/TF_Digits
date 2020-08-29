#coding=utf-8
import cv2 as cv
import matplotlib.pylab as plt
import numpy as np
import os
import time

def saveNumbers(img):
    filename = img
    path = os.getcwd()
    newPath = os.path.join(path,'sudoku',filename)
    savePath = os.path.join(path,'examples')
    img = cv.imread(newPath,1)
    img = cv.resize(img,(600,800))
    canny = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    canny = cv.adaptiveThreshold(canny, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 13,5)
    contours, hierarchy = cv.findContours(canny, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    img_crop = None
    for index,cnt in enumerate(contours):
        if 100000< cv.contourArea(cnt) < 350000:
            (x,y,w,h) = cv.boundingRect(contours[index])
            if 400 < h < 800 and 400 < w < 700:
                #cv.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 7)
                img_crop = img[y:y + h, x:x + w]
    if (img_crop is None):
        print (f'чет с размером в файле {filename}' )
        return
    canny_crop = cv.cvtColor(img_crop, cv.COLOR_RGB2GRAY)
    canny_crop = cv.adaptiveThreshold(canny_crop, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11,7)
    contours, hierarchy = cv.findContours(canny_crop, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    prev = [[0,0,0,0]]
    prev_digits = [[0,0,0,0]]
    for index,cnt in enumerate(contours):
        if 1<cv.contourArea(cnt) < 6000:
            (x, y, w, h) = cv.boundingRect(cnt)
            if (20 < h < 55 and 10 < w < 40):
                isok = True
                for digit_i in prev_digits:
                    if (abs(x - digit_i[0]) > 10 or abs(y - digit_i[1]) > 10):
                        continue
                    else:
                        isok = False
                        break
                if (isok):
                    prev_digits.append([x,y,w,h])
                    numberIMG = img_crop[y:y + h, x:x + w]
                    numberIMG = cv.cvtColor(numberIMG, cv.IMREAD_GRAYSCALE)
                    numberIMG = cv.resize(numberIMG,(30,30))
                    cv.imwrite(savePath+ '//'+str(time.time())+'.jpg',numberIMG)

imgs = os.listdir(os.path.join(os.getcwd(),'sudoku'))

for img in imgs:
   saveNumbers(img)
