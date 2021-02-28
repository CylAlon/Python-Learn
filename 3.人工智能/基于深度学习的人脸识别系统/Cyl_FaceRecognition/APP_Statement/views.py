import os
import re

from django.core.paginator import Paginator
from django.http import JsonResponse, FileResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from APP_BasicInfo.models import InfoRule, InfoClass, InfoStudent, InfoCollege, InfoCourse, InfoTeCour, InfoChoose, \
    InfoFacecode, InfoCheck, InfoTeacher
import matplotlib.pyplot as plt
import xlwt

# Create your views here.
from APP_Login.views import gowelcome
from Other_Code.view_utils.view_utils import try_log


def skip_person(request):
    data = {}
    inf = request.session['inf']
    if inf !='student':
        data = request.session['data']
        data['nav_path']['nav_path_one'] = '主页'
        data['userinfo'] = 'student'
        return render(request, 'skip_welcome.html', context=data)

    return render(request, 'personinfo.html', context=data)


def show_allkq(request):
    data = {}
    list = []
    li = []
    li2 = []
    li3 = []
    li4 = []
    li5 = []
    li6 = []
    collinfo = []
    teinfo = []
    value(request)  # 这里创建session
    try:
        data_sess = request.session['data']
        id = data_sess['unum']  # 获得自己的学号
        name = data_sess['uname']  # 获得自己的姓名
        per_page = 15
        chdb = InfoCheck.objects.filter(st_id=id).order_by('st_id').values()
        paglater = Paginator(chdb, per_page)  # 设置页码
        page_ob = paglater.page(1)  # 查出来的第几页的一个对象
        for lp in page_ob:
            te_co_id = lp['te_co_id']
            what_week = lp['what_week']
            what_day = lp['what_day']
            which_lesson = lp['which_lesson']
            state = lp['state']

            codb = InfoTeCour.objects
            courdb = codb.get(te_co_id=te_co_id)
            courid = courdb.cour_id  # 课程号
            teid = courdb.te_id  # 教师id

            teadb = InfoTeacher.objects.get(te_id=teid)
            tename = teadb.te_name

            coname = InfoCourse.objects.get(cour_id=courid).cour_name  # 课程名

            list.append([id, name, coname, tename, what_week, what_day, which_lesson, state])
        data['list'] = list

        # 显示课程
        choodb = InfoChoose.objects.filter(st_id=id)
        kc = choodb.values('te_co_id')
        for tid in kc:
            toid = tid['te_co_id']
            tecoddb = InfoTeCour.objects.get(te_co_id=toid)
            courid = tecoddb.cour_id
            coname = InfoCourse.objects.get(cour_id=courid).cour_name

            teid = tecoddb.te_id

            tname = InfoTeacher.objects.get(te_id=teid).te_name

            li6.append(tname)

            li.append(coname)
            collinfo.append([toid, coname])
            teinfo.append([teid, tname])
        data['li'] = li
        request.session['collinfo'] = collinfo
        request.session['teinfo'] = teinfo

        for i in range(20):
            li2.append(i + 1)
        for i in range(7):
            li3.append(i + 1)
        for i in range(12):
            li4.append(i + 1)
        li5.append('出勤')
        li5.append('迟到')
        li5.append('请假')
        li5.append('缺勤')
        data['li2'] = li2
        data['li3'] = li3
        data['li4'] = li4
        data['li5'] = li5
        data['li6'] = li6

        request.session['page'] = 1
    except Exception as e:
        try_log()
    return JsonResponse(data=data)


def value(request):
    value1 = request.POST.get('value1')
    value2 = request.POST.get('value2')
    value3 = request.POST.get('value3')
    value4 = request.POST.get('value4')
    value5 = request.POST.get('value5')
    value6 = request.POST.get('value6')

    if value1 == None:
        value1 = '请选择课程'
    if value3 == None:
        value3 = '请选择周数'
    if value4 == None:
        value4 = '请选择周几'
    if value5 == None:
        value5 = '请选择课数'
    if value6 == None:
        value6 = '请选择状态'
    value_cs = [value1, value2, value3, value4, value5, value6]
    request.session['value_cs'] = value_cs
    return value1, value2, value3, value4, value5, value6


