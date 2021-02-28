import time

from django.core.paginator import Paginator
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render
import numpy as np
from APP_BasicInfo.models import InfoStudent, InfoTeacher, InfoAdmin, InfoClass, InfoCollege, InfoSpecialty, InfoCourse, \
    InfoTeCour, InfoChoose, InfoFacecode
from APP_ImportData.models import InfoFilesBeaseMessage
from Other_Code.face.utils.utils import compare_faces
from Other_Code.view_utils import view_utils as utils
from Other_Code.face.utils import utils
from Cyl_FaceRecognition.settings import FACE_CLASS as face, CAMERA_IP
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
import pandas as pa
import os
import cv2

import traceback
# from Cyl_FaceRecognition.settings import BASE_DIR

# 上传信息 静态变量
from Other_Code.view_utils.view_utils import try_log

UP_INFO = {
    'col': {
        'co_id': '学院号',
        'co_name': '学院名',
    },
    'stu': {
        'st_id': '学号',
        'st_name': '姓名',
        'st_age': '年龄',
        'st_sex': '性别',
        'st_phone': '手机号',
        'st_email': '邮箱',
        'st_pic_path': 'img/head_portrait/student/morentouxiang.jpg',  # 该字段在此处无效
        'st_login_id': '登陆账号',
        'st_passwd': '123',
        'cl_id': '班级',
    },
    'tea': {
        'te_id': '教师编号',
        'te_name': '姓名',
        'te_age': '年龄',
        'te_sex': '性别',
        'te_phone': '手机号',
        'te_email': '邮箱',
        'te_pic_path': 'img/head_portrait/teacher/morentouxiang.jpg',  # 该字段在此处无效
        'te_login_id': '登陆账号',
        'te_passwd': '123',
    },
    'spe': {
        'sp_id': '专业号',
        'sp_name': '专业名',
        'co_id': '学院名',  # 数据库字段存的时学院id 上传的表使用的时学院名
    },
    'cla': {
        'cl_id': '班级号',
        'cl_grade': '年级',  # 这里使用字符串切割
        'cl_number': '班级',
        'cl_name': '班级',
        'sp_id': '专业',
        'te_id': '班主任',  # 存id
    },
    'cou':{
        'cour_id':'课程号',
        'cour_name':'课程名',
        'cour_credit':'学分',
    },
    'tecu':{
        'te_co_id':'排课号',
        'te_id':'教师编号',
        'cour_id':'课程号',
        'time':'时间',
        'week':'起止周',
        'te_class':'教学班',
    },
}




# from django.db import transaction
#
# @transaction.atomic


# Create your views here.
def skip_import(request):
    inf = request.session['inf']
    if inf != 'admin':
        data = request.session['data']
        data['nav_path']['nav_path_one'] = '主页'
        data['userinfo'] = 'admin'
        return render(request, 'skip_welcome.html', context=data)
    return render(request, 'skip_import.html')


def manageFiles(fid, fname):
    """
    上传excel
    :param fid:操作者的ID
    :param fname: 文件名
    :return:excel数据
    """
    if fname:
        infostudent = InfoFilesBeaseMessage()

        infostudent.admin_number = fid
        infostudent.file_path = fname
        infostudent.save()
        studentpath = infostudent.file_path
        path = 'static/upload\\' + str(studentpath)
        da = pa.read_excel(path)
        os.remove(path)
        infostudent.delete()
        return True, da
    return False, ''


def dict_flag():
    """
    定义上传标志
    :return:
    """
    file_flag = {
        'college_flag': '',
        'student_flag': '',
        'teacher_flag': '',
        'admin_flag': '',
        'class_flag': '',
        'course_flag': '',
        'course_table_flag': '',
        'info_flag': '',
        'error_flag': '',
    }
    return file_flag


def import_info(id, flag, info):
    """
    插入信息提示函数
    :param id: 代表时哪个类别的信息
    :param info: 具体信息内容
    :param flag: 信息代码
    :return: 返回整个标志字典
    """
    file_flag = dict_flag()
    file_flag[id] = info
    file_flag['error_flag'] = flag
    return file_flag


