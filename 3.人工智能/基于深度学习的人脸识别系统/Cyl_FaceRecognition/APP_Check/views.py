import time

import cv2
import numpy as np
from django.core.paginator import Paginator
from django.db import transaction
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from APP_BasicInfo.models import InfoRule, InfoClass, InfoStudent, InfoCollege, InfoCourse, InfoTeCour, InfoChoose,InfoFacecode,InfoCheck
from Other_Code.face.utils import utils
from Other_Code.face.utils.utils import compare_faces
from Other_Code.view_utils.view_utils import try_log
from Cyl_FaceRecognition.settings import FACE_CLASS as face, CAMERA_IP, END_TIME, CD_TIME
from Cyl_FaceRecognition import class_state


def skip_set_check(request):
    data = {}
    inf = request.session['inf']
    if inf != 'admin':
        data = request.session['data']
        data['nav_path']['nav_path_one'] = '主页'
        data['userinfo'] = 'admin'
        return render(request, 'skip_welcome.html', context=data)
    try:

        dbinf = InfoRule.objects.first()
        data['attendance'] = dbinf.attendance
        data['absent'] = dbinf.absent
        data['late'] = dbinf.late
        data['leave'] = dbinf.leave
        data['absent_number'] = dbinf.absent_number
        data['late_number'] = dbinf.late_number

    except Exception as e:
        try_log()
    return render(request,'skip_set_check.html',context=data)

def set_check(request):
    data = {}
    data_sess = request.session['data']  # 获得自己的ID
    unum = data_sess['unum']
    with transaction.atomic():
        try:
            attendance = request.POST.get('attendance')
            absent = request.POST.get('absent')
            late = request.POST.get('late')
            leave = request.POST.get('leave')
            absent_number = request.POST.get('absent_number')
            late_number = request.POST.get('late_number')
            db = InfoRule.objects.first()
            db.admin_number = unum
            db.attendance = attendance
            db.absent = absent
            db.late = late
            db.leave = leave
            db.absent_number = absent_number
            db.late_number = late_number
            db.save()
            data['er'] = '1'
        except Exception as ed:
            data['er'] = '0'
            try_log()

    return JsonResponse(data=data)


def skip_check(request):
    inf = request.session['inf']
    data = {}
    if inf != 'teacher':
        data = request.session['data']
        data['nav_path']['nav_path_one'] = '主页'
        data['userinfo'] = 'teacher'
        return render(request, 'skip_welcome.html', context=data)
    data['ip'] = data['ip'] = CAMERA_IP
    return render(request,'skip_check.html',context=data)



def show_college(request):
    """
    学院下拉框显示  更具教师的ID查看
    :param request:
    :return:
    """
    #--------------需要权限判断
    data = {}
    list = []
    sess_list = []
    data_sess = request.session['data']  # 获得自己的ID
    unum = data_sess['unum']
    teco = InfoTeCour.objects.filter(te_id=unum).values()
    for t in teco:
        tcid = t['te_co_id']
        couid = t['cour_id']
        db = InfoCourse.objects
        try:
            courname = db.get(cour_id=couid).cour_name
            if courname in list:
                courname = courname + tcid[-2:-1]
            sess_list.append([courname, tcid])
            list.append(courname)
        except Exception as e:
            try_log()

    request.session['list'] = sess_list
    data['list'] = list
    return JsonResponse(data=data)


def show_week(request):
    data={}
    list = []
    value1 = request.POST.get('value1')
    lis = request.session['list']
    tecoid = ''
    for li in lis:
        if li[0] == value1:
            tecoid = li[1]
            break
    try:
        tcdb = InfoTeCour.objects.get(te_co_id=tecoid)
        begin = int(tcdb.begin_time)
        end =int(tcdb.end_time)
        while begin!=end+1:
            list.append(begin)
            begin = begin+1
    except Exception as e:
        try_log()
    request.session['te_co_id'] = tecoid
    data['list'] = list

    return JsonResponse(data=data)


