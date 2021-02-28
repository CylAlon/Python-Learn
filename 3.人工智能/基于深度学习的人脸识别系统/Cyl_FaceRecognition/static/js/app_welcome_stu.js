$(document).ready(function () {
    $(".comment_div").css("height", "900px");
    $(function () {
        $(function () {
            $.post('/app_basic/show_stud/', {}, function (data, status) {
                ds = data.list;
                for (i = 0 ; i <ds.length ; i++){
                    df = ds[i];
                    $('#ff_1').append('<option>' + df + '</option>');
                }
            });
        });
        return false;
    });



    function showtbtf1(url){
        $.post('/app_basic/'+url+'/', {
            "value_kc1": $('#ff_1').val(),
        }, function (data, status) {
            $("#imtl").css({
                "background": "url('/" + "" + "') no-repeat",
                "background-size": "100% 100%"
            });
            $("#imtl").css({
                "background": "url('/" + data.path + "') no-repeat",
                "background-size": "100% 100%"
            });
        });
    }
    $("#ff_1").change(function () {
        showtbtf1('show_tb1');
        return false;
    });


});