def college_info(request):
    """
    添加学院信息
    :param request:
    :return:
    """
    fid = 'college'  # 该字段时无用字段
    fname = request.FILES.get('college_file')
    fl, ds = manageFiles(fid, fname)
    if fl:  # 文件是否上传成功
        if UP_INFO['col']['co_id'] in ds.columns.values:  # 校验文件中字段是否匹配
            try:
                with transaction.atomic():
                    for li in ds.iterrows():
                        li = li[1]
                        db = InfoCollege()
                        try:
                            db = InfoCollege.objects.get(co_id=li[UP_INFO['col']['co_id']])  # 查看源库是否存在 存在则做修改
                        except Exception as ex:

                            pass

                        db.co_id = li[UP_INFO['col']['co_id']]
                        db.co_name = li[UP_INFO['col']['co_name']]
                        db.save()
                data = import_info("info_flag", "0", "数据导入成功")
                return JsonResponse(data=data)
            except Exception as e:
                print('数据存在错误')
                data = import_info("info_flag", "1", "数据存在错误")
                return JsonResponse(data=data)

        else:
            data = import_info("info_flag", "1", "文件内容格式错误")
            print('文件内容格式错误')
            return JsonResponse(data=data)
    else:
        data = import_info("info_flag", "1", "文件上传失败")
        print('文件上传失败')
        return JsonResponse(data=data)


def admin_info(request):
    """
    添加管理员信息
    :param request:
    :return:
    """
    file_flag = dict_flag()
    admin_number = request.POST.get('admin_number')
    admin_passwd = request.POST.get('admin_passwd')
    try:
        InfoAdmin.objects.get(admin_number=admin_number)
        data = import_info("info_flag", "1", "管理员存在")
        print('管理员存在')
        return JsonResponse(data=data)
    except Exception as e:
        with transaction.atomic():
            try:
                adinfo = InfoAdmin()
                adinfo.admin_number = admin_number
                adinfo.admin_passwd = admin_passwd
                adinfo.save()
                data = import_info("info_flag", "0", "添加成功")
                print('添加成功')
                return JsonResponse(data=data)
            except Exception as ex:
                data = import_info("info_flag", "1", "添加出错")
                print('添加出错')
                return JsonResponse(data=data)


def teacher_info(request):
    """
    添加教师信息
    :param request:
    :return:
    """
    fid = 'teacher'  # 该字段时无用字段
    fname = request.FILES.get('teacher_file')
    fl, ds = manageFiles(fid, fname)
    if fl:  # 文件是否上传成功
        info = UP_INFO['tea']
        if info['te_id'] in ds.columns.values:  # 校验文件中字段是否匹配
            with transaction.atomic():
                try:
                    for li in ds.iterrows():
                        li = li[1]
                        db = InfoTeacher()
                        try:
                            db = InfoTeacher.objects.get(te_id=li[info['te_id']])  # 查看源库是否存在 存在则做修改
                        except Exception as ex:
                            pass
                        db.te_id = li[info['te_id']]
                        db.te_name = li[info['te_name']]
                        db.te_age = li[info['te_age']]
                        db.te_sex = li[info['te_sex']]
                        db.te_phone = li[info['te_phone']]
                        db.te_email = li[info['te_email']]
                        db.te_login_id = li[info['te_id']]
                        db.te_pic_path = info['te_pic_path']
                        db.te_passwd = info['te_passwd']
                        db.save()
                    data = import_info("info_flag", "0", "数据导入成功")
                    return JsonResponse(data=data)
                except Exception as e:
                    print('数据存在错误')
                    data = import_info("info_flag", "1", "数据存在错误")
                    return JsonResponse(data=data)
        else:
            data = import_info("info_flag", "1", "文件内容格式错误")
            print('文件内容格式错误')
            return JsonResponse(data=data)
    else:
        data = import_info("info_flag", "1", "文件上传失败")
        print('文件上传失败')
        return JsonResponse(data=data)