def show_day(request):
    data = {}
    list = []
    tecoid = request.session['te_co_id']
    try:
        tcdb = InfoTeCour.objects.get(te_co_id=tecoid)
        sp = tcdb.specific.split(';')
        for s in sp:
            s = s.split(':')
            list.append(s[0])
    except Exception as e:
        try_log()
    data['list'] = list
    return JsonResponse(data=data)


def show_num(request):
    data = {}
    list = []
    tecoid = request.session['te_co_id']
    try:
        tcdb = InfoTeCour.objects.get(te_co_id=tecoid)
        sp = tcdb.specific.split(';')
        for s in sp:
            if len(s)!=0:
                s = s.split(':')
                s = s[1].split(',')
                for f in s:
                    list.append(f)
    except Exception as e:
        try_log()
    data['list'] = list
    return JsonResponse(data=data)





def show_conf(request):
    """
    选择号信息点击确认
    :param request:
    :return:
    """
    data = {}
    list = []
    sesslist = []
    stidlist = []

    value2 = request.POST.get('value2')
    value3 = request.POST.get('value3')
    value4 = request.POST.get('value4')
    if value3 =='请选择周几' or value4=='请选择课数' or value4=='请选周数':
        return JsonResponse(data=data)
    clval = [value2,value3,value4]
    request.session['clval']=[value2,value3,value4]




    tecoid = request.session['te_co_id']

    with transaction.atomic():
        try:
            tecodb = InfoChoose.objects.filter(te_co_id=tecoid).distinct().values('st_id')  # 查出该堂客的学生ID
            for id in tecodb:
                sid = id['st_id']
                stidlist.append(sid)
                # 插入检查表
                ckdb = InfoCheck()
                try:
                    ckdb = InfoCheck.objects.filter(te_co_id=tecoid).filter(what_week=clval[0]).filter(
                        what_day=clval[1]).filter(which_lesson=clval[2]).get(st_id=sid)  # 查看源库是否存在 存在则做修改
                except Exception as ex: # 不存在
                    db = InfoChoose.objects.filter(te_co_id=tecoid).get(st_id=sid)
                    db.all_number = db.all_number+1
                    db.truant_number = db.truant_number+1
                    db.save()
                    ckdb.st_id = sid
                    ckdb.te_co_id = tecoid
                    ckdb.what_week = clval[0]
                    ckdb.what_day = clval[1]
                    ckdb.which_lesson = clval[2]
                    ckdb.state = class_state[3]
                    ckdb.save()


            # request.session['stidlist'] = stidlist

            tcdb = InfoChoose.objects.filter(te_co_id=tecoid).order_by('st_id').distinct().values('st_id')
            i = 0
            for st in tcdb:
                if i<5:
                    i = i+1
                    stu = InfoStudent.objects.get(st_id=st['st_id'])
                    stu_id = stu.st_id
                    stu_name = stu.st_name
                    stu_pic_path = stu.st_pic_path
                    cl_id = stu.cl_id
                    cl_name = InfoClass.objects.get(cl_id=cl_id).cl_name
                    state = InfoCheck.objects.filter(te_co_id=tecoid).filter(what_week=clval[0]).filter(
                        what_day=clval[1]).filter(which_lesson=clval[2]).get(st_id=stu_id).state
                    list.append([stu_pic_path,stu_id,stu_name,cl_name,state])
                    sesslist.append(stu_id)
                else:
                    break
            request.session['page']=1
        except Exception as e:
            try_log()
    # print(list)
    request.session['sesslist'] = sesslist
    data['list'] = list
    return JsonResponse(data=data)


