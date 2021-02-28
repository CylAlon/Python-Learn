import numpy as np
import math
import cv2


def normalization(img):
    """
        function:图像归一化
        parameters:图片
        return:归一化后的图片
    """
    return (img - 127.5) / 127.5


def img_scales(img):
    """
        function:图像金字塔的比例
        parameters:图片
        return:缩放比例
    """
    scale = 1.0
    threshold = 500.0
    h, w, _ = img.shape
    ma = max(w,h)
    mi = min(w,h)
    ds = 0
    if mi > threshold:
        ds = threshold / mi
        w = int(w * ds)
        h = int(h * ds)
    elif ma < threshold:
        ds = threshold / ma
        w = int(w * ds)
        h = int(h * ds)

    scales = []
    factor = 0.709
    factor_count = 0
    mina = min(h, w)
    while mina >= 12:
        scales.append(scale * pow(factor, factor_count))
        mina *= factor
        factor_count += 1
    return scales


def IOU(box, boxes, flag=False):  # 第一个框 其余的框  两个功能  计算交际并集最小面积
    """
        function:计算交集面积
        parameters: box 第一个候选框  boxes剩下的候选框
        return:面积
    """
    # 计算第一个矩形框面积  x1 y1  x2  y2
    box_area = (box[2] - box[0]) * (box[3] - box[1])
    # 计算剩下的矩形框
    boxes_area = (boxes[:, 2] - boxes[:, 0]) * (boxes[:, 3] - boxes[:, 1])
    # 计算交集 左上角点
    xx1 = np.maximum(box[0], boxes[:, 0])
    yy1 = np.maximum(box[1], boxes[:, 1])
    xx2 = np.minimum(box[2], boxes[:, 2])
    yy2 = np.minimum(box[3], boxes[:, 3])
    # 判断偶没有交集
    w = np.maximum(0, xx2 - xx1)  # 这里是xx2-xx1比0大 则取大值
    h = np.maximum(0, yy2 - yy1)

    inter = w * h
    if flag:
        # 最小面积
        over_area = np.true_divide(inter, np.minimum(box_area, boxes_area))
    else:
        # 并集面积
        over_area = np.true_divide(inter, box_area + boxes_area - inter)
    return over_area


def NMS(boxes, thesh=0.3, flag=False):
    """
        function:去除相交面积大的
        parameters: boxes候选框  thesh阈值
        return:候选框
    """
    if len(boxes) == 0:
        return np.array([])  # 返回一个空框
    # 对boxes降序排序
    boxes = np.array(boxes)
    rank=boxes[-boxes[:, 4].argsort()]
    # boxes =   # 应为是一个二维的  所以前面的一维全要
    pick=[]
    while len(rank) > 0:  # 框大于1的时候才取
        a_box = rank[0]  # 排完序后第一个框要要
        b_box = rank[1:]  # 拿到第一个框后拿其余的框
        pick.append(a_box)
        rank = b_box[np.where(IOU(a_box, b_box, flag) < thesh)]
    return np.stack(pick)  # 操作的是numpy  这里是组装数据






def restore_box_Pnet(face_pro,face_loca, scale, con_coe=0.5):
    """
        function:还原pnet处理后的框
        parameters: boxe候选框 scale比例  con_coe阈值
        return:候选框
    """
    # boxes = np.array(boxes)


    index = np.where(face_pro > con_coe)  # 赛选出来大概率脸的索引
    out_h, out_w = face_pro.shape
    out_side = max(out_h, out_w)
    stride = 0
    # stride略等于2
    if out_side != 1:
        stride = float(2 * out_side - 1) / (out_side - 1)
    if index[0].size == 0:
        return np.array([])

    boundingbox = np.array([index[1], index[0]]).T
    # 找到对应原图的位置
    bb1 = np.fix((stride * (boundingbox) + 0) / scale)
    bb2 = np.fix((stride * (boundingbox) + 11) / scale)

    boundingbox = np.concatenate((bb1, bb2), axis=1)

    # 相对位置
    x1, y1, x2, y2 = [face_loca[index[0], index[1], i] for i in range(4)]

    offset = np.array([x1, y1, x2, y2]).T
    score = np.array(face_pro[index[0], index[1]]).reshape(-1, 1)

    boundingbox = boundingbox + (offset * 12.0) / scale

    newBox = np.concatenate((boundingbox, score), axis=1)
    newBox = change_box(newBox)

    newBox = NMS(newBox, 0.3)
    return newBox
def restore_box_Rnet(face_prob, box_location, boxes, threshold):
    """
        function:还原rnet处理后的框
        parameters: boxe候选框 scale比例  con_coe阈值
        return:候选框
    """
    prob = face_prob[:, 1]  # 获取置信度
    pick = np.where(prob >= threshold)  # 找到大概率的框索引

    rectangles = np.array(boxes)

    x1, y1, x2, y2 = [rectangles[pick, i] for i in range(4)]

    sc = np.array([prob[pick]]).T

    dx1, dx2, dx3, dx4 = [box_location[pick, i] for i in range(4)]

    w = x2 - x1
    h = y2 - y1
    x1 = np.array([(x1 + dx1 * w)[0]]).T
    y1 = np.array([(y1 + dx2 * h)[0]]).T
    x2 = np.array([(x2 + dx3 * w)[0]]).T
    y2 = np.array([(y2 + dx4 * h)[0]]).T

    rectangles = np.concatenate((x1, y1, x2, y2, sc), axis=1)
    rectangles = change_box(rectangles)
    newBoxes = NMS(rectangles, 0.3)
    return newBoxes


