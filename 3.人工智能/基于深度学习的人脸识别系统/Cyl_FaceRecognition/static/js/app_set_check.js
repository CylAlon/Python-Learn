$(document).ready(function () {
    $(".comment_div").css("height", "920px");
    $("#xgsz").click(function () {
        $.post('/app_check/set_check/', {
                "attendance": $("#attendance").val(),
                "absent": $("#absent").val(),
                "late": $("#late").val(),
                "leave": $("#leave").val(),
                "absent_number": $("#absent_number").val(),
                "late_number": $("#late_number").val(),
            },
            function (data, status) {
            ds = data.er;
            if (ds=='1'){
                $("#er").html('修改成功')
            }else if (ds == '0'){
                $("#er").html('修改失败')
            }
            });
        return false;
    });
});