def show_pagetrun(request):
    """
    向下翻页
    :param request:
    :return:
    """
    data = {}
    list = []
    sesslist = []
    tecoid = request.session['te_co_id']
    page = request.session['page']
    flag = request.POST.get('flag')
    clval = request.session['clval']
    if flag=='0':
        page = page-1
    elif flag=='1':
        page = page + 1
    request.session['page']=page
    per_page = 5
    stuchoose = InfoChoose.objects.filter(te_co_id=tecoid).order_by('st_id').distinct().values('st_id')

    paglater = Paginator(stuchoose, per_page)  # 设置页码
    page_ob = paglater.page(page)  # 查出来的第几页的一个对象
    try:
        for p in page_ob:
            stid = p['st_id']
            stinfo = InfoStudent.objects.get(st_id=stid)
            clid = InfoClass.objects.get(cl_id=stinfo.cl_id).cl_name
            state = InfoCheck.objects.filter(te_co_id=tecoid).filter(what_week=clval[0]).filter(
                what_day=clval[1]).filter(which_lesson=clval[2]).get(st_id=stid).state
            list.append([stinfo.st_pic_path, stinfo.st_id, stinfo.st_name, clid,state])
            sesslist.append(stinfo.st_id)
    except Exception as  e:
        try_log()
    data['list'] = list
    data['err'] = '1'
    request.session['sesslist'] = sesslist
    return JsonResponse(data=data)

def show_kaoqin(request):
    """
    学生签到
    :param request: 
    :return: 
    """""
    data = {
            "err": '1',
            "number": '0',
            }
    list = []
    starttime = time.time()
    tecoid = request.session['te_co_id']
    clval = request.session['clval']
    clval = request.session['clval']
    print('准备签到*************************')

    camp = cv2.VideoCapture(CAMERA_IP)
    dis = 0
    stuiid=''
    stunamee=''
    ck = ''
    print('准备完毕***************************************')
    while True:
        try:
            mtime = time.time()
            ti = mtime-starttime
            if ti>END_TIME:
                break
            ret, frame = camp.read()
            img = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            box = face[0].faceDecognition(img)
            box = utils.change_box(np.array(box))

            ck = InfoCheck.objects.filter(te_co_id=tecoid).filter(what_week=clval[0]).filter(
                        what_day=clval[1]).filter(which_lesson=clval[2])

            ckdb = ck.filter(~Q(state=class_state[0])).values()
            if len(ckdb)==0:
                break

            for bo in box:

                face_img = img[int(bo[1]):int(bo[3]), int(bo[0]):int(bo[2])]
                face_encoding = face[1].face_encoding(face_img, bo)
                for sid in ckdb:
                    sid = sid['st_id']
                    sttdb = InfoStudent.objects.get(st_id=sid)
                    sname = sttdb.st_name
                    fadb = InfoFacecode.objects.get(st_id=sid).face_encoding
                    fadb = fadb.replace('\n', '').strip('[ ]')
                    fadb = fadb.split(' ')
                    ll = []
                    for f in fadb:
                        if len(f) != 0:
                            ll.append(float(f))
                    fadb = np.array(ll)

                    fl,dis = compare_faces(fadb,face_encoding)
                    if fl==True:
                        db = ck.get(st_id=sid)
                        if ti>CD_TIME and ti<END_TIME:
                            db.state = class_state[2]
                        elif ti<=CD_TIME:
                            db.state = class_state[0]
                        db.save()
                        list.append([dis,sid,sname])

            if len(list) !=0:
                for s in list:
                    print(f"{s[1]} {s[2]} 签到成功  对比脸获得空间长度为 {s[0]}")
                list=[]

            else:
                print('这个图像不匹配 签到失败')
                # pass
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
        except Exception as e:
            try_log()
    index = len(ck.filter(state=class_state[0]))
    data['number'] = index
    #  签到完成进行局部刷新
    sesslist = []
    tcdb = InfoChoose.objects.filter(te_co_id=tecoid).order_by('st_id').distinct().values('st_id')
    i = 0
    for st in tcdb:
        if i < 5:
            i = i + 1
            stu = InfoStudent.objects.get(st_id=st['st_id'])
            stu_id = stu.st_id
            stu_name = stu.st_name
            stu_pic_path = stu.st_pic_path
            cl_id = stu.cl_id
            cl_name = InfoClass.objects.get(cl_id=cl_id).cl_name
            state = InfoCheck.objects.filter(te_co_id=tecoid).filter(what_week=clval[0]).filter(
                what_day=clval[1]).filter(which_lesson=clval[2]).get(st_id=stu_id).state
            list.append([stu_pic_path, stu_id, stu_name, cl_name, state])
            sesslist.append(stu_id)
        else:
            break
    data['list'] = list
    data['sesslist'] = sesslist
    return JsonResponse(data=data)


