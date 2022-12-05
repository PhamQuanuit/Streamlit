
import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def showimg(img):
    cv2.imshow("camera", img)
    return 0

def detect(img):
    # chuyển ảnh màu sang ảnh xám
    if img is not None:
        gray = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2GRAY)
        # cv2.imshow('gray', gray)
        # nhận diện mặt người
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        for (x, y, w, h) in faces:
            #print('img: ', x, y, w, h)
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

        return img
    else:
        return None