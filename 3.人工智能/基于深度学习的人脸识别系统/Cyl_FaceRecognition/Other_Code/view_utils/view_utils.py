# encoding=utf-8
import traceback

import cv2
import random
import numpy as np


import pandas as pa


def createCode(index=4):
    """
        function:画二维码
        index:生成几位验证码
        return:二维码的名字或者内容
    """
    w = 120
    h = 60
    code = []
    name = ''
    source = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    zero_img = np.zeros((h, w, 3), np.uint8)  # 生成一张三维空列表

    # 给这张图随机添加像素点颜色
    for i in range(0, h, 2):
        for j in range(0, w, 2):
            for k in range(3):
                zero_img[i][j][k] = np.random.randint(0, 255)
    font = cv2.FONT_HERSHEY_SIMPLEX
    for i in range(index):
        word = str(random.choice(source))
        code.append(word)
        name += word
        cv2.putText(zero_img, word, (10 + i * 25, 40), font, 1, tuple(random.sample(range(0, 256), 3)), 4)
    cv2.imwrite('static/img/verification_code\\' + 'yzmimg.jpg', zero_img)
    return name


def try_log():
    # pass
    print('以下是异常捕获信息*************************')
    traceback.print_exc()
    print('以上是异常捕获信息*************************')




# # if '__name__' == '__main__':
#     print('*******')
#
# def verify_token(request):
#     """
#         function:验证token
#         request:
#         return:身份 db
#     """
#     token = 'radio1c3c927389bfb27d44026158270e71014'  #request.COOKIES.get('token') # *******************************************************
#     # print(token)
#     iden = str(token)[5:6]
#
#     uname = ''
#     unum = ''
#     img_path=''
#     try:
#         if iden == '1':
#             db = InfoStudent.objects.get(stu_token=token)
#             uname = db.stu_name
#             unum = db.stu_id
#             img_path = db.stu_pic_path
#         elif iden == '2':
#             db = InfoTeacher.objects.get(teach_token=token)
#             uname = db.teach_name
#             unum = db.teach_id
#         elif iden == '3':
#             db = InfoAdmin.objects.get(admin_token=token)
#             uname = db.admin_number
#             unum = uname
#         data = {
#             'title': '主页',
#             'nav_path':{'nav_path_one':'','nav_path_two':'','nav_path_three':''},
#             'uname': uname,
#             'unum': unum,
#             'img_path': img_path,
#             'file_flag':''
#         }
#         return [True,iden, db,data]
#     except Exception as e:
#
#         return [False,iden, db]




