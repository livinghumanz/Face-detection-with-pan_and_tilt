import face_recognition
import pickle
#import numpy as np

all_face_encodings={}

#add encoding to dictionary
thyagarajan_image = face_recognition.load_image_file("./images/thyagarajan.jpg")
all_face_encodings["thyagarajan"] = face_recognition.face_encodings(thyagarajan_image)[0]
ramesh_image = face_recognition.load_image_file("./images/ramesh.jpg")
all_face_encodings["ramesh"] = face_recognition.face_encodings(ramesh_image)[0]
raghav_image = face_recognition.load_image_file("./images/raghav.jpg")
all_face_encodings["raghav"] = face_recognition.face_encodings(raghav_image)[0]
rohit_image = face_recognition.load_image_file("./images/rohit.jpg")
all_face_encodings["rohit"] = face_recognition.face_encodings(rohit_image)[0]

#dump encoding to dat file named "dataset_faces"

with open('dataset_faces.dat','wb') as f:
    pickle.dump(all_face_encodings,f)
