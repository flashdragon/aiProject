import cv2
import itertools
import numpy as np
from time import time
import mediapipe as mp
import matplotlib.pyplot as plt



def makelandmark(img):
    mp_face_mesh = mp.solutions.face_mesh
    face_mesh_images = mp_face_mesh.FaceMesh(static_image_mode=True, max_num_faces=2,
                                         min_detection_confidence=0.5)
    sample_img = img


    x=len(sample_img[0])
    y=len(sample_img)

    face_mesh_results = face_mesh_images.process(sample_img[:,:,::-1])
    l=[]
    for single_face_landmarks in face_mesh_results.multi_face_landmarks:
        coordinates = single_face_landmarks.landmark[1] # 코끝
        new_x=int(coordinates.x*x)
        new_y=int(coordinates.y*y)
        li=[coordinates.x*x,coordinates.y*y]
        l.append(li)
        coordinates = single_face_landmarks.landmark[33] # 왼쪽눈 왼쪽
        new_x=int(coordinates.x*x)
        new_y=int(coordinates.y*y)
        li=[coordinates.x*x,coordinates.y*y]
        l.append(li)
        coordinates = single_face_landmarks.landmark[133] # 왼쪽눈 오른쪽
        new_x=int(coordinates.x*x)
        new_y=int(coordinates.y*y)
        li=[coordinates.x*x,coordinates.y*y]
        l.append(li)
        coordinates = single_face_landmarks.landmark[362] # 오른쪽눈 왼쪽
        new_x=int(coordinates.x*x)
        new_y=int(coordinates.y*y)
        li=[coordinates.x*x,coordinates.y*y]
        l.append(li)
        coordinates = single_face_landmarks.landmark[263] # 오른족눈 오른쪽
        new_x=int(coordinates.x*x)
        new_y=int(coordinates.y*y)
        li=[coordinates.x*x,coordinates.y*y]
        l.append(li)
        coordinates = single_face_landmarks.landmark[13] # 입술위
        new_x=int(coordinates.x*x)
        new_y=int(coordinates.y*y)
        li=[coordinates.x*x,coordinates.y*y]
        l.append(li)
        coordinates = single_face_landmarks.landmark[14] # 입술아래
        new_x=int(coordinates.x*x)
        new_y=int(coordinates.y*y)
        li=[coordinates.x*x,coordinates.y*y]
        l.append(li)
        coordinates = single_face_landmarks.landmark[76] # 입술왼쪽
        new_x=int(coordinates.x*x)
        new_y=int(coordinates.y*y)
        li=[coordinates.x*x,coordinates.y*y]
        l.append(li)
        coordinates = single_face_landmarks.landmark[291] # 입술오른쪽
        new_x=int(coordinates.x*x)
        new_y=int(coordinates.y*y)
        li=[coordinates.x*x,coordinates.y*y]
        l.append(li)
    l=np.array(l)
    return l