def restore_box_Onet(face_prob, face_location, landmak, boxes, threshold):
    prob = face_prob[:, 1]
    pick = np.where(prob >= threshold)
    rectangles = np.array(boxes)

    x1, y1, x2, y2 = [rectangles[pick, i] for i in range(4)]

    sc = np.array([prob[pick]]).T

    dx1, dx2, dx3, dx4 = [face_location[pick, i] for i in range(4)]

    w = x2 - x1
    h = y2 - y1

    pts0 = np.array([(w * landmak[pick, 0] + x1)[0]]).T
    pts1 = np.array([(h * landmak[pick, 5] + y1)[0]]).T

    pts2 = np.array([(w * landmak[pick, 1] + x1)[0]]).T
    pts3 = np.array([(h * landmak[pick, 6] + y1)[0]]).T

    pts4 = np.array([(w * landmak[pick, 2] + x1)[0]]).T
    pts5 = np.array([(h * landmak[pick, 7] + y1)[0]]).T

    pts6 = np.array([(w * landmak[pick, 3] + x1)[0]]).T
    pts7 = np.array([(h * landmak[pick, 8] + y1)[0]]).T

    pts8 = np.array([(w * landmak[pick, 4] + x1)[0]]).T
    pts9 = np.array([(h * landmak[pick, 9] + y1)[0]]).T

    x1 = np.array([(x1 + dx1 * w)[0]]).T
    y1 = np.array([(y1 + dx2 * h)[0]]).T
    x2 = np.array([(x2 + dx3 * w)[0]]).T
    y2 = np.array([(y2 + dx4 * h)[0]]).T

    rectangles = np.concatenate((x1, y1, x2, y2, sc, pts0, pts1, pts2, pts3, pts4, pts5, pts6, pts7, pts8, pts9),
                                axis=1)
    newBox = NMS(rectangles, 0.3)
    return newBox

# 变成正方形
def change_box(box):
    """
        function:将候选框变成正方形 将原来的框包裹
        parameters: boxe候选框
        return:候选框
    """
    newBox = box.copy()  # 复制一份框   原框还需要使用
    if box.shape[0] == 0:  # 如果没有框
        return np.array([])
    h = box[:, 3] - box[:, 1] # 计算宽高
    w = box[:, 2] - box[:, 0]

    max_side = np.maximum(w, h)  # 找到最长边  # 扩边  按照长边扩  将原框包含在里面
    newBox[:, 0] = newBox[:, 0] + w * 0.5 - max_side * 0.5 # 获取左上角的坐标 再+最大边max_size完成方框
    newBox[:, 1] = newBox[:, 1] + h * 0.5 - max_side * 0.5
    newBox[:, 2] = newBox[:, 0] + max_side
    newBox[:, 3] = newBox[:, 1] + max_side
    return newBox

def face_align(img, landmark):
    """
    人脸对齐
    :param img:
    :param landmark:
    :return:
    """
    x = landmark[1][0] - landmark[0][0]
    y = landmark[1][1] - landmark[0][1]
    if x == 0:
        angle = 0
    else:
        angle = math.atan(y / x) * 180 / math.pi
    center = (img.shape[1] // 2, img.shape[0] // 2)
    RotationMatrix = cv2.getRotationMatrix2D(center, angle, 1)
    new_img = cv2.warpAffine(img, RotationMatrix, (img.shape[1], img.shape[0]))
    return new_img



def pre_process(x):
    """
    图片预处理
    高斯归一化
    :param x:
    :return:
    """
    if x.ndim == 4:
        axis = (1, 2, 3)
        size = x[0].size
    elif x.ndim == 3:
        axis = (0, 1, 2)
        size = x.size
    else:
        raise ValueError('Dimension should be 3 or 4')

    mean = np.mean(x, axis=axis, keepdims=True)
    std = np.std(x, axis=axis, keepdims=True)
    std_adj = np.maximum(std, 1.0 / np.sqrt(size))
    y = (x - mean) / std_adj
    return y


def l2_normalize(x, axis=-1, epsilon=1e-10):
    """
    l2标准化
    :param x:
    :param axis:
    :param epsilon:
    :return:
    """
    output = x / np.sqrt(np.maximum(np.sum(np.square(x), axis=axis, keepdims=True), epsilon))
    return output


def calc_128_vec(model, img):
    """
    计算128特征值
    :param model:
    :param img:
    :return:
    """
    face_img = pre_process(img)
    pre = model.predict(face_img)
    pre = l2_normalize(np.concatenate(pre))
    pre = np.reshape(pre, [128])
    return pre

def face_distance(face_encodings, face_to_compare):
    """
    计算人脸距离
    :param face_encodings:
    :param face_to_compare:
    :return:
    """
    if len(face_encodings) == 0:
        return 0
    # return np.linalg.norm(face_encodings - face_to_compare, axis=0)
    return np.sqrt(np.sum(np.asarray(face_encodings - face_to_compare)**2, axis=0))

def compare_faces(known_face_encodings, face_encoding_to_check, tolerance=0.6):
    """
    比较人脸
    :param known_face_encodings:
    :param face_encoding_to_check:
    :param tolerance:
    :return:
    """
    dis = face_distance(known_face_encodings, face_encoding_to_check)
    return dis<=tolerance,dis
