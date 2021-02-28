/*浏览器窗口变化*/
function change_win(){
    var window_width = $(document.body).width();
    // alert(window_width)
    if (window_width < 1600) {

        $(".nav_hadder_w").css("width", "1600px");
        $(".menu_bar").hide("");
          $("#cm").css("margin-left", "0");
          // $("#ajcr").css("margin-left", "0");

    } else {

        $(".nav_hadder_w").css("width", "100%");
        $("#cm").css("margin-left", "295px");
        $(".menu_bar").show("");
    }
}

$(window).resize(function () {          //当浏览器大小变化时
change_win();
});
/*部分a标签点击事件*/
// var rota1_flag = true;
// var rota2_flag = true;

var rata_name = ["a1", "a2", "a3", "a4", "a5","a6","a7","a8"];
var rata_flag = [false, false, false, false, ,false,false,false,false];
var hidden_name = ["#hidden1", "#hidden2", "#hidden3", "#hidden4", "#hidden5","#hidden6","#hidden7","#hidden8"];
var rotal_name = ["#rota1", "#rota2", "#rota3", "#rota4", "#rota5","#rota6","#rota7","#rota8"];
$(document).ready(function () {
    $(".cl").click(function () {
        var val = $(this).attr("id");
        var index_flag = 100;
        for (i = 0; i < rata_name.length; i++) {
            if (rata_name[i] == val) {
                index_flag = i;
                rata_flag[index_flag]=!rata_flag[index_flag];
                break;
            }
        }
        if (index_flag != 100) {
            if (rata_flag[index_flag]==true){
                $(hidden_name[index_flag]).slideDown("show");
                $(rotal_name[index_flag]).css("transform", "rotate(90deg)");
            }
            else if (rata_flag[index_flag]==false){
                $(hidden_name[index_flag]).slideUp("show");
                $(rotal_name[index_flag]).css("transform", "rotate(0deg)");
            }
            for (i = 0; i < rata_name.length; i++){
                if (index_flag != i){
                    $(hidden_name[i]).slideUp("show");
                    $(rotal_name[i]).css("transform", "rotate(0deg)");
                    rata_flag[i]=false;
                }
            }
        }
    });

 //
 //    $(window).bind('beforeunload',function(){
 //        $.post('/app_login/loginout/', {
 //            "value1": $('#se_2').val(),
 //        }, function (data, status) {
 //        });
 //        return '确定离开此页面吗？';
 //    }
 //        );
 // $(window).unload(function(){
 //       $.post('/app_login/loginout/', {
 //            "value1": $('#se_2').val(),
 //        }, function (data, status) {
 //        });
 //        // return '确定离开此页面吗？';
 //    });




});
 $(function(){
      change_win();
 });