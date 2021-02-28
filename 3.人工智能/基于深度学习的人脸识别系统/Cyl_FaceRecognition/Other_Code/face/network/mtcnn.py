from tensorflow.keras.layers import Conv2D, Input,MaxPool2D,Flatten, Dense, Permute
from tensorflow.keras.layers import PReLU
from tensorflow.keras.models import Model
# from tensorflow.keras import layers


def create_Pnet(weight_path):
    """
    论文原论文创建p-net
    :param weight_path:
    :return:
    """
    input = Input(shape=[None, None, 3])  # 传入大小不固定的照片

    x = Conv2D(10, (3, 3), strides=1, padding='valid', name='conv1')(input)
    x = PReLU(shared_axes=[1,2],name='PReLU1')(x)
    x = MaxPool2D(pool_size=2)(x)

    x = Conv2D(16, (3, 3), strides=1, padding='valid', name='conv2')(x)
    x = PReLU(shared_axes=[1,2],name='PReLU2')(x)

    x = Conv2D(32, (3, 3), strides=1, padding='valid', name='conv3')(x)
    x = PReLU(shared_axes=[1,2],name='PReLU3')(x)

    classifier = Conv2D(2, (1, 1), activation='softmax', name='conv4-1')(x)

    bbox_regress = Conv2D(4, (1, 1), name='conv4-2')(x)

    model = Model([input], [classifier, bbox_regress])
    model.load_weights(weight_path, by_name=True)
    return model

#-----------------------------#
#   mtcnn的第二段
#   精修框
#-----------------------------#
def create_Rnet(weight_path):
    """
    论文原论文创建r-net
    :param weight_path:
    :return:
    """
    input = Input(shape=[24, 24, 3])

    x = Conv2D(28, (3, 3), strides=1, padding='valid', name='conv1')(input) # 卷积层  提取特征

    x = PReLU(shared_axes=[1, 2], name='prelu1')(x) # 激励层

    x = MaxPool2D(pool_size=3,strides=2, padding='same')(x) # 池化层 提取特征

    x = Conv2D(48, (3, 3), strides=1, padding='valid', name='conv2')(x)
    x = PReLU(shared_axes=[1, 2], name='prelu2')(x)
    x = MaxPool2D(pool_size=3, strides=2)(x)

    x = Conv2D(64, (2, 2), strides=1, padding='valid', name='conv3')(x)
    x = PReLU(shared_axes=[1, 2], name='prelu3')(x)
    x = Permute((3, 2, 1))(x)  #改变维度
    x = Flatten()(x)
    x = Dense(128, name='conv4')(x)
    x = PReLU( name='prelu4')(x)
    classifier = Dense(2, activation='softmax', name='conv5-1')(x)
    bbox_regress = Dense(4, name='conv5-2')(x)
    model = Model([input], [classifier, bbox_regress])
    model.load_weights(weight_path, by_name=True)
    return model

#-----------------------------#
#   mtcnn的第三段
#   精修框并获得五个点
#-----------------------------#
def create_Onet(weight_path):
    """
    论文原论文创建o-net
    :param weight_path:
    :return:
    """
    input = Input(shape = [48,48,3])
    x = Conv2D(32, (3, 3), strides=1, padding='valid', name='conv1')(input)
    x = PReLU(shared_axes=[1,2],name='prelu1')(x)
    x = MaxPool2D(pool_size=3, strides=2, padding='same')(x)
    x = Conv2D(64, (3, 3), strides=1, padding='valid', name='conv2')(x)
    x = PReLU(shared_axes=[1,2],name='prelu2')(x)
    x = MaxPool2D(pool_size=3, strides=2)(x)
    x = Conv2D(64, (3, 3), strides=1, padding='valid', name='conv3')(x)
    x = PReLU(shared_axes=[1,2],name='prelu3')(x)
    x = MaxPool2D(pool_size=2)(x)
    x = Conv2D(128, (2, 2), strides=1, padding='valid', name='conv4')(x)
    x = PReLU(shared_axes=[1,2],name='prelu4')(x)
    x = Permute((3,2,1))(x)

    x = Flatten()(x)
    x = Dense(256, name='conv5') (x)
    x = PReLU(name='prelu5')(x)

    classifier = Dense(2, activation='softmax',name='conv6-1')(x)
    bbox_regress = Dense(4,name='conv6-2')(x)
    landmark_regress = Dense(10,name='conv6-3')(x)

    model = Model([input], [classifier, bbox_regress, landmark_regress])
    model.load_weights(weight_path, by_name=True)

    return model



