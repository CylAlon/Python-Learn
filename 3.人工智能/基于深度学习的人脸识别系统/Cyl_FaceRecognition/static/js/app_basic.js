

$(document).ready(function () {


    function ks(){
        $.post('/app_basic/show_set/', {

        }, function (data, status) {
            $("#setzh").val(data.list);
        });

    }


    $("#set_clic1").click(function () {
        $('.nfs').slideDown('show');
        ks();
        return false;
    });
    $("#set_clic2").click(function () {
        $('.nfs').slideDown('show');
        ks();
    });
    $("#tc_button").click(function () {
        $('.nfs').slideUp('show')
    });
    $("#xg_button").click(function () {
       $.post('/app_basic/show_setqr/', {
            "setzh":$("#setzh").val(),
           "sstmm":$("#sstmm").val(),
           "qrsstmm":$("#qrsstmm").val(),
        }, function (data, status) {
           if (data.er=='0')
                $("#xgfl3").html('修改成功');
           else if (data.er=='1')
                $("#xgfl3").html('修改失败');
        });
       return false;
    });

    // $("#set_clic").click(function () {
    //     $.post('/app_basic/show_set/', {
    //         "zh": $('#setzh').val(),
    //         "mm": $('#sstmm').val(),
    //         "qrmm": $('#qrsstmm').val(),
    //     }, function (data, status) {
    //         remse(2);
    //         for (i = 0; i < data.list.length; i++) {
    //             ds = data.list[i];
    //             $("#se_3").append('<option class="tj" title=ds>' + ds + '</option>');
    //         }
    //     });
    //     return false;
    // });


});