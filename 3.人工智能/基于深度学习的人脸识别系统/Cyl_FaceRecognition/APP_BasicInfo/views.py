import os
import shutil
import time

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from APP_BasicInfo.models import InfoCheck, InfoChoose, InfoTeCour, InfoCourse, InfoRule, InfoStudent, InfoTeacher, \
    InfoAdmin
from Other_Code.view_utils.view_utils import try_log
import matplotlib.pyplot as plt


login_flag = 0

def clear_session(request):
    print('***********')
    try:
        del request.session['page']
        del request.session['class_id']
        del request.session['te_co_id']
        del  request.session['list']
        del  request.session['stidlist']
        del  request.session['collinfo']

    except Exception as e:
        try_log()
    return JsonResponse(data={})


def creat_legend(lendb_0, lendb_1, lendb_2, lendb_3,value_kc1,id,inf,score):
    tim = time.time()
    plt.rcParams['font.sans-serif'] = 'SimHei'  # 设置中文显示
    plt.figure(figsize=(6, 6))  # 将画布设定为正方形，则绘制的饼图是正圆

    label = ['出勤', '请假', '迟到', '缺勤']  # 定义饼图的标签，标签是列表
    explode = [0.01, 0.01, 0.01, 0.05]  # 设定各项距离圆心n个半径
    values = [lendb_0, lendb_1, lendb_2, lendb_3]
    # plt.subplot(223, axisbg='#FF7F50')

    plt.pie(values, explode=explode, labels=label, autopct='%1.1f%%')  # 绘制饼图
    plt.title(id+value_kc1+'-得分：'+str(score))  # 绘制标题

    path = f'static/img/legend/{inf}/{id}'
    try:
        shutil.rmtree(path)
        os.mkdir('path')
    except Exception as e:
        try_log()
    if not os.path.exists(path):
        os.makedirs(path)
    path = f'{path}/legend_{tim}.jpg'
    plt.savefig(path)  # 保存图片
    # plt.show()
    return path


def show_stud(request):
    data = {}
    collinfo = []
    list = []
    data_sess = request.session['data']
    id = data_sess['unum']  # 获得自己的学号
    choodb = InfoChoose.objects.filter(st_id=id)
    kc = choodb.values('te_co_id')
    for tid in kc:
        toid = tid['te_co_id']
        tecoddb = InfoTeCour.objects.get(te_co_id=toid)
        courid = tecoddb.cour_id
        coname = InfoCourse.objects.get(cour_id=courid).cour_name
        list.append(coname)
        collinfo.append([toid, coname])
    request.session['collinfo'] = collinfo
    data['list'] = list

    return JsonResponse(data=data)



def show_tb1(request):

    data = {}
    data_sess = request.session['data']
    id = data_sess['unum']  # 获得自己的学号
    name = data_sess['uname']  # 获得自己的姓名
    value_kc1 = request.POST.get('value_kc1')
    collinfo = request.session['collinfo']
    inf = request.session['inf']
    te_co_id = 0
    if value_kc1 != '请选择课程':
        for li in collinfo:
            if li[1] == value_kc1:
                te_co_id = li[0]
                break
    db = InfoCheck.objects.filter(st_id=id).filter(te_co_id=te_co_id)

    lendb_all = len(db)  # 获取所有次数
    db_0 = db.filter(state=0)
    lendb_0 = len(db_0)

    db_1 = db.filter(state=1)
    lendb_1 = len(db_1)

    db_2 = db.filter(state=2)
    lendb_2 = len(db_2)

    db_3 = db.filter(state=3)
    lendb_3 = len(db_3)

    path = ''
    if lendb_all>0:
        rule = InfoRule.objects.first()
        attendance = rule.attendance
        absent = rule.absent
        late = rule.late
        leave = rule.leave
        absent_number = rule.absent_number
        late_number = rule.late_number

        core = InfoChoose.objects.filter(st_id=id).filter(te_co_id=te_co_id).first()

        fl = 1
        if lendb_2>=late_number:
            s = lendb_2/late_number
            lendb_3 = lendb_3+s
            lendb_2 = lendb_2%late_number
            pass
        if lendb_3>=absent_number:
            fl = 0
        score = ((lendb_0 * attendance + lendb_1 * leave + lendb_2 * late + lendb_3 * absent)*fl) / lendb_all
        score = round(score,2)
        core.score = score
        core.save()
        path = creat_legend(lendb_0, lendb_1, lendb_2, lendb_3, value_kc1, id, inf,score)
    data['path'] = path

    return JsonResponse(data=data)


