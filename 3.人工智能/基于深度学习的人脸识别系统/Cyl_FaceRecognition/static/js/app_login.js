// $("#im").click(function () {
//         $.post('/app_login/login/', {
//         }, function (data, status) {
//             $('#vah2').html(data.stu_id + " " + data.stu_name);
//             if (data.err == '1') {
//                 $("#errinf").html('信息不正确，请重新输入')
//             }
//             // bgm_img(data.img_path);
//             $("#face_bgm").css({
//                 <img src="{% static 'img/verification_code/yzmimg.jpg' %}" id="code" alt="验证码">
//                 "background": "url('/static/" + data.img_path + "') no-repeat",
//                 "background-size": "100% 100%"
//             });
//
//         });
//
//         return false;
//     });