def specialty_info(request):
    """
    添加专业信息
    :param request:
    :return:
    """
    fid = 'specilaty'  # 该字段时无用字段
    fname = request.FILES.get('specialty_file')
    fl, ds = manageFiles(fid, fname)
    if fl:  # 文件是否上传成功
        info = UP_INFO['spe']
        if info['sp_id'] in ds.columns.values:  # 校验文件中字段是否匹配
            with transaction.atomic():
                try:
                    for li in ds.iterrows():
                        li = li[1]
                        db = InfoSpecialty()
                        try:
                            db = InfoSpecialty.objects.get(sp_id=li[info['sp_id']])  # 查看源库是否存在 存在则做修改
                        except Exception as ex:
                            pass
                        db.sp_id = li[info['sp_id']]
                        db.sp_name = li[info['sp_name']]
                        try:
                            cl_db = InfoCollege.objects.get(co_name=li[info['co_id']])
                            db.co_id = cl_db.co_id
                            db.save()
                        except Exception as es:
                            print(f"sp_id该班级不存在")
                            data = import_info("info_flag", "1", "班级不存在，请先插入班级")
                            return JsonResponse(data=data)
                    data = import_info("info_flag", "0", "数据导入成功")
                    return JsonResponse(data=data)
                except Exception as e:
                    print('数据存在错误')
                    data = import_info("info_flag", "1", "数据存在错误")
                    return JsonResponse(data=data)
        else:
            data = import_info("info_flag", "1", "文件内容格式错误")
            print('文件内容格式错误')
            return JsonResponse(data=data)
    else:
        data = import_info("info_flag", "1", "文件上传失败")
        print('文件上传失败')
        return JsonResponse(data=data)


def class_info(request):
    """
    添加班级信息
    :param request:
    :return:
    """
    fid = 'class'  # 该字段时无用字段
    fname = request.FILES.get('class_file')
    fl, ds = manageFiles(fid, fname)
    if fl:  # 文件是否上传成功
        info = UP_INFO['cla']
        if info['cl_id'] in ds.columns.values:  # 校验文件中字段是否匹配
            with transaction.atomic():
                try:
                    for li in ds.iterrows():
                        li = li[1]
                        db = InfoClass()
                        try:
                            db = InfoClass.objects.get(cl_id=li[info['cl_id']])
                        except Exception as e:
                            pass

                        db.cl_id = li[info['cl_id']]
                        db.cl_grade = li[info['cl_grade']]
                        clname = li[info['cl_name']]
                        db.cl_number = clname[-1]  # 切割最后一个数字 第几班
                        db.cl_name = clname  # 班级全称
                        try:
                            sp_db = InfoSpecialty.objects.get(sp_name=li[info['sp_id']])
                            db.sp_id = sp_db.sp_id
                        except Exception as er:
                            data = import_info("info_flag", "1", "专业不存在，请先插入专业")
                            return JsonResponse(data=data)
                        try:
                            te_db = InfoTeacher.objects.get(te_id=li[info['te_id']])
                            db.te_id = li[info['te_id']]
                        except Exception as et:
                            try_log()
                            data = import_info("info_flag", "1", "教师不存在，请先插入教师")
                            return JsonResponse(data=data)
                        db.save()
                    data = import_info("info_flag", "0", "数据导入成功")
                    return JsonResponse(data=data)
                except Exception as e:
                    try_log()
                    data = import_info("info_flag", "1", "数据存在错误")
                    return JsonResponse(data=data)
        else:
            data = import_info("info_flag", "1", "文件内容格式错误")
            return JsonResponse(data=data)
    else:
        data = import_info("info_flag", "1", "文件上传失败")
        return JsonResponse(data=data)

