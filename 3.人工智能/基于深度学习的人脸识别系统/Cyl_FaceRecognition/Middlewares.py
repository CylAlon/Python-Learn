from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect, HttpResponse, render
from django.urls import reverse

# process_request和process_response两个方法最常用

from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect, HttpResponse
from django.urls import reverse

from APP_BasicInfo.models import InfoStudent, InfoTeacher, InfoAdmin
from APP_Login.views import return_anew
# from Cyl_FaceRecognition import LOGIN_FLAG
from Other_Code.view_utils import view_utils as utils



# class MiddlewareToken(MiddlewareMixin):
#     def process_request(self, request):
#
#
#
#         return None



login_flag = 0

class Middleware1(MiddlewareMixin):
    def process_request(self, request):
        """
        中间件--携带token验证登陆信息
        :param request:
        :return:
        """
        token = '0'
        viflag = '0'
        try:
            viflag = request.session['viflag']
            token = request.COOKIES.get('token')
        except Exception as ed:
            pass
        try:

            loginflag = request.POST.get('loginflag')
            if loginflag == 'login':
                return None
        except Exception as er:
            pass

        if token is None and viflag=='1':
            request.session.flush()
            return return_anew(request)
        iden = str(token)[5:6]
        uname = ''
        unum = ''
        img_path = ''
        try:
            if iden == '1':
                db = InfoStudent.objects.get(st_token=token)
                uname = db.st_name
                unum = db.st_id
                img_path = db.st_pic_path
            elif iden == '2':
                db = InfoTeacher.objects.get(te_token=token)
                uname = db.te_name
                unum = db.te_id
                img_path = db.te_pic_path
            elif iden == '3':
                db = InfoAdmin.objects.get(admin_token=token)

                uname = db.admin_number
                unum = uname
                img_path = db.admin_pic_path
            data = {
                'title': '',
                'nav_path': {'nav_path_one': '',
                             'nav_path_two': '',
                             'nav_path_three': '',
                             'nav_path_four':''
                             },  # 每个功能的导航
                'uname': uname,
                'unum': unum,
                'img_path': img_path,
                'file_flag': ''
            }
            request.session['data']=data
            return None
        except Exception as e:
            print('不存在token,再此拦截')
            return return_anew(request,ucod='数字证书错误')        #redirect(reverse('app_login:login'))



    # def process_view(self, request, view_func, view_args, view_kwargs):
    #     print('M1_process_view:控制器映射之后，视图函数执行之前')

    # def process_exception(self, request, exception):
    #     """
    #     中间件--视图函数错误执行
    #     :param request:
    #     :param exception:
    #     :return:
    #     """
    #     print('***************************************************************')
    #     print('***************************************************************')
    #     print('**************************   报错了     ***********************')
    #     print('***************************************************************')
    #     print('***************************************************************')
    #     return redirect(reverse('app_login:login'))



    # def process_response(self, request, response):
    #     print('M1_process_response')
    #     # 在process_response中，返回值只有为response对象时，才会接力式返回视图函数的返回结果，否则会被process_response中的return结果覆盖，不写则报错
    #     return HttpResponse('M1_process_response：视图函数执行之后，wsgi.py封装send之前，返回值不是接力原视图函数resopnse对象，而是被覆盖')
    #     # return response


