import cv2
import numpy as np
from Other_Code.face.utils import utils
from Other_Code.face.network import facenet

class Facenet():
    def __init__(self,path):
        self.model = facenet.InceptionResNetV1()
        self.model.load_weights(path['facenet'])
    def face_encoding(self,img,box):
        landmark = []
        for i in range(5, 15, 2):
            landmark.append([box[i + 0], box[i + 1]])

        crop_img = cv2.resize(img, (160, 160))
        # cv2.imshow('dd', crop_img)
        new_img = utils.face_align(crop_img, landmark)
        # 改变形状
        new_img = np.expand_dims(new_img, 0)

        face_encoding = utils.calc_128_vec(self.model, new_img)
        return face_encoding