def mdbte(request, id, per_page, page):
    dbte = ''
    page_ob = ''
    db = InfoCheck.objects.filter(st_id=id).order_by('st_id')
    value1, value2, value3, value4, value5, value6 = value(request)
    collinfo = request.session['collinfo']
    if value1 != '请选择课程':
        tecoid = 0
        for li in collinfo:
            if li[1] == value1:
                tecoid = li[0]
                break
        db = db.filter(te_co_id=tecoid)
    if value3 != '请选择周数':
        db = db.filter(what_week=value3)
    if value4 != '请选择周几':
        db = db.filter(what_day=value4)
    if value5 != '请选择课数':
        db = db.filter(which_lesson=value5)
    if value6 != '请选择状态':
        val = 10
        if value6 == '出勤':
            val = 0
        elif value6 == '请假':
            val = 1
        elif value6 == '迟到':
            val = 2
        elif value6 == '缺勤':
            val = 3
        db = db.filter(state=val)
    if value1 == '请选择课程' and value3 == '请选择周数' and value4 == '请选择周几' and value5 == '请选择课数' and value6 == '请选择状态':
        pass
    dbte = db.values()
    paglater = Paginator(dbte, per_page)  # 设置页码
    page_ob = paglater.page(page)  # 查出来的第几页的一个对象
    return page_ob


def showtab(request):
    data = {}
    list = []

    data_sess = request.session['data']
    id = data_sess['unum']  # 获得自己的学号
    name = data_sess['uname']  # 获得自己的姓名
    per_page = 15
    dbte = mdbte(request, id, per_page, 1)
    try:

        for lp in dbte:
            te_co_id = lp['te_co_id']
            what_week = lp['what_week']
            what_day = lp['what_day']
            which_lesson = lp['which_lesson']
            state = lp['state']

            codb = InfoTeCour.objects
            courdb = codb.get(te_co_id=te_co_id)
            courid = courdb.cour_id  # 课程号
            teid = courdb.te_id  # 教师id

            teadb = InfoTeacher.objects.get(te_id=teid)
            tename = teadb.te_name

            coname = InfoCourse.objects.get(cour_id=courid).cour_name  # 课程名

            list.append([id, name, coname, tename, what_week, what_day, which_lesson, state])
        data['list'] = list
        request.session['page'] = 1

    except Exception as e:
        try_log()
    return data


def show_cour(request):
    data = showtab(request)
    return JsonResponse(data=data)


def show_week(request):
    data = showtab(request)
    return JsonResponse(data=data)


def show_day(request):
    data = showtab(request)
    return JsonResponse(data=data)


def show_num(request):
    data = showtab(request)
    return JsonResponse(data=data)


def show_state(request):
    data = showtab(request)
    return JsonResponse(data=data)


def show_page(request):
    data = {}
    list = []
    page_ob = ''
    data_sess = request.session['data']
    id = data_sess['unum']  # 获得自己的学号
    name = data_sess['uname']  # 获得自己的姓名

    value1, value2, value3, value4, value5, value6 = value(request)

    page = request.session['page']
    flag = request.POST.get('flag')
    if flag == '0':
        page = page - 1
    elif flag == '1':
        page = page + 1
    request.session['page'] = page
    per_page = 15

    page_ob = mdbte(request, id, per_page, page)
    for lp in page_ob:
        te_co_id = lp['te_co_id']
        what_week = lp['what_week']
        what_day = lp['what_day']
        which_lesson = lp['which_lesson']
        state = lp['state']

        codb = InfoTeCour.objects
        courdb = codb.get(te_co_id=te_co_id)
        courid = courdb.cour_id  # 课程号
        teid = courdb.te_id  # 教师id

        teadb = InfoTeacher.objects.get(te_id=teid)
        tename = teadb.te_name

        coname = InfoCourse.objects.get(cour_id=courid).cour_name  # 课程名

        list.append([id, name, coname, tename, what_week, what_day, which_lesson, state])
    data['list'] = list

    return JsonResponse(data=data)