def student_info(request):
    fid = 'student'  # 该字段时无用字段
    fname = request.FILES.get('student_file')
    fl, ds = manageFiles(fid, fname)
    if fl:  # 文件是否上传成功
        info = UP_INFO['stu']
        if info['st_id'] in ds.columns.values:  # 校验文件中字段是否匹配
            try:
                with transaction.atomic():
                    for li in ds.iterrows():
                        li = li[1]
                        db = InfoStudent()
                        try:
                            db = InfoStudent.objects.get(st_id=li[info['st_id']])  # 查看源库是否存在 存在则做修改
                        except Exception as ex:
                            pass
                        db.st_id = li[info['st_id']]
                        db.st_name = li[info['st_name']]
                        db.st_age = li[info['st_age']]
                        db.st_sex = li[info['st_sex']]
                        db.st_phone = li[info['st_phone']]
                        db.st_email = li[info['st_email']]
                        db.st_login_id = li[info['st_id']]
                        db.st_passwd = info['st_passwd']
                        db.st_pic_path = info['st_pic_path']
                        try:
                            cl = InfoClass.objects.get(cl_name=li[info['cl_id']])
                            db.cl_id = cl.cl_id
                            db.save()
                        except Exception as e:
                            try_log()
                            data = import_info('info_flag', '1',"班级信息不正确")
                            return JsonResponse(data=data)
                    data = import_info("info_flag", "0", "数据导入成功")
                    return JsonResponse(data=data)
            except Exception as e:
                try_log()
                data = import_info("info_flag", "1", "数据存在错误")
                return JsonResponse(data=data)
        else:
            data = import_info("info_flag", "1", "文件内容格式错误")
            return JsonResponse(data=data)
    else:
        data = import_info("info_flag", "1", "文件上传失败")
        return JsonResponse(data=data)



def course_info(request):
    """
    课程插入
    :param request:
    :return:
    """
    fid = 'course'  # 该字段时无用字段
    fname = request.FILES.get('course_file')
    fl, ds = manageFiles(fid, fname)
    if fl:  # 文件是否上传成功
        info = UP_INFO['cou']
        if info['cour_id'] in ds.columns.values:  # 校验文件中字段是否匹配
            try:
                with transaction.atomic():
                    for li in ds.iterrows():
                        li = li[1]
                        db = InfoCourse()
                        try:
                            db = InfoCourse.objects.get(cour_id=li[info['cour_id']])  # 查看源库是否存在 存在则做修改
                        except Exception as ex:
                            pass
                        db.cour_id = li[info['cour_id']]
                        db.cour_name = li[info['cour_name']]
                        db.cour_credit = li[info['cour_credit']]
                        db.save()
                    data = import_info("info_flag", "0", "数据导入成功")
                    return JsonResponse(data=data)
            except Exception as e:
                try_log()
                data = import_info("info_flag", "1", "数据存在错误")
                return JsonResponse(data=data)
        else:
            data = import_info("info_flag", "1", "文件内容格式错误")
            return JsonResponse(data=data)
    else:
        data = import_info("info_flag", "1", "文件上传失败")
        return JsonResponse(data=data)


def course_table(request):
    """
    课程表插入
    :param request:
    :return:
    """
    fid = 'course_table'  # 该字段时无用字段
    fname = request.FILES.get('course_table_file')
    fl, ds = manageFiles(fid, fname)
    llii=[]
    if fl:  # 文件是否上传成功
        info = UP_INFO['tecu']
        if info['te_co_id'] in ds.columns.values:  # 校验文件中字段是否匹配
            try:
                with transaction.atomic():
                    for li in ds.iterrows():
                        li = li[1]
                        db = InfoTeCour()
                        try:
                            db = InfoTeCour.objects.get(te_co_id=li[info['te_co_id']])  # 查看源库是否存在 存在则做修改
                        except Exception as ex:
                            pass
                        db.te_co_id = li[info['te_co_id']]
                        db.te_id = li[info['te_id']]
                        db.cour_id = li[info['cour_id']]
                        tim = str(li[info['time']])
                        wee = str(li[info['week']])
                        week = wee.split('-')
                        db.begin_time = week[0]
                        db.end_time = week[1]
                        db.specific = tim
                        db.save()
                    # 下面是教学班级
                        cl_list = str(li[info['te_class']])
                        cl_list = cl_list.split(';')
                        llii.append([cl_list,li[info['te_co_id']]])

                    for il in llii:
                        dd = il[1]

                        for c in il[0]:
                            clid = InfoClass.objects.get(cl_name=c)
                            clid = clid.cl_id
                            stid = InfoStudent.objects.filter(cl_id=clid).distinct().values('st_id')
                            for si in stid:
                                chdb = InfoChoose()
                                try:
                                    chdb = InfoChoose.objects.filter(te_co_id=dd).get(st_id=si['st_id'])  # 查看源库是否存在 存在则做修改
                                except Exception as ee:
                                    pass
                                chdb.st_id = si['st_id']
                                chdb.te_co_id = dd
                                chdb.truant_number = 0
                                chdb.leave_number = 0
                                chdb.belate_number = 0
                                chdb.all_number = 0
                                chdb.score = 0
                                chdb.save()

                    # for cl_li in cl_list:
                    #     clid = InfoClass.objects.get(cl_name=cl_li)
                    #     clid = clid.cl_id
                    #     stid = InfoStudent.objects.filter(cl_id=clid).values('st_id')
                    #     for si in stid:
                    #         chdb = InfoChoose()
                    #         chdb.st_id = si['st_id']
                    #         chdb.te_co_id = li[info['te_co_id']]
                    #         chdb.truant_number=0
                    #         chdb.leave_number=0
                    #         chdb.belate_number=0
                    #         chdb.score=0
                    #         chdb.save()
                    data = import_info("info_flag", "0", "数据导入成功")
                    return JsonResponse(data=data)
            except Exception as e:
                try_log()
                data = import_info("info_flag", "1", "数据存在错误")
                return JsonResponse(data=data)
        else:
            data = import_info("info_flag", "1", "文件内容格式错误")
            return JsonResponse(data=data)
    else:
        data = import_info("info_flag", "1", "文件上传失败")
        return JsonResponse(data=data)



