# FaceRecognition_attendance_system
This is a browser-based application of Face Recognition technology. This FACE ATTENDANCE SYSTEM website is built primarily with the OPENCV and the Django framework. It recognises the user's face and records their attendance.

### Features and functionalities:
1) Record attendance in a streamlined manner
2) Examine the attendance sheet
3) Create a New Student Account
4) Simple and intuitive UI


### TechStack
* Python 3.9.6 
* Django 2.2

### Installation Steps:
1) Clone the repository using `git clone https://github.com/dikshika-s/FaceRecognition_attendance_system`.
2) Install [Django framework](https://docs.djangoproject.com/en/4.0/topics/install/).
3) Install the Python libraries OpenCV, face_recognition, numpy, OS and pandas.
4) In the terminal navigate to upper folder *mysite* : 

    `cd mysite`
5) Run the application: 
    
    `python manage.py runserver`
6) A local host link will appear in the terminal, which you can copy into your browser to view the website.  
   [localhost:(http://127.0.0.1:8000/)](http://127.0.0.1:8000/)

---

> Bug :
It is not a bug per se, but I didn’t use WEBRTC to access camera so it is accessing the python shell webcam, hosting it directly may result in the webcamera not being accessible.