def get_dat(request, value_cs):
    data = {}
    list = []
    dbte = ''
    data_sess = request.session['data']
    id = data_sess['unum']  # 获得自己的学号
    name = data_sess['uname']  # 获得自己的姓名

    db = InfoCheck.objects.filter(st_id=id).order_by('st_id')

    value1 = value_cs[0]
    value3 = value_cs[2]
    value4 = value_cs[3]
    value5 = value_cs[4]
    value6 = value_cs[5]
    collinfo = request.session['collinfo']
    if value1 != '请选择课程':
        tecoid = 0
        for li in collinfo:
            if li[1] == value1:
                tecoid = li[0]
                break
        db = db.filter(te_co_id=tecoid)
    if value3 != '请选择周数':
        db = db.filter(what_week=value3)
    if value4 != '请选择周几':
        db = db.filter(what_day=value4)
    if value5 != '请选择课数':
        db = db.filter(which_lesson=value5)
    if value6 != '请选择状态':
        val = 10
        if value6 == '出勤':
            val = 0
        elif value6 == '请假':
            val = 1
        elif value6 == '迟到':
            val = 2
        elif value6 == '缺勤':
            val = 3
        db = db.filter(state=val)
    # if value1 == '请选择课程' and value3 == '请选择周数' and value4 == '请选择周几' and value5 == '请选择课数' and value6 == '请选择状态':
    #     pass
    # if value1 == None and value3 == None and value4 == None and value5 == None and value6 == None:
    #     pass

    db = db.values()
    try:

        for lp in db:
            te_co_id = lp['te_co_id']
            what_week = lp['what_week']
            what_day = lp['what_day']
            which_lesson = lp['which_lesson']
            state = lp['state']

            codb = InfoTeCour.objects
            courdb = codb.get(te_co_id=te_co_id)
            courid = courdb.cour_id  # 课程号
            teid = courdb.te_id  # 教师id

            teadb = InfoTeacher.objects.get(te_id=teid)
            tename = teadb.te_name

            coname = InfoCourse.objects.get(cour_id=courid).cour_name  # 课程名

            list.append([id, name, coname, tename, what_week, what_day, which_lesson, state])

    except Exception as e:
        try_log()
    return list


def show_print(request):
    response = ''
    try:
        data_sess = request.session['data']
        id = data_sess['unum']  # 获得自己的学号
        inf = request.session['inf']
        value_cs = request.session['value_cs']
        path = f'static/download/{inf}/{id}'
        if not os.path.exists(path):
            os.makedirs(path)
        #  下面是保存为excel
        list = get_dat(request, value_cs)

        ins = ['学号', '姓名', '课程名', '教师', '第几周',
               '周几', '第几节课', '出勤情况']
        qq = ['出勤', '请假', '迟到', '缺勤']
        work_book = xlwt.Workbook(encoding='utf-8')
        sheet = work_book.add_sheet('报表')
        for i in range(8):
            sheet.write(0, i, ins[i])
        for i in range(len(list)):
            s = i + 1
            for j in range(7):
                sheet.write(s, j, list[i][j])
            j = 7
            if list[i][j] == '0':
                sheet.write(s, 7, qq[0])
            if list[i][j] == '1':
                sheet.write(s, 7, qq[1])
            if list[i][j] == '2':
                sheet.write(s, 7, qq[2])
            if list[i][j] == '3':
                sheet.write(s, 7, qq[3])
        work_book.save(path + '/state.xls')
        # 以下是下载文件
        response = ''
        path = f'{path}/state.xls'
        file = open(path, 'rb')
        response = FileResponse(file)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = f'attachment;filename="state.xls"'
    except Exception as e:
        try_log()
    return response


def skip_class(request):
    data = {}
    inf = request.session['inf']
    if inf != 'teacher':
        data = request.session['data']
        data['nav_path']['nav_path_one'] = '主页'
        data['userinfo'] = 'teacher'
        return render(request, 'skip_welcome.html', context=data)
    return render(request, 'classinfo.html', context=data)


# ******************************************************************************************************
def show_allcl(request):
    data = {}
    list = []
    li1 = []
    li2 = []
    li3 = []
    li4 = []
    li5 = []
    li6 = []
    li7 = []
    courinfo = []
    data_sess = request.session['data']
    id = data_sess['unum']
    name = data_sess['uname']
    inf = request.session['inf']
    per_page = 15
    tecodb = InfoTeCour.objects.filter(te_id=id)
    te_co_id_db = tecodb.values('te_co_id')
    for tecoid in te_co_id_db:
        te_co_id = tecoid['te_co_id']
        tecoddb = InfoTeCour.objects.get(te_co_id=te_co_id)
        courid = tecoddb.cour_id
        coname = InfoCourse.objects.get(cour_id=courid).cour_name
        courinfo.append([te_co_id, coname])
        li1.append(coname)

        chdb = InfoCheck.objects.filter(te_co_id=te_co_id).order_by('te_co_id').values()
        paglater = Paginator(chdb, per_page)  # 设置页码
        page_ob = paglater.page(1)  # 查出来的第几页的一个对象

        for ch in page_ob:
            st_id = ch['st_id']
            st_name = InfoStudent.objects.get(st_id=st_id).st_name
            # li2.append(st_id + st_name)
            li3.append(st_name)
            what_week = ch['what_week']
            what_day = ch['what_day']
            which_lesson = ch['which_lesson']
            state = ch['state']

            list.append([coname, id, name, st_id, st_name, what_week, what_day, which_lesson, state])
        tecid = InfoChoose.objects.filter(te_co_id=te_co_id).values()
        for ig in tecid:
            st_id1 = ig['st_id']
            st_name1 = InfoStudent.objects.get(st_id=st_id1).st_name
            li2.append(st_id1 + st_name1)

    for i in range(20):
        li4.append(i + 1)
    for i in range(7):
        li5.append(i + 1)
    for i in range(12):
        li6.append(i + 1)
    li7.append('出勤')
    li7.append('迟到')
    li7.append('请假')
    li7.append('缺勤')
    data['li1'] = li1
    data['li2'] = li2
    data['li3'] = li3
    data['li4'] = li4
    data['li5'] = li5
    data['li6'] = li6
    data['li7'] = li7

    data['list'] = list
    request.session['courinfo'] = courinfo
    request.session['page'] = 1
    return JsonResponse(data=data)


