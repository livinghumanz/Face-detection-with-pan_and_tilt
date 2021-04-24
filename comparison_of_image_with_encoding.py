import face_recognition
import pickle
import numpy as np
import cv2

#use pickle to mine through dataset

with open('dataset_faces.dat','rb') as f:
    all_face_encodings=pickle.load(f)

#grab list of names and list of encodings

face_names = list(all_face_encodings.keys())
face_encodings = np.array(list(all_face_encodings.values()))


#unlnown face encoding 

unknown_image = face_recognition.load_image_file("./images/pic.jpg")
cv2.imshow('img',unknown_image)
cv2.waitKey(0)

#unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

#get result of compared faces with encoding
#results = face_recognition.compare_faces(face_encodings, unknown_encoding)

#print result with list of names with true or false
#names_with_result=list(zip(face_names,results))
#print(names_with_result)
