$(document).ready(function () {

    $(".comment_div").css("height", "1300px");
    //改变长度


    //页面加载后载访问获取信息  该页面独有
    $(function () {

        $.post('/app_check/show_college/', {}, function (data, status) {
            for (i = 0; i < data.list.length; i++) {
                ds = data.list[i];
                $('#se_1').append('<option>' + ds + '</option>');
            }
        });
        return false;
    });

    function remse(se) {
        for (var i = 1; i < 5; i++) {
            var na = "#se_" + i;
            if ($(na + " .tj") && i > se)
                $(na + " .tj").remove();
        }
    }


    $("#se_1").change(function () {
        // change_selc("#se_1", "#se_2", "show_week")
        $.post('/app_check/show_week/', {
            "value1": $('#se_1').val(),
        }, function (data, status) {
            remse(1);
            for (i = 0; i < data.list.length; i++) {
                ds = data.list[i];
                $("#se_2").append('<option class="tj" title=ds>' + ds + '</option>');
            }
        });
        return false;
    });
    $("#se_2").change(function () {
        $.post('/app_check/show_day/', {
            "value1": $('#se_2').val(),
        }, function (data, status) {
            remse(2);
            for (i = 0; i < data.list.length; i++) {
                ds = data.list[i];
                $("#se_3").append('<option class="tj" title=ds>' + ds + '</option>');
            }
        });
        return false;
    });
    $("#se_3").change(function () {
        $.post('/app_check/show_num/', {
            "value1": $('#se_3').val(),
        }, function (data, status) {
            remse(3);
            for (i = 0; i < data.list.length; i++) {
                ds = data.list[i];
                $("#se_4").append('<option class="tj" title=ds>' + ds + '</option>');
            }
        });
        return false;
    });

    function instainfo(ds) {
        for (i = 0; i < 5; i++) {
            s = i + 2;
            q = i + 1;
            for (j = 0; j < 7; j++) {
                p = j + 1;
                $(".stutb tr:nth-child(" + s + ") td:nth-child(" + p + ")").html('');
            }
        }

        for (var i = 0; i < ds.length; i++) {
            s = i + 2;
            q = i + 1;
            $(".stutb tr:nth-child(" + s + ") td:nth-child(1)").css({
                "background": "url('/static/" + ds[i][0] + "') no-repeat",
                "background-size": "100% 100%"
            });
            $(".stutb tr:nth-child(" + s + ") td:nth-child(2)").html(ds[i][1]);
            $(".stutb tr:nth-child(" + s + ") td:nth-child(3)").html(ds[i][2]);
            $(".stutb tr:nth-child(" + s + ") td:nth-child(4)").html(ds[i][3]);

            bs = ds[i][4];
            bp = '';

            if (bs == '0') {
                bp = '出勤';
                $(".stutb tr:nth-child(" + s + ") td:nth-child(5)").css("color", "blue");

            } else if (bs == '1') {
                bp = '请假';
                $(".stutb tr:nth-child(" + s + ") td:nth-child(5)").css("color", "#4cae4c");

            } else if (bs == '2') {
                bp = '迟到';
                $(".stutb tr:nth-child(" + s + ") td:nth-child(5)").css("color", "#46b8da");
            } else if (bs == '3') {
                bp = '缺勤';
                $(".stutb tr:nth-child(" + s + ") td:nth-child(5)").css("color", "red");
            }

            $(".stutb tr:nth-child(" + s + ") td:nth-child(5)").html(bp);

            $(".stutb tr:nth-child(" + s + ") td:nth-child(6) ").html(
                '<button type="submit" class="btn btn-primary cq">出勤</button>'
            );

            $(".stutb tr:nth-child(" + s + ") td:nth-child(7) ").html(
                '<button type="submit" class="btn btn-danger qq">缺勤</button>'
            );
            $(".stutb tr:nth-child(" + s + ") td:nth-child(8) ").html(
                '<button type="submit" class="btn btn-success qj">请假</button>'
            );
            $(".stutb tr:nth-child(" + s + ") td:nth-child(9) ").html(
                '<button type="submit" class="btn btn-info cd">迟到</button>'
            );
            $(".qdx" + q).attr('id', ds[i][1]);
            // $(".stutb tr:nth-child(" + s + ") td:nth-child(6) ").html(


            //
            // '<ul class="pagination bj">'+
            //     '<li class="ggg">'+
            // '<a href="#" class="cq" id="+ds[i][1]+">出勤' + '</a>'+
            // '<li/>'+
            // '<li>'+
            // '<a href="#" class="qq" id="+ds[i][1]+">缺勤' + '</a>'+
            // '<li/>'+
            // '<li>'+
            // '<a href="#" class="qj" id="+ds[i][1]+">请假' + '</a>'+
            // '<li/>'+
            // '<li>'+
            // '<a href="#" class="cd" id="+ds[i][1]+">迟到' + '</a>'+
            //     '<li/>'+
            //     '</ul>'

            // '<form action="" method="post">'+
            // {% csrf_token %}+
            //     <button type="submit" class="btn btn-primary cq">出勤</button>
            //     <button type="submit" class="btn btn-danger qq">缺勤</button>
            //     <button type="submit" class="btn btn-success qj">请假</button>
            //     <button type="submit" class="btn btn-info cd">迟到</button>
            // '</form>'
            // '</div>'+
            // '</div>'
            // );
            // $(".stutb tr:nth-child(" + s + ") td:nth-child(5) #qdzt").html(ds[i][1]);

            // $(".stutb tr:nth-child(" + s + ") td:nth-child(5)").html('<a href="#">详情' + '</a>' + '<p hidden class="np">' + ds[i][1] + '</p>');
        }
    }

    $("#chick_button").click(function () {
        $.post('/app_check/show_conf/', {
            "value2": $('#se_2').val(),
            "value3": $('#se_3').val(),
            "value4": $('#se_4').val(),
        }, function (data, status) {

            ds = data.list;
            instainfo(ds);

        });

        return false;
    });

    $("#qc_button").click(function () {
        remse(0);
    });
    //********************************************************************
    $("#kaoqin").click(function () {
        $.post('/app_check/show_kaoqin/', {
            "value1": $('#se_2').val(),
        }, function (data, status) {
            $("#errinf").html('已经签到人数: ' + data.number);
            $("#errinf").css("color", "black");

            ds = data.list;
            for (var i = 0; i < ds.length; i++) {
                s = i + 2;
                bs = ds[i][4];
                bp = '';

                if (bs == '0') {
                    bp = '出勤';
                    $(".stutb tr:nth-child(" + s + ") td:nth-child(5)").css("color", "blue");

                } else if (bs == '1') {
                    bp = '请假';
                    $(".stutb tr:nth-child(" + s + ") td:nth-child(5)").css("color", "#4cae4c");

                } else if (bs == '2') {
                    bp = '迟到';
                    $(".stutb tr:nth-child(" + s + ") td:nth-child(5)").css("color", "#46b8da");
                } else if (bs == '3') {
                    bp = '缺勤';
                    $(".stutb tr:nth-child(" + s + ") td:nth-child(5)").css("color", "red");
                }

                $(".stutb tr:nth-child(" + s + ") td:nth-child(5)").html(bp);
            }


        });
        return false;
    });

    $("#ripage").click(function () {
        $.post('/app_check/show_pagetrun/', {
                "flag": "1",
            },
            function (data, status) {
                ds = data.list;
                if (data.errr == '1') {  //***************这个没有用 展示显示不出来  后期删掉
                    $("#errr").html('没有学生了')
                } else {
                    $("#errr").html('')
                }
                instainfo(ds);
            });
        return false;
    });
    $("#lipage").click(function () {
        $.post('/app_check/show_pagetrun/', {
                "flag": "0",
            },
            function (data, status) {
                ds = data.list;
                if (data.errr == '1') {  //***************这个没有用 展示显示不出来  后期删掉
                    $("#errr").html('没有学生了')
                } else {
                    $("#errr").html('')
                }
                instainfo(ds);
            });
        return false;
    });
    // $(".qdxq").click(function () {
    //     var dat = $(".np").html();
    //     $.post('/app_check/show_deta/', {
    //             "nstid": dat,
    //         },
    //         function (data, status) {
    //             ds = data.state;
    //             did = data.stid;
    //             if (ds == 0) {
    //                 $("#sstid").html(did);
    //                 $("#qdzt").html('出勤');
    //
    //             } else if (ds == 1) {
    //                 $("#sstid").html(did);
    //                 $("#qdzt").html('请假');
    //             } else if (ds == 2) {
    //                 $("#sstid").html(did);
    //                 $("#qdzt").html('迟到');
    //             } else if (ds == 3) {
    //                 $("#sstid").html(did);
    //                 $("#qdzt").html('缺勤');
    //             }
    //
    //             $("#ffc").slideDown('show');
    //         });
    //     return false;
    // });

    $("#qdgb").click(function () {


        $.post('/app_check/show_gb/', {
                "kgfl": 1,

            },
            function (data, status) {
                $("#ffc").slideUp('show');
            });
        return false;
    });

    $(".qdxq1").click(function () { //点击出勤
        var dat = $(this).attr("id");
        $.post('/app_check/show_xq/', {
                "xqflag": "0",
                "nstid": dat,
            },
            function (data, status) {
                bp = '出勤';
                s = data.num;
                $(".stutb tr:nth-child(" + s + ") td:nth-child(5)").html('');
                $(".stutb tr:nth-child(" + s + ") td:nth-child(5)").css("color", "blue");
                $(".stutb tr:nth-child(" + s + ") td:nth-child(5)").html(bp);
            });
        // return false;
    });
    $(".qdxq2").click(function () {
        var dat = $(this).attr("id");
        $.post('/app_check/show_xq/', {
                "xqflag": "3",
                "nstid": dat,
            },
            function (data, status) {
                bp = '缺勤';
                s = data.num;
                $(".stutb tr:nth-child(" + s + ") td:nth-child(5)").html('');
                $(".stutb tr:nth-child(" + s + ") td:nth-child(5)").css("color", "red");
                $(".stutb tr:nth-child(" + s + ") td:nth-child(5)").html(bp);
            });
        return false;
    });
    $(".qdxq3").click(function () {
        var dat = $(this).attr("id");
        $.post('/app_check/show_xq/', {
                "xqflag": "1",
                "nstid": dat,
            },
            function (data, status) {

                bp = '请假';
                s = data.num;
                $(".stutb tr:nth-child(" + s + ") td:nth-child(5)").html('');
                $(".stutb tr:nth-child(" + s + ") td:nth-child(5)").css("color", "#4cae4c");
                $(".stutb tr:nth-child(" + s + ") td:nth-child(5)").html(bp);
            });
        return false;
    });
    $(".qdxq4").click(function () {
        var dat = $(this).attr("id");
        $.post('/app_check/show_xq/', {
                "xqflag": "2",
                "nstid": dat,
            },
            function (data, status) {
                bp = '迟到';
                s = data.num;
                $(".stutb tr:nth-child(" + s + ") td:nth-child(5)").html('');
                $(".stutb tr:nth-child(" + s + ") td:nth-child(5)").css("color", "#46b8da");
                $(".stutb tr:nth-child(" + s + ") td:nth-child(5)").html(bp);
            });
        return false;
    });


});