def show_deta(request):
    """
    签到详情
    :param request:
    :return:
    """
    data = {}
    nstid = request.POST.get('nstid')
    kgfl = request.POST.get('kgfl')
    clval = request.session['clval']
    tecoid = request.session['te_co_id']

    print(nstid)
    db = InfoCheck.objects.filter(te_co_id=tecoid).filter(what_week=clval[0]).filter(
                        what_day=clval[1]).filter(which_lesson=clval[2]).get(st_id=nstid).state

    data['state']=db
    data['stid']=nstid
    request.session['nstid']=nstid
    return JsonResponse(data=data)

def show_gb(request):
    """
    关闭清除ID
    :param request:
    :return:
    """
    data = {}
    try:
        del request.session['nstid']
    except Exception as e:
        try_log()
    return JsonResponse(data=data)



def core(flag,oflag,stid,tecoid):

    db = InfoChoose.objects.filter(te_co_id=tecoid).get(st_id=stid)

    if flag == '0':  # 出勤
        if oflag =='0':
            pass
        elif oflag == '1':
            lc = db.leave_number
            db.leave_number = lc - 1
            pass
        elif oflag == '2': # 迟到
            lc = db.belate_number
            db.belate_number = lc-1
        elif oflag == '3': # 缺勤
            qq = db.truant_number
            db.truant_number = qq-1
    elif flag == '1':  # 请假
        lv = db.leave_number
        db.leave_number = lv + 1
        if oflag =='0':
            pass
        elif oflag == '1':
            lv = db.leave_number
            db.leave_number = lv - 1
        elif oflag == '2': # 迟到
            lc = db.belate_number
            db.belate_number = lc-1
        elif oflag == '3': # 缺勤
            qq = db.truant_number
            db.truant_number = qq-1
    elif flag == '2':  # 迟到
        lv = db.belate_number
        db.belate_number = lv + 1
        if oflag =='0':
            pass
        elif oflag == '1':
            lv = db.leave_number
            db.leave_number = lv - 1
        elif oflag == '2': # 迟到
            lv = db.belate_number
            db.belate_number = lv - 1
        elif oflag == '3': # 缺勤
            qq = db.truant_number
            db.truant_number = qq-1
    elif flag == '3':  # 旷课
        lv = db.truant_number
        db.truant_number = lv + 1
        if oflag =='0':
            pass
        elif oflag == '1':
            lv = db.leave_number
            db.leave_number = lv - 1
        elif oflag == '2': # 迟到
            lv = db.belate_number
            db.belate_number = lv - 1
        elif oflag == '3': # 缺勤
            lv = db.truant_number
            db.truant_number = lv - 1

    db.save()





def show_xq(request):
    """
    点击出勤 缺勤......
    :param request:
    :return:
    """
    data = {}
    nstid = request.POST.get('nstid')
    clval = request.session['clval']
    tecoid = request.session['te_co_id']
    xqflag = request.POST.get('xqflag')
    sesslist = request.session['sesslist']
    num = sesslist.index(nstid)
    db = InfoCheck.objects.filter(te_co_id=tecoid).filter(what_week=clval[0]).filter(
        what_day=clval[1]).filter(which_lesson=clval[2]).get(st_id=nstid)
    st = db.state
    with transaction.atomic():
        try:
            core(xqflag, st, nstid, tecoid)
            if xqflag=='0': #出勤
                db.state = class_state[0]
            elif xqflag =='1':
                db.state = class_state[1]
            elif xqflag == '2':
                db.state = class_state[2]
            elif xqflag=='3':
                db.state = class_state[3]
            db.save()

        except Exception as e:
            try_log()

    data['num'] = num+2
    return JsonResponse(data=data)


