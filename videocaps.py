import cv2

image1=cv2.VideoCapture(0)
image=image1.read()
print(type(image1))
cv2.imshow("live video",image)
iamge1.release()