def valuet(request):
    value1 = request.POST.get('value1')
    value2 = request.POST.get('value2')
    value3 = request.POST.get('value3')
    value4 = request.POST.get('value4')
    value5 = request.POST.get('value5')
    value6 = request.POST.get('value6')
    value7 = request.POST.get('value7')

    if value1 == None:
        value1 = '请选择课程'
    if value2 == None:
        value2 = '请选择学生学号'
    if value3 == None:
        value3 = '请选择学生姓名'

    if value4 == None:
        value4 = '请选择周数'
    if value4 == None:
        value4 = '请选择周几'
    if value6 == None:
        value6 = '请选择课数'
    if value7 == None:
        value7 = '请选择状态'
    if value2 != None and value2 != '请选择学生学号':
        value2 = re.findall("\d+", value2)[0]
        value2 = str(value2)
    value_cs = [value1, value2, value3, value4, value5, value6, value7]
    request.session['value_cs'] = value_cs
    return value1, value2, value3, value4, value5, value6, value7


def mdbtet(request, per_page, page):
    dbte = ''
    page_ob = ''
    db = InfoCheck.objects.all()
    value1, value2, value3, value4, value5, value6, value7 = valuet(request)
    collinfo = request.session['courinfo']
    if value1 != '请选择课程':
        tecoid = 0
        for li in collinfo:

            if li[1] == value1:
                tecoid = li[0]
                break
        db = db.filter(te_co_id=tecoid)

    if value2 != '请选择学生学号':
        db = db.filter(st_id=value2)

    if value4 != '请选择周数':
        db = db.filter(what_week=value4)
    if value5 != '请选择周几':
        db = db.filter(what_day=value5)
    if value6 != '请选择课数':
        db = db.filter(which_lesson=value6)

    if value7 != '请选择状态':
        val = 10
        if value7 == '出勤':
            val = 0
        elif value7 == '请假':
            val = 1
        elif value7 == '迟到':
            val = 2
        elif value7 == '缺勤':
            val = 3
        db = db.filter(state=val)
    dbte = db.order_by('what_week').values()

    paglater = Paginator(dbte, per_page)  # 设置页码
    page_ob = paglater.page(page)  # 查出来的第几页的一个对象
    return page_ob


def showtabt(request):
    data = {}
    list = []

    data_sess = request.session['data']
    id = data_sess['unum']  # 获得自己的学号
    name = data_sess['uname']  # 获得自己的姓名
    collinfo = request.session['courinfo']
    per_page = 15
    dbte = mdbtet(request, per_page, 1)
    teconame = ''
    st_id = ''
    st_name = ''
    try:
        for lp in dbte:
            te_co_id = lp['te_co_id']
            for li in collinfo:
                if li[0] == te_co_id:
                    teconame = li[1]
                    break
            st_id = lp['st_id']
            st_name = InfoStudent.objects.get(st_id=st_id).st_name
            what_week = lp['what_week']
            what_day = lp['what_day']
            which_lesson = lp['which_lesson']
            state = lp['state']

            list.append([teconame, id, name, st_id, st_name, what_week, what_day, which_lesson, state])
        data['list'] = list
        request.session['page'] = 1

    except Exception as e:
        try_log()
    return data


def show_court(request):
    data = showtabt(request)
    return JsonResponse(data=data)


def show_stut(request):
    data = showtabt(request)
    return JsonResponse(data=data)


def show_weekt(request):
    data = showtabt(request)
    return JsonResponse(data=data)


def show_dayt(request):
    data = showtabt(request)
    return JsonResponse(data=data)


def show_numt(request):
    data = showtabt(request)
    return JsonResponse(data=data)


def show_statet(request):
    data = showtabt(request)
    return JsonResponse(data=data)


# ---------------------------------------------

