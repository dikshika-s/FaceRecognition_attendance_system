import cv2
import face_recognition as fr
import numpy as np
import os
from datetime import datetime

basepath = os.path.abspath(os.path.dirname(__file__))

def run_script():
    # training image dataset will be stored in this folder
    path = os.path.join(basepath,'st_images') 

    # create an array to store name and images
    # images and name is extracted by traversing images present in 
    # path directory as images files are named as name.jpg
    images_l = []
    names_l = [] 
    classnames = os.listdir(path)
    for i in classnames:
        images_l.append(cv2.imread(f'{path}/{i}'))
        names_l.append(os.path.splitext(i)[0])

    # define function to encode images
    def encoder(images_l):
        encoder_l = []
        for img in images_l:
            img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
            encoded_info = fr.face_encodings(img)[0]
            encoder_l.append(encoded_info)
        return encoder_l

    # define function to mark attendance
    def markattendance(name):
        with open(os.path.join(basepath,'attendance1.csv'),'r+') as f:
            mylist = f.readlines()
            name_list = []
            for line in mylist:
                entry = line.split(',')
                now = datetime.now()
                date = now.strftime('%d-%B-%Y')
                if(entry[1]==date):
                    name_list.append(entry[0])
            if name not in name_list:
                now = datetime.now()
                date = now.strftime('%d-%B-%Y')
                time=now.strftime('%H:%M:%S')
                attendance='P'
                f.writelines(f'{name},{date},{time},{attendance}\n')
            else:
                return 0
    # train data
    encoder_face_train = encoder(images_l)

    # capture video
    capture  = cv2.VideoCapture(0) 
    while True:
        success, img = capture.read()
        # reduce image size to 1/4th for the inner frames
        imgS = cv2.resize(img, (0,0), None, 0.25,0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
        faces_in_frame = fr.face_locations(imgS)
        encoded_faces = fr.face_encodings(imgS, faces_in_frame)
        a=1
        for encode_face, faceloc in zip(encoded_faces,faces_in_frame):
            matches = fr.compare_faces(encoder_face_train, encode_face)
            # returns the distance between the test image and training set images
            faceDist = fr.face_distance(encoder_face_train, encode_face)
            matchIndex = np.argmin(faceDist)
            print(matchIndex)
            if matches[matchIndex]:
                name = names_l[matchIndex].upper().lower()
                y1,x2,y2,x1 = faceloc
                # since we scaled down by 4 times
                y1, x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
                # draw rectangular box
                cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
                cv2.rectangle(img, (x1,y2-35),(x2,y2), (0,255,0), cv2.FILLED)
                cv2.putText(img,name, (x1+6,y2-5), cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
                a=markattendance(name)
        cv2.imshow('webcam', img)
        if cv2.waitKey(0) & 0xFF == ord('x'):
            cv2.destroyAllWindows()
            print('a',a,a==0)
            if(a==0):
                return 0
            else:
                return '1'

if __name__ == '__main__':
    run_script()