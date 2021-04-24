import face_recognition
import pickle
import numpy as np
import cv2
import random
emotion_choice=["happy","sad","normal","angry"]
#use pickle to mine through dataset
class facedetect:

    def __init__(cls):
        with open('dataset_faces.dat','rb') as f:
            all_face_encodings=pickle.load(f)

        #grab list of names and list of encodings

        cls.face_names = list(all_face_encodings.keys())
        cls.face_encodings = np.array(list(all_face_encodings.values()))
        
    def unknownface(cls,image):
         # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(image, (0, 0), fx=0.25, fy=0.25)
        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        
        #unknown_image = face_recognition.load_image_file(image)
        cls.unknown_encoding = face_recognition.face_encodings(rgb_small_frame,face_locations)
    
    def printname(self):
        
        if not self.unknown_encoding:
            print("unknown")
        else:
            li=[]
            emotiondic={}
            results = face_recognition.compare_faces(self.face_encodings, self.unknown_encoding)
            names_with_result=list(zip(self.face_names,results))
            for i in names_with_result:
                if i[1]==True:
                    li.append(i[0])
                    emotiondic[i[0]]=random.choice(emotion_choice)
            string_name="hello "+" and ".join(li)
            print(string_name,emotiondic)
            emotionstatement(**emotiondic)
    
def emotionstatement(**emotiondic):
    kl=emotiondic.keys()
    for name in kl:
        if emotiondic[name]=="happy":
             #happy quotes
            statement=r'life is better when we are happy, healthy, and successful.'
            print(name,statement)
            #play music
        elif emotiondic[name]=="sad":
            #sad quotes
            statement=r'It\'s time to just be happy. Being angry , sad and overthinking isn\'t worth it anymore. Just let things flow. Be positive. Hear this, you may get motivated '
            print(name,statement)
            #play motivating song
        elif emotiondic[name]=="normal":
            #neutral quotes
            statement=r'It\'s good being Normal.'
            print(name,statement)
        elif emotiondic[name]=="angry":
            #angry quotes
            statement=r'Anger dosen\'t solve anything. It builds nothing , but it can Destroy Everything.'
            print(name,statement)
            #play furious songs'''
           #print(name)
'''d={}
d['ram']='sad'
d['ramesh']='angry'
emotionstatement(**d)'''
