import time

from Other_Code.face.face_recognition import face_detection as mt
from Other_Code.face.face_recognition import facial_recognition as fa
from Other_Code.face.utils import utils
# from Cyl_FaceRecognition.settings import FACE_CLASS as face


import cv2
import numpy as np

def fac(base_dir):


    base_dir=str(base_dir)
    base_dir=base_dir.replace('\\','/')
    path = {
        'pnet': f'{base_dir}/static/face/face_model/pnet.h5',
        'rnet': f'{base_dir}/static/face/face_model/rnet.h5',
        'onet': f'{base_dir}/static/face/face_model/onet.h5',
        'facenet': f'{base_dir}/static/face/face_model/facenet.h5',
    }
    # 加载两个模型
    mtcnn = mt.Mtcnn(path)
    facenet = fa.Facenet(path)
    return [mtcnn,facenet]

def im(base_dir):
    base_dir = str(base_dir)
    base_dir = base_dir.replace('\\', '/')
    return cv2.imread(f"{base_dir}/static/img/face_test_img/zly.jpg")

if __name__ == '__main__':
    # path = "C:\MyFile\PyCharmWorkSpace\MyPython\Django_learn\Cyl_FaceRecognition"
    # face = fac(path)
    # camp = cv2.VideoCapture("http://192.168.137.83:8080/?action=stream")
    # # img = im(path)
    # while True:
    #     try:
    #         ret, frame = camp.read()
    #         img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    #         box = face[0].faceDecognition(img)
    #         box = utils.change_box(np.array(box))
    #         for bo in box:
    #             face_img = img[int(bo[1]):int(bo[3]), int(bo[0]):int(bo[2])]
    #             face_encoding = face[1].face_encoding(face_img, bo)
    #             print(face_encoding)
    #
    #             # facenet.
    #             cv2.rectangle(img, (int(bo[0]), int(bo[1])),
    #                           (int(bo[2]), int(bo[3])),
    #                           (0, 255, 0), 3)
    #
    #         cv2.imshow('img', img)
    #         cv2.waitKey(1)
    #     except Exception as e:
    #         print('************')




    path = "C:\MyFile\PyCharmWorkSpace\MyPython\Django_learn\Cyl_FaceRecognition"
    face = fac(path)
    # camp = cv2.VideoCapture("http://192.168.137.83:8080/?action=stream")
    img = im(path)
    # while True:
    # ret, frame = camp.read()
    # img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    tim1 = time.time()
    print(f'tim1{tim1}')
    box = face[0].faceDecognition(img)
    box = utils.change_box(np.array(box))
    tim2 = time.time()
    print(f'tim1{tim2}')
    print(int(tim2)-int(tim1))
    for bo in box:
        face_img = img[int(bo[1]):int(bo[3]), int(bo[0]):int(bo[2])]
        face_encoding = face[1].face_encoding(face_img, bo)
        print(face_encoding)

        # facenet.
        cv2.rectangle(img, (int(bo[0]), int(bo[1])),
                      (int(bo[2]), int(bo[3])),
                      (0, 255, 0), 3)

    cv2.imshow('img', img)


