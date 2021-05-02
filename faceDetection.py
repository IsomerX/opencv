import cv2 as cv

img = cv.imread('images/2.jpg')
cv.imshow('Person', img)



cv.waitKey(0)