def face_gather(request):
    """
    跳转到人脸数据采集
    :param request:
    :return:
    """
    inf = request.session['inf']
    data = {}
    if inf != 'admin':
        data = request.session['data']
        data['nav_path']['nav_path_one'] = '主页'
        data['userinfo'] = 'admin'
        return render(request, 'skip_welcome.html', context=data)
    data['ip'] = data['ip'] = CAMERA_IP
    return render(request, 'face_gather.html', context=data)


def class_info_face(request):
    """
    提交班级一边查询信息
    :param request:
    :return:
    """
    dada = {"index": [],
            "err": '0',
            "img_path": '',
            "stu_name": '',
            "stu_id":'',
            }
    flag = request.POST.get('info_flag')

    try:
        if flag == '1':
            d = InfoCollege.objects.all().values('co_name')
            for s in d:
                dada['index'].append(s['co_name'])  # 加载学院
        elif flag == '2':
            index = request.POST.get('index1')  # 获得传上来的学院名
            co_id = InfoCollege.objects.get(co_name=index).co_id
            d = InfoSpecialty.objects.filter(co_id=co_id).values('sp_name')
            for s in d:
                dada['index'].append(s['sp_name'])
        elif flag == '3':
            index1 = request.POST.get('index1')
            index2 = request.POST.get('index2')
            sp_id = InfoSpecialty.objects.get(sp_name=index2).sp_id
            d = InfoClass.objects.filter(sp_id=sp_id).values('cl_name')
            for s in d:
                dada['index'].append(s['cl_name'])
        elif flag == '4':
            index3 = request.POST.get('index3')
            try:
                classid = InfoClass.objects.get(cl_name=index3).cl_id
                stu_db = InfoStudent.objects.filter(cl_id=classid).order_by('st_id')
                st_db = stu_db.first()
                dada['stu_id'] = st_db.st_id
                dada['stu_name'] = st_db.st_name
                dada['img_path'] = st_db.st_pic_path
                request.session['stu_id'] = dada['stu_id']
                request.session['class_id'] = classid
                lli = stu_db.values()
                dd=[]
                for l in lli:
                    dd.append([l['st_pic_path'],l['st_id'],l['st_name'],index3])
                dada['dd']=dd

            except Exception as ex:
                try_log()
                dada['err'] = '1'
    except Exception as e:
        try_log()
        dada['err'] = '1'
    return JsonResponse(data=dada)


