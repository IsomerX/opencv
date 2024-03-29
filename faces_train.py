import os
import cv2 as cv
import numpy as np

p = []

for i in os.listdir(r'C:\Users\dbaks\OneDrive\Desktop\desktop\programming\python\opencv\train'):
    p.append(i)

DIR = "C:/Users/dbaks/OneDrive/Desktop/desktop/programming/python/opencv/train"
features = []
labels = []

haar = cv.CascadeClassifier("haar_face.xml")

def train():
    for person in p:
        path = os.path.join(DIR, person)
        label = p.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_arr = cv.imread(img_path)
            gray = cv.cvtColor(img_arr, cv.COLOR_BGR2GRAY)

            faces = haar.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for (x,y,w,h) in faces:
                faces_roi = gray[y:y+h, x:x+w]
                # region of interest = roi 
                features.append(faces_roi)
                labels.append(label)

            
train()

# print(f'length of features {len(features)}')
# print(f'length of labels {len(labels)}')

features = np.array(features, dtype='object')
labels = np.array(labels)

face_recog = cv.face.LBPHFaceRecognizer_create()

# train the recogniser now
face_recog.train(features, labels)

np.save('features.npy', features)
np.save('labels.npy', labels)