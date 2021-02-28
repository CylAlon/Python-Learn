import cv2
import numpy as np
from Other_Code.face.network import mtcnn
from Other_Code.face.utils import utils

class Mtcnn():
    def __init__(self,path):
        self.p_net = mtcnn.create_Pnet(path['pnet'])
        self.r_net = mtcnn.create_Rnet(path['rnet'])
        self.o_net = mtcnn.create_Onet(path['onet'])


    def create_box_pnet(self,img,scales):
        """
            function:创建pnet的候选框
            parameters: img 图像  scales 比例
            return:候选框
        """
        h, w, _ = img.shape
        boxes = []
        for scale in scales:
            h_zoom = int(h * scale)
            w_zoom = int(w * scale)
            new_img = cv2.resize(img, (w_zoom, h_zoom))
            inputs = new_img.reshape(1, *new_img.shape)
            out = self.p_net.predict(inputs)
            boxes.append(out)

        bo=[]
        for i in range(len(scales)):
            # 脸的置信度
            face_pro = boxes[i][0][0][:, :, 1]
            # 其对应的框的位置
            face_loca = boxes[i][1][0]
            box = utils.restore_box_Pnet(face_pro,face_loca, scales[i], 0.5)
            bo.extend(box)

        # 进行非极大抑制
        boxes = utils.NMS(bo, 0.7)
        return boxes
    def create_box_rent(self,boxes,img):

        inputs = []
        for box in boxes:
            crop_img = img[int(box[1]):int(box[3]), int(box[0]):int(box[2])]
            if crop_img.size != 0:
                scale_img = cv2.resize(crop_img, (24, 24))
                inputs.append(scale_img)

        inputs = np.array(inputs)
        out = self.r_net.predict(inputs)

        face_prob = np.array(out[0])
        box_location = np.array(out[1])
        boxes = utils.restore_box_Rnet(face_prob, box_location, boxes, 0.6)
        return boxes
    def create_box_onet(self,boxes,img):
        inputs = []
        for box in boxes:
            crop_img = img[int(box[1]):int(box[3]), int(box[0]):int(box[2])]
            scale_img = cv2.resize(crop_img, (48, 48))
            inputs.append(scale_img)

        inputs = np.array(inputs)
        output = self.o_net.predict(inputs)

        face_prob = output[0]
        face_location = output[1]
        landmak = output[2]

        boxes = utils.restore_box_Onet(face_prob, face_location, landmak, boxes, 0.7)
        return boxes

    def faceDecognition(self,img):
        new_img = utils.normalization(img)
        scales = utils.img_scales(new_img)

        boxes = self.create_box_pnet(new_img,scales)


        if len(boxes)==0:
            return boxes
        boxes = self.create_box_rent(boxes,new_img)

        if len(boxes)==0:
            return boxes
        out = self.create_box_onet(boxes, new_img)
        return out
    def face_test(self):
        print('这是测试')



