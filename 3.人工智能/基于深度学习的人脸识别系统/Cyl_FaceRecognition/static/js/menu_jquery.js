var nav_data = {
    "home": {"nav_path_one": "主页", "nav_path_two": "", "nav_path_three": ""},
    "student_info": {
        "person": {"nav_path_one": "学生信息", "nav_path_two": "/", "nav_path_three": "个人信息"},
        "class": {"nav_path_one": "学生信息", "nav_path_two": "/", "nav_path_three": "班级信息"}
    },

    "get_info": {
        "person": {"nav_path_one": "", "nav_path_two": "", "nav_path_three": ""},
        "class": {"nav_path_one": "", "nav_path_two": "", "nav_path_three": ""}
    },

    "sssss": {
        "person": {"nav_path_one": "", "nav_path_two": "", "nav_path_three": ""},
        "class": {"nav_path_one": "", "nav_path_two": "", "nav_path_three": ""}
    },

};

function nav_info(nav1, nav2, nav3, id, data) {
    $("#nav_path_one").html(nav1);
    $("#nav_path_two").html(nav2);
    $("#nav_path_three").html(nav3);
    $(id).html(data);
}

$(document).ready(function () {
    $(".comment_div").css("height", "900px");
    // 基础数据导入提交
    $("#get_info_base").click(function () {
        $.get('/app_import/skip_import/',
            function (data, status) {
                nav_info("数据导入", "/", "基础数据导入", "#ajcr", data);
            });
        return false;
    });
    //人脸数据采集
    $("#get_info_face").click(function () {
        $.get('/app_import/face_gather/',
            function (data, status) {
                nav_info("数据导入", "/", "人脸数据采集", "#ajcr", data);
            });
        return false;
    });
    //学生考勤
    $("#student_check").click(function () {
        $.get('/app_check/skip_check/',
            function (data, status) {
                nav_info("考勤管理", "/", "立即考勤", "#ajcr", data);
            });
        return false;
    });


    //考勤管理
    $("#get_info_check_message").click(function () {
        $.get('/app_check/skip_set_check/',
            function (data, status) {
                nav_info("考勤管理", "/", "考勤规则", "#ajcr", data);
            });
        return false;
    });
    //个人信息查询
    $("#get_person_message").click(function () {
        $.get('/app_statement/skip_person/',
            function (data, status) {
                nav_info("考勤信息", "/", "个人考勤信息", "#ajcr", data);
            });
        return false;
    });
     //班级信息查询
    $("#get_class_message").click(function () {
        $.get('/app_statement/skip_class/',
            function (data, status) {
                nav_info("考勤信息", "/", "班级考勤信息", "#ajcr", data);
            });
        return false;
    });









    $("#nav_path_one").bind('DOMNodeInserted', function (e) {

        $.get('/app_basic/clear_session/', function (data, status) {

        });
        return false;

    });

});