def show_ted(request):
    data = {}
    li1 = []
    li2 = []
    courinfo = []
    data_sess = request.session['data']
    id = data_sess['unum']
    tecodb = InfoTeCour.objects.filter(te_id=id)
    te_co_id_db = tecodb.values('te_co_id')
    for tecoid in te_co_id_db:
        te_co_id = tecoid['te_co_id']
        tecoddb = InfoTeCour.objects.get(te_co_id=te_co_id)
        courid = tecoddb.cour_id
        coname = InfoCourse.objects.get(cour_id=courid).cour_name
        courinfo.append([te_co_id, coname])
        li1.append(coname)

    data['li1'] = li1
    request.session['courinfo'] = courinfo

    return JsonResponse(data=data)


def creat_legend1(lendb_0, lendb_1, lendb_2, lendb_3,value_kc1,id,inf):
    tim = time.time()
    plt.rcParams['font.sans-serif'] = 'SimHei'  # 设置中文显示
    plt.figure(figsize=(6, 6))  # 将画布设定为正方形，则绘制的饼图是正圆

    label = ['出勤', '请假', '迟到', '缺勤']  # 定义饼图的标签，标签是列表
    explode = [0.01, 0.01, 0.01, 0.05]  # 设定各项距离圆心n个半径
    values = [lendb_0, lendb_1, lendb_2, lendb_3]
    # plt.subplot(223, axisbg='#FF7F50')

    plt.pie(values, explode=explode, labels=label, autopct='%1.1f%%')  # 绘制饼图
    plt.title(value_kc1+'全部学生考勤情况')  # 绘制标题

    path = f'static/img/legend/{inf}/{id}'
    try:
        shutil.rmtree(path)
        os.mkdir('path')
    except Exception as e:
        try_log()

    if not os.path.exists(path):
        os.makedirs(path)
    path = f'{path}/legend_{tim}.jpg'
    plt.savefig(path)  # 保存图片
    # plt.show()
    return path


def show_te_std(request):
    data = {}
    list = []
    li = []
    data_sess = request.session['data']
    id = data_sess['unum']  # 获得自己的学号
    name = data_sess['uname']  # 获得自己的姓名
    courinfo = request.session['courinfo']
    value_kc1 = request.POST.get('value_kc1')
    inf = request.session['inf']
    te_co_id = 0
    if value_kc1 != '请选择课程':
        for li in courinfo:
            if li[1] == value_kc1:
                te_co_id = li[0]
                break
    db = InfoChoose.objects.filter(te_co_id=te_co_id)
    chdb = db.values('st_id')
    for sid in chdb:
        st_id = sid['st_id']
        st_name = InfoStudent.objects.get(st_id=st_id).st_name
        list.append([st_id,st_name])

    data['li'] = list
    request.session['stli'] = list
    # -------------------以下是画图
    all_number=0
    truant_number=0
    belate_number = 0
    leave_number = 0
    cq_number = 0
    path = ''
    cdb = db.values()
    for s in cdb:
        all_number = all_number+s['all_number']
        truant_number = truant_number+s['truant_number']
        belate_number = belate_number+s['belate_number']
        leave_number = leave_number+s['leave_number']
        cq_number = all_number-truant_number-belate_number-leave_number
    if all_number>0:
        path = creat_legend1(cq_number,leave_number,belate_number,truant_number,value_kc1,id,inf)
    data['path'] = path
    return JsonResponse(data=data)



