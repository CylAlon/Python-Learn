$(document).ready(function () {
    //页面加载后载访问获取信息  该页面独有
    $(function () {
        $.post('/app_import/class_info_face/', {
            "info_flag": "1",
        }, function (data, status) {
            for (i = 0; i < data.index.length; i++) {
                $('#se1').append('<option>' + data.index[i] + '</option>');
            }
        });
        return false;
    });




    //浮层
    $("#admin_button").click(function () {
        $('.fc').slideDown('show')
    });
    $("#tj_button").click(function () {
        $('.fc').slideUp('show')
    });
    $("#gb_button").click(function () {
        $('.fc').slideUp('show')
    });
    $("#tjj_button").click(function () {
        $('.afc').slideUp('show')
    });
    $("#gbb_button").click(function () {
        $('.afc').slideUp('show')
    });

    //ajax上传文件方法
    function upload(file_id, field, path, content_id) {
        var upload_file = $(file_id)[0].files[0];
        var formData = new FormData();
        formData.append(field, upload_file);
        $.ajax({
            url: "/app_import/" + path + "/",
            type: "POST",
            data: formData,
            contentType: false,
            processData: false,
            success: function (data) {
                $(content_id).html(data.info_flag);
                if (data.error_flag != '0')
                    $(content_id).css("color", "red");
                else if (data.error_flag == '0')
                    $(content_id).css("color", "black");
            }
        });
    }

    //添加学院
    $("#college_button").click(function () {
        upload("#college_file", "college_file", "college_info", "#td_coll");
        return false;
    });
    //管理员提交方式
    $("#tj_button").click(function () {
        $.post('/app_import/admin_info/', {
                "admin_number": $("#admin_number").val(),
                "admin_passwd": $("#admin_passwd").val(),
            },
            function (data, status) {
                $("#td_admin").html(data.info_flag);
                if (data.error_flag != '0')
                    $("#td_admin").css("color", "red");
                else if (data.error_flag == '0')
                    $("#td_admin").css("color", "black");
            });
        return false;
    });
    //   添加教师
    $("#teacher_button").click(function () {
        upload("#teacher_file", "teacher_file", "teacher_info", "#td_teacher");

        return false;
    });
    //添加专业
    $("#specialty_button").click(function () {
        upload("#specialty_file", "specialty_file", "specialty_info", "#td_sp");

        return false;
    });
    //添加班级
    $("#class_button").click(function () {
        upload("#class_file", "class_file", "class_info", "#td_class");

        return false;
    });

    // 添加学生
    $("#student_button").click(function () {
        upload("#student_file", "student_file", "student_info", "#td_stu");

        return false;
    });
    //课程
    $("#course_button").click(function () {
        upload("#course_file", "course_file", "course_info", "#td_course");
        return false;
    });


    //添加课程表
    $("#course_table_button").click(function () {
        upload("#course_table_file", "course_table_file", "course_table", "#td_table_course");
        return false;

    });

//    以下是人脸数据采集

    function change_box(s1, s2, da) {
        $.post('/app_import/class_info_face/', {
            "info_flag": da,
            "index1": $('#se1').val(),
            "index2": $('#se2').val(),
            "index3": $('#se3').val(),
        }, function (data, status) {
            if ($(s2 + " .tj"))
                $(s2 + " .tj").remove(); // 伤处上一次选择添加的元素 防止重复
            if (s1 == "#se1")  //如果是第一个框 则删除下面的全部
                $("#se3" + " .tj").remove();

            for (i = 0; i < data.index.length; i++) {
                $(s2).append('<option class="tj">' + data.index[i] + '</option>');

            }
        });
        return false;
    }

    $("#se1").change(function () {
        change_box("#se1", "#se2", "2")
    });
    $("#se2").change(function () {
        change_box("#se2", "#se3", "3")
    });
    //班级悬着完成后确定
    $("#face_cl_button").click(function () {
        $.post('/app_import/class_info_face/', {
            "info_flag": '4',
            "index1": $('#se1').val(),
            "index2": $('#se2').val(),
            "index3": $('#se3').val(),
        }, function (data, status) {
            $('#vah2').html(data.stu_id + " " + data.stu_name);
            if (data.err == '1') {
                $("#errinf").html('信息不正确，请重新输入')
            }
            // bgm_img(data.img_path);
            $("#face_bgm").css({
                "background": "url('/static/" + data.img_path + "') no-repeat",
                "background-size": "100% 100%"
            });

        });

        return false;
    });

    $("#xz2").click(function () {
        $.post('/app_import/cloose_stu/', {
            "info_flag": '1',
        }, function (data, status) {
            if (data.stu_id != null) {
                $('#vah2').html(data.stu_id + " " + data.stu_name);
                $("#face_bgm").css({
                    "background": "url('/static/" + data.img_path + "') no-repeat",
                    "background-size": "100% 100%"
                });
            }
            if (data.err == '1') {
                $("#erran").html('没有该学生');
            }
            else if (data.err != '1'){
                $("#erran").html('&nbsp;');
            }
        });
        return false;
    });


    $("#xz1").click(function () {
        $.post('/app_import/cloose_stu/', {
            "info_flag": '0',
        }, function (data, status) {
            if (data.stu_id != null){
                $('#vah2').html(data.stu_id + " " + data.stu_name);
             $("#face_bgm").css({
                "background": "url('/static/" + data.img_path + "') no-repeat",
                "background-size": "100% 100%"
            });
             }
            if (data.err == '1') {
                $("#erran").html('没有该学生');
            }
        });
        return false;
    });

    $("#paizao").click(function () {
        $.post('/app_import/cloose_stu/', {
            "info_flag": '2',
        }, function (data, status) {
            if (data.stu_id != null) {
                $('#vah2').html(data.stu_id + " " + data.stu_name);
                $("#face_bgm").css({
                    "background": "url('/static/" + data.img_path + "') no-repeat",
                    "background-size": "100% 100%"
                });
            }

            if (data.err == '1') {
                $("#erran").html('没有该学生');
                $("#erran").css("color", "red");
            }
            else if (data.err == '2') {
                $("#erran").html('获取人像不成功');
                $("#erran").css("color", "red");
            }
            else if (data.err == '3') {
                $("#erran").html(data.stu_id + " " + data.stu_name+'--获取头像成功');
                $("#erran").css("color", "black");
            }
        });
        return false;
    });
});

