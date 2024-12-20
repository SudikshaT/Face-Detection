import cv2
face_classifier=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
imp=cv2.imread("A:\\imgpros\\imgp\\image\\TomHolland.jpg")
gim=cv2.cvtColor(imp,cv2.COLOR_BGR2GRAY)
face=face_classifier.detectMultiScale(gim, scaleFactor=1.1,minNeighbors=5,minSize=(20,20))
for(x,y,w,h) in face:
 cv2.rectangle(imp, (x,y), (x+w,y+h), (2,22,222),4)
cv2.imshow("pic",imp)
cv2.waitKey()
