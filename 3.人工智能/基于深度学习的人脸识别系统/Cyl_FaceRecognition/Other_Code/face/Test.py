
from Other_Code.face.face_recognition import face_detection as mt
from Other_Code.face.face_recognition import facial_recognition as fa
from Other_Code.face.utils import utils
from Cyl_FaceRecognition.settings import BASE_DIR


import cv2
import numpy as np

def fac(base_dir):


    base_dir=str(base_dir)
    base_dir=base_dir.replace('\\','/')
    img = cv2.imread(f"{base_dir}/static/img/face_test_img/zly.jpg")
    path = {
        'pnet':  f'{base_dir}/static/face/face_model/pnet.h5',
        'rnet':  f'{base_dir}/static/face/face_model/rnet.h5',
        'onet': f'{base_dir}/static/face/face_model/onet.h5',
        'facenet': f'{base_dir}/static/face/face_model/facenet.h5',
    }
    # 加载两个模型
    mtcnn = mt.Mtcnn(path)
    facenet = fa.Facenet(path)
    # return [mtcnn,facenet] # ****************************
    box = mtcnn.faceDecognition(img)
    # 变正方形
    box = utils.change_box(np.array(box))

    for bo in box:

        face_img = img[int(bo[1]):int(bo[3]), int(bo[0]):int(bo[2])]
        face_encoding = facenet.face_encoding(face_img,bo)
        print(face_encoding)
        print(face_encoding[0])
        print(type(face_encoding[0]))

        # facenet.
        cv2.rectangle(img, (int(bo[0]), int(bo[1])),
                      (int(bo[2]), int(bo[3])),
                      (0, 255, 0), 3)
        for i in range(5, 15, 2):
            cv2.circle(img, (int(bo[i + 0]), int(bo[i + 1])), 2, (0, 255, 0))
    cv2.imshow('img', img)
    cv2.waitKey(0)

if __name__ == '__main__':
    fac(BASE_DIR)