def show_tecour(request):
    data = {}
    path = ''
    data_sess = request.session['data']
    id = data_sess['unum']  # 获得自己的工号
    name = data_sess['uname']  # 获得自己的姓名
    value_kc1 = request.POST.get('value_kc1')
    value_kc2 = request.POST.get('value_kc2')
    value_kc2 = str(value_kc2)
    tr = value_kc2.split(',')
    tr = tr[0]
    collinfo = request.session['courinfo']
    inf = request.session['inf']
    te_co_id = 0
    if value_kc1 != '请选择课程':
        for li in collinfo:
            if li[1] == value_kc1:
                te_co_id = li[0]
                break
    db = InfoChoose.objects.filter(te_co_id=te_co_id).get(st_id=tr)
    lendb_all = db.all_number
    lendb_3 = db.truant_number
    lendb_2 = db.belate_number
    lendb_1 = db.leave_number
    lendb_0 = lendb_all-lendb_3-lendb_2-lendb_1
    if lendb_all>0:
        rule = InfoRule.objects.first()
        attendance = rule.attendance
        absent = rule.absent
        late = rule.late
        leave = rule.leave
        absent_number = rule.absent_number
        late_number = rule.late_number

        core = InfoChoose.objects.filter(st_id=tr).filter(te_co_id=te_co_id).first()

        fl = 1
        if lendb_2 >= late_number:
            s = lendb_2 / late_number
            lendb_3 = lendb_3 + s
            lendb_2 = lendb_2 % late_number
        if lendb_3 >= absent_number:
            fl = 0
            pass
        score = ((lendb_0 * attendance + lendb_1 * leave + lendb_2 * late + lendb_3 * absent) * fl) / lendb_all
        score = round(score, 2)
        core.score = score
        core.save()

        path = creat_legend(lendb_0, lendb_1, lendb_2, lendb_3, value_kc1, id, inf, score)
    data['path'] = path

    return JsonResponse(data=data)


def show_set(request):
    data = {}
    data_sess = request.session['data']
    id = data_sess['unum']  # 获得自己的工号
    inf = request.session['inf']
    db = ''
    try:
        if inf == 'student':
            db = InfoStudent.objects.get(st_id=id).st_login_id
        elif inf == 'teacher':
            db = InfoTeacher.objects.get(te_id=id).te_login_id
        elif inf == 'admin':
            db = InfoAdmin.objects.get(admin_number=id).admin_number
    except Exception as e:
        try_log()
    data['list'] = db
    return JsonResponse(data=data)


def show_setqr(request):
    data = {}
    er = '1'
    data_sess = request.session['data']
    id = data_sess['unum']  # 获得自己的工号
    inf = request.session['inf']
    setzh=request.POST['setzh']
    sstmm=request.POST['sstmm']
    qrsstmm=request.POST['qrsstmm']
    db = ''
    if id!=setzh:
        er='1'
        data['er']=er
        return JsonResponse(data=data)
    try:
        if inf == 'student':
            db = InfoStudent.objects.get(st_id=id)
            passwd = db.st_passwd
            if passwd!=sstmm:
                er='1'
            else:
                er='0'
                db.st_passwd = qrsstmm
                db.save()
        elif inf == 'teacher':
            db = InfoTeacher.objects.get(te_id=id)
            passwd = db.te_passwd
            if passwd!=sstmm:
                er='1'
            else:
                er='0'
                db.te_passwd = qrsstmm
                db.save()
        elif inf == 'admin':
            db = InfoAdmin.objects.get(admin_number=id)
            passwd = db.admin_passwd
            if passwd != sstmm:
                er = '1'
            else:
                er = '0'
                db.admin_passwd = qrsstmm
                db.save()
        data['er'] = er
    except Exception as e:
        try_log()
    return JsonResponse(data=data)