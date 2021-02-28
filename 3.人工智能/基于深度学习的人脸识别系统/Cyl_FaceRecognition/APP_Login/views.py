# encoding=utf-8
import hashlib
import time
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse

from APP_BasicInfo.models import InfoStudent, InfoTeacher, InfoAdmin
# from Cyl_FaceRecognition import LOGIN_FLAG
# from Middlewares import login_flag
from Other_Code.view_utils import view_utils as utils
from Other_Code.view_utils.view_utils import try_log


def return_anew(request, uname='', upad='', ucod=''):
    """
    GET提交时执行  生成验证码并返回登陆页面
    :param request:
    :param uname:
    :param upad:
    :param ucod:
    :return:
    """
    data = {
        'uname': uname,
        'upad': upad,
        'ucod': ucod,
    }
    name = utils.createCode() # 画二维码
    request.session['yzmname'] = name
    print(name)
    return render(request, 'login.html', context=data)


def create_token(request, username, radio):
    """
    创建token  使用ip和用户名和使时间构成唯一的令牌
    :param request:
    :param username:
    :param radio:
    :return:
    """
    ip = request.META.get("REMOTE_ADDR")
    c_time = time.ctime()

    r = username

    return radio + hashlib.new("md5", (ip + c_time + r).encode("utf-8")).hexdigest()


def login(request):
    uname = ''
    unum = ''
    img_path = ''
    inf = ''
    yzm = 0
    data ={}
    request.session['viflag'] = '1' # 是否开局拦截
    if request.method == 'GET':
        return return_anew(request)
    elif request.method == 'POST':
        yzmname = request.session.get('yzmname')
        da = request.POST
        uco = da.get('usercode').lower()
        try:
            yzm = yzmname.lower()
        except Exception as e:
            yzm = '0'
        if uco != yzm:
            return return_anew(request, ucod='验证码错误')
        elif uco == yzm:
            username = da.get('username')
            userpasswd = da.get('userpassword')
            radio = da.get('radio')
            db_login = ''
            if radio == 'radio1':
                db_login = InfoStudent.objects.filter(st_login_id=username).filter(st_passwd=userpasswd)
            elif radio == 'radio2':
                db_login = InfoTeacher.objects.filter(te_login_id=username).filter(te_passwd=userpasswd)
            elif radio == 'radio3':
                db_login = InfoAdmin.objects.filter(admin_number=username).filter(admin_passwd=userpasswd)
            if db_login.exists():
                token = create_token(request, username, radio)
                db_login = db_login.first()
                if radio == 'radio1':
                    db_login.st_token = token
                    db_login.save()
                    uname = db_login.st_name
                    unum = db_login.st_id
                    img_path = db_login.st_pic_path
                    inf = 'student'
                elif radio == 'radio2':
                    db_login.te_token = token
                    db_login.save()
                    uname = db_login.te_name
                    unum = db_login.te_id
                    img_path = db_login.te_pic_path
                    inf = 'teacher'
                elif radio == 'radio3':
                    db_login.admin_token = token
                    db_login.save()
                    uname = db_login.admin_number
                    unum = uname
                    img_path = db_login.admin_pic_path
                    inf = 'admin'
                response = redirect(reverse('app_login:welcome'))
                response.set_cookie('token', token)
                request.session['data'] = data
                request.session['inf'] = inf
                return response
            else:
                return return_anew(request, upad='账号或密码错误')

def gowelcome(request):  #  0 不刷新
    data = request.session['data']
    data['nav_path']['nav_path_one'] = '主页'
    return render(request, 'welcome.html', context=data)

def welcome(request):
    inf = ''
    try:
        inf = request.session['inf']
    except Exception as e:
        try_log()
    data = request.session['data']
    data['nav_path']['nav_path_one'] = '主页'
    if inf == 'teacher':
        return render(request, 'teacher_welcome.html', context=data)
    elif inf == 'student':
        return render(request, 'student_welcome.html', context=data)
    elif inf == 'admin':
        return render(request, 'admin_welcome.html', context=data)
    # return gowelcome(request)

    # data = request.session['data']
    # data['nav_path']['nav_path_one'] = '主页'
    # return render(request, 'welcome.html', context=data)



def loginout(request):

    token = request.COOKIES.get('token')
    iden = str(token)[5:6]
    db = 0
    try:
        if iden == '1':
            db = InfoStudent.objects.get(st_token=token)
            db.st_token = ' '
        elif iden == '2':
            db = InfoTeacher.objects.get(te_token=token)
            db.te_token = ' '
        elif iden == '3':
            db = InfoAdmin.objects.get(admin_token=token)
            db.admin_token = ' '

        db.save()
    except Exception as e:
        pass
    request.session.flush()
    response = redirect(reverse('app_login:login'))
    response.delete_cookie('token')
    return response


def skip_welcome(request):

    return gowelcome(request)