def cloose_stu(request):
    dada = {"index": [],
            "err": '0',
            "img_path": '',
            "stu_id": '',
            "stu_name": '',
            }
    face_encoding = ''

    flag = request.POST.get('info_flag')
    stuid = ''
    classid = ''
    st_pic_path = ''
    stu_name = ''
    try:
        stuid = request.session['stu_id']
        classid = request.session['class_id']
        stu_name = request.session['stu_name']
        st_pic_path = request.session['st_pic_path']
    except Exception as ee:
        try_log()
        dada['err'] = '0'

    img_path = st_pic_path
    db = InfoStudent.objects.all()
    if flag == '0' or flag == '1':
        try:
            if flag == '0':
                stuid = str(int(stuid) - 1)
            elif flag == '1':
                stuid = str(int(stuid) + 1)
            try:
                db = db.filter(cl_id=classid).get(st_id=stuid)
            except Exception as d:
                pass
            dada['img_path'] = db.st_pic_path
            dada['stu_name'] = db.st_name
            dada['stu_id'] = db.st_id
            request.session['stu_id'] = db.st_id
            request.session['stu_name'] = db.st_name
            request.session['st_pic_path'] = db.st_pic_path

        except Exception as e:
            try_log()
            dada['err'] = '1'

    elif flag == '2':
        try:
            camp = cv2.VideoCapture(CAMERA_IP)
            ret, frame = camp.read()
            path = f'static/face/face_coding_img/{classid}/{stuid}'
            if not os.path.exists(path):
                os.makedirs(path)
            path = f'{path}/{stuid}.jpg'
            cv2.imwrite(path, frame)

            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            box = face[0].faceDecognition(img)
            box = utils.change_box(np.array(box))

            for bo in box:
                face_img = img[int(bo[1]):int(bo[3]), int(bo[0]):int(bo[2])]
                face_encoding = face[1].face_encoding(face_img, bo)
                print(face_encoding)

                db = InfoFacecode.objects.get(st_id=stuid)
                db.face_encoding=face_encoding
                db.save()
            if face_encoding!='':
                pa = f'face/face_coding_img/{classid}/{stuid}/{stuid}.jpg'
                sdb = InfoStudent.objects.get(st_id=stuid)
                sdb.st_pic_path=pa
                sdb.save()

                dada['err'] = '3'
                img_path = pa
                print('拍照成功')
            else:
                print('人像获取不成功')
                dada['err'] = '2'

            cv2.waitKey(0)
            camp.release()
            dada['img_path'] = img_path
            dada['stu_id'] = stuid
            dada['stu_name'] = stu_name
        except Exception as er:
            try_log()
            dada['err'] = '2'

    return JsonResponse(data=dada)


def fy(request,id):
    classid = id  # 这里会有异常 后期处理
    page = 1  # int(request.GET.get(('page'), 1))
    per_page = 5  # int(request.GET.get(('per_page'), 10))
    classname = InfoClass.objects.get(cl_id=classid).cl_name  # 这里也有异常
    students = InfoStudent.objects.all().order_by('st_id')
    paglater = Paginator(students, per_page)  # 设置页码
    page_ob = paglater.page(page)  # 查出来的第几页的一个对象
    stuinf = {}
    stulist = []
    for inf in page_ob:
        stuinf['st_id'] = inf.st_id
        stuinf['st_name'] = inf.st_name
        stuinf['cl_id'] = classname
        stulist.append(stuinf)
    data = {
        'page_ob': stulist,
        'page_range': list(paglater.page_range),  # 页码表
        'num_pages': paglater.num_pages,
    }
    print(data)

def fenye(request):
    classid = request.session['class_id']  # 这里会有异常 后期处理
    page = 1  # int(request.GET.get(('page'), 1))
    per_page = 5  # int(request.GET.get(('per_page'), 10))
    classname = InfoClass.objects.get(class_id=classid).class_name  # 这里也有异常
    students = InfoStudent.objects.all().order_by('stu_id')
    paglater = Paginator(students, per_page)  # 设置页码
    page_ob = paglater.page(page)  # 查出来的第几页的一个对象
    stuinf = {}
    stulist = []
    for inf in page_ob:
        stuinf['stu_id'] = inf.stu_id
        stuinf['stu_name'] = inf.stu_name
        stuinf['class_id'] = classname
        stulist.append(stuinf)
    data = {
        'page_ob': stulist,
        'page_range': list(paglater.page_range),  # 页码表
        'num_pages': paglater.num_pages,
    }
    print(data)

    return JsonResponse(data=data)
