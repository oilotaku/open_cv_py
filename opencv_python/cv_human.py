import cv2
import numpy as np
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img_smp = cv2.imread ('test.jpg')
img_smp_gray = cv2.cvtColor(img_smp, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(
    img_smp,
    scaleFactor=1.001,
    minNeighbors=30,
    minSize = (130,15))

for (x, y, w, h) in faces:
    cv2.rectangle(img_smp, (x, y), (x + w, y + h), (0, 255, 0), 2)


cv2.imshow ('my', img_smp)
cv2.waitKey(0)
