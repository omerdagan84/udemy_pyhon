import numpy as np
import cv2

fac_cas = cv2.CascadeClassifier('/home/omerd/.local/lib/python3.6/site-packages/cv2/data/haarcascade_frontalface_default.xml')
#fac_cas = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
videocap = cv2.VideoCapture(0)

scale_factor = 1.1

while 1:
    ret, pic = videocap.read()
    #print("ret value " + str(ret))
    #if not ret :
    #    continue

    faces = fac_cas.detectMultiScale(pic, scale_factor, 5)
    print("number of faces found {}".format(len(faces)))
    for (x,y,w,h) in faces:
            cv2.rectangle(pic, (x,y), (x+w, y+h), (255,0,0), 2)
    cv2.imshow('test', pic)
    k = cv2.waitKey(30) & 0xff
    if k == 2:
        break

cv2.destroyAllWindows()