def show_paget(request):
    data = {}
    list = []
    page_ob = ''
    teconame = ''
    data_sess = request.session['data']
    id = data_sess['unum']  # 获得自己的学号
    name = data_sess['uname']  # 获得自己的姓名
    collinfo = request.session['courinfo']
    value1, value2, value3, value4, value5, value6, value7 = valuet(request)

    page = request.session['page']
    flag = request.POST.get('flag')
    if flag == '0':
        page = page - 1
    elif flag == '1':
        page = page + 1
    request.session['page'] = page
    per_page = 15

    page_ob = mdbtet(request, per_page, page)
    for lp in page_ob:
        te_co_id = lp['te_co_id']
        for li in collinfo:
            if li[0] == te_co_id:
                teconame = li[1]
                break
        st_id = lp['st_id']
        st_name = InfoStudent.objects.get(st_id=st_id).st_name
        what_week = lp['what_week']
        what_day = lp['what_day']
        which_lesson = lp['which_lesson']
        state = lp['state']

        list.append([teconame, id, name, st_id, st_name, what_week, what_day, which_lesson, state])
    data['list'] = list

    return JsonResponse(data=data)


def get_datt(request, value_cs):
    data = {}
    list = []
    dbte = ''
    data_sess = request.session['data']
    id = data_sess['unum']  # 获得自己的学号
    name = data_sess['uname']  # 获得自己的姓名

    db = InfoCheck.objects.all()

    value1 = value_cs[0]
    value2 = value_cs[1]
    value3 = value_cs[2]
    value4 = value_cs[3]
    value5 = value_cs[4]
    value6 = value_cs[5]
    value7 = value_cs[6]

    collinfo = request.session['courinfo']
    if value1 != '请选择课程':
        tecoid = 0
        for li in collinfo:

            if li[1] == value1:
                tecoid = li[0]
                break
        db = db.filter(te_co_id=tecoid)

    if value2 != '请选择学生学号':
        db = db.filter(st_id=value2)

    if value4 != '请选择周数':
        db = db.filter(what_week=value4)
    if value5 != '请选择周几':
        db = db.filter(what_day=value5)
    if value6 != '请选择课数':
        db = db.filter(which_lesson=value6)

    if value7 != '请选择状态':
        val = 10
        if value7 == '出勤':
            val = 0
        elif value7 == '请假':
            val = 1
        elif value7 == '迟到':
            val = 2
        elif value7 == '缺勤':
            val = 3
        db = db.filter(state=val)
    db = db.values()
    try:

        for lp in db:
            te_co_id = lp['te_co_id']
            what_week = lp['what_week']
            what_day = lp['what_day']
            which_lesson = lp['which_lesson']
            state = lp['state']

            codb = InfoTeCour.objects
            courdb = codb.get(te_co_id=te_co_id)
            courid = courdb.cour_id  # 课程号
            teid = courdb.te_id  # 教师id

            teadb = InfoTeacher.objects.get(te_id=teid)
            tename = teadb.te_name

            coname = InfoCourse.objects.get(cour_id=courid).cour_name  # 课程名

            list.append([id, name, coname, tename, what_week, what_day, which_lesson, state])

    except Exception as e:
        try_log()

    return list


def show_printt(request):
    response = ''
    try:
        data_sess = request.session['data']
        id = data_sess['unum']
        inf = request.session['inf']
        value_cs = request.session['value_cs']
        path = f'static/download/{inf}/{id}'
        if not os.path.exists(path):
            os.makedirs(path)

        #  下面是保存为excel
        list = get_datt(request, value_cs)

        ins = ['课程名', '教师号', '学号', '姓名', '教师', '第几周', '周几', '第几节课', '出勤情况']
        qq = ['出勤', '请假', '迟到', '缺勤']

        work_book = xlwt.Workbook(encoding='utf-8')
        sheet = work_book.add_sheet('报表')
        for i in range(9):
            sheet.write(0, i, ins[i])
        for i in range(len(list)):
            s = i + 1
            for j in range(8):
                sheet.write(s, j, list[i][j])
            j = 7
            if list[i][j] == '0':
                sheet.write(s, 8, qq[0])
            if list[i][j] == '1':
                sheet.write(s, 8, qq[1])
            if list[i][j] == '2':
                sheet.write(s, 8, qq[2])
            if list[i][j] == '3':
                sheet.write(s, 8, qq[3])

        work_book.save(path + '/state.xls')

        # 以下是下载文件

        response = ''
        path = f'{path}/state.xls'
        file = open(path, 'rb')

        response = FileResponse(file)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = f'attachment;filename="state.xls"'
    except Exception as e:
        try_log()

    return response
