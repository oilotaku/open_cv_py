import cv2
import numpy as np
img_name_fire = []      #擷取後的圖片
img_name = []   #擷取後圖片的檔案名稱
name_l = 0      #檔案名稱的編號
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')     #導入辨識庫
img_smp = cv2.imread ('test.jpg')       #讀取目標檔案
img_smp_gray = cv2.cvtColor(img_smp, cv2.COLOR_BGR2GRAY)        #圖片色彩變換
faces = face_cascade.detectMultiScale(
   img_smp,
   scaleFactor=1.01,
   minNeighbors=3,
   minSize = (130,20))
#辨識參數調整

for (x, y, w, h) in faces:
        name_l = name_l + 1
        cv2.rectangle(img_smp_gray, (x, y), (x + w, y + h), (0, 255, 0), 2)     #針對兩點畫方格
        img_name_fire.append(img_smp[y:y + h, x:x + w]) #存取內含物
        name = 'img_name' + str(name_l) +'.jpg' 
        img_name.append(name)
#畫出辨識物

for i in range(len(img_name)):
        cv2.imwrite(img_name[i],img_name_fire[i])
#儲存各個辨識物

cv2.imshow("mysmp",img_smp_gray)
cv2.waitKey(0)