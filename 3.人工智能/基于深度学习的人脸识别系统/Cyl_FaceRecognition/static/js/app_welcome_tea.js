$(document).ready(function () {
    $(".comment_div").css("height", "900px");
    $(function () {
        $(function () {
            $.post('/app_basic/show_ted/', {}, function (data, status) {
                ds = data.li1;
                for (i = 0; i < ds.length; i++) {
                    df = ds[i];
                    $('#gg_1').append('<option>' + df + '</option>');
                }

            });
        });
        return false;
    });


    function showtbtf2(url) {
        $.post('/app_basic/' + url + '/', {
            "value_kc1": $('#gg_1').val(),
            "value_kc2": $('#gg_2').val(),
        }, function (data, status) {
            ds = data.li;
            $("#gg_2 .po").remove();
            for (i = 0; i < ds.length; i++) {
                df = ds[i];
                $('#gg_2').append('<option class="po">' + df + '</option>');
            }
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

    $("#gg_1").change(function () {
        showtbtf2('show_te_std');
        return false;
    });
    $("#gg_2").change(function () {
        $.post('/app_basic/show_tecour/', {
            "value_kc1": $('#gg_1').val(),
            "value_kc2": $('#gg_2').val(),
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
        return false;
    });


    /*
     $("#imtl").css({
                "background": "url('/" + "" + "') no-repeat",
                "background-size": "100% 100%"
            });
            $("#imtl").css({
                "background": "url('/" + data.path + "') no-repeat",
                "background-size": "100% 100%"
            });
    * */


});