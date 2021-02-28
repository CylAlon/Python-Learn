$(document).ready(function () {

    $(".comment_div").css("height", "900px");

    function cl() {
        for (i = 0; i <15 ;i++){
            s = i + 2;
            q = i + 1;
            for (j = 0; j < 8; j++) {
                p = j + 1;
                $(".kqtab tr:nth-child(" + s + ") td:nth-child(" + p + ")").html('');
            }
        }
    }

    function showtab(ds) {
        for (i = 0; i < ds.length; i++) {
            s = i + 2;
            q = i + 1;
            for (j = 0; j < 7; j++) {
                p = j + 1;
                $(".kqtab tr:nth-child(" + s + ") td:nth-child(" + p + ")").html(ds[i][j]);
            }
            if (ds[i][7] == 0) {
                $(".kqtab tr:nth-child(" + s + ") td:nth-child(" + 8 + ")").html("出勤");
            } else if (ds[i][7] == 1) {
                $(".kqtab tr:nth-child(" + s + ") td:nth-child(" + 8 + ")").html("请假");
            } else if (ds[i][7] == 2) {
                $(".kqtab tr:nth-child(" + s + ") td:nth-child(" + 8 + ")").html("迟到");
            } else if (ds[i][7] == 3) {
                $(".kqtab tr:nth-child(" + s + ") td:nth-child(" + 8 + ")").html("缺勤");
            }
        }
    }
    function cl1() {
        for (i = 0; i <15 ;i++){
                    s = i + 2;
                    q = i + 1;
                    for (j = 0; j < 9; j++) {
                        p = j + 1;
                        $(".kqtab tr:nth-child(" + s + ") td:nth-child(" + p + ")").html('');
                    }
                }
    }
    function showtabt(ds) {

        for (i = 0; i < ds.length; i++) {
            s = i + 2;
            q = i + 1;
            for (j = 0; j < 8; j++) {
                p = j + 1;
                $(".kqtab tr:nth-child(" + s + ") td:nth-child(" + p + ")").html(ds[i][j]);
            }
            if (ds[i][8] == 0) {
                $(".kqtab tr:nth-child(" + s + ") td:nth-child(" + 9 + ")").html("出勤");
            } else if (ds[i][8] == 1) {
                $(".kqtab tr:nth-child(" + s + ") td:nth-child(" + 9 + ")").html("请假");
            } else if (ds[i][8] == 2) {
                $(".kqtab tr:nth-child(" + s + ") td:nth-child(" + 9 + ")").html("迟到");
            } else if (ds[i][8] == 3) {
                $(".kqtab tr:nth-child(" + s + ") td:nth-child(" + 9 + ")").html("缺勤");
            }
        }
    }


    function remse(se) {
        for (var i = 1; i < 15; i++) {
            var na = "#bb_" + i;
            if ($(na + " .qc") && i > se)
                $(na + " .qc").remove();
        }
    }

//页面加载后载访问获取信息  该页面独有
    $(function () {
        $.post('/app_statement/show_allkq/', {
        }, function (data, status) {
            ds = data.list;

            for (i = 0; i < ds.length; i++) {
                showtab(ds)
            }
            dt = data.li;

            for (i = 0; i < dt.length; i++) {
                df = dt[i];
                $('#bb_1').append('<option>' + df + '</option>');
                // $('#kc1').append('<option>' + df + '</option>');
            }
            dt = data.li2;
            for (i = 0; i < dt.length; i++) {
                df = dt[i];
                $('#bb_2').append('<option>' + df + '</option>');
            }
            dt = data.li3;
            for (i = 0; i < dt.length; i++) {
                df = dt[i];
                $('#bb_3').append('<option>' + df + '</option>');
            }
            dt = data.li4;
            for (i = 0; i < dt.length; i++) {
                df = dt[i];
                $('#bb_4').append('<option>' + df + '</option>');
            }
            dt = data.li5;
            for (i = 0; i < dt.length; i++) {
                df = dt[i];
                $('#bb_5').append('<option>' + df + '</option>');
            }
            dt = data.li6;
            for (i = 0; i < dt.length; i++) {
                df = dt[i];
                $('#bb_6').append('<option>' + df + '</option>');
            }
        });

        $.post('/app_statement/show_allcl/', {
        }, function (data, status) {
            ds = data.list;

            for (i = 0; i < ds.length; i++) {
                showtabt(ds)
            }
            dt = data.li1;

            for (i = 0; i < dt.length; i++) {
                df = dt[i];
                $('#cc_1').append('<option>' + df + '</option>');
                // $('#kc1').append('<option>' + df + '</option>');
            }
            dt = data.li2;
            for (i = 0; i < dt.length; i++) {
                df = dt[i];
                $('#cc_2').append('<option>' + df + '</option>');
            }
            dt = data.li3;
            for (i = 0; i < dt.length; i++) {
                df = dt[i];
                $('#cc_3').append('<option>' + df + '</option>');
            }
            dt = data.li4;
            for (i = 0; i < dt.length; i++) {
                df = dt[i];
                $('#cc_4').append('<option>' + df + '</option>');
            }
            dt = data.li5;
            for (i = 0; i < dt.length; i++) {
                df = dt[i];
                $('#cc_5').append('<option>' + df + '</option>');
            }
            dt = data.li6;
            for (i = 0; i < dt.length; i++) {
                df = dt[i];
                $('#cc_6').append('<option>' + df + '</option>');
            }
            dt = data.li7;
            for (i = 0; i < dt.length; i++) {
                df = dt[i];
                $('#cc_7').append('<option>' + df + '</option>');
            }
        });
        return false;
    });

    function showtb(url){
        $.post('/app_statement/'+url+'/', {
            "value1": $('#bb_1').val(),
            "value2": $('#bb_6').val(),
            "value3": $('#bb_2').val(),
            "value4": $('#bb_3').val(),
            "value5": $('#bb_4').val(),
            "value6": $('#bb_5').val(),
        }, function (data, status) {
            ds = data.list;
            cl();
            for (i = 0; i < ds.length; i++) {
                showtab(ds)
            }
        });
    }
    $("#bb_1").change(function () {
        showtb('show_cour');
        return false;
    });

    $("#bb_2").change(function () {
        showtb('show_week');
        return false;
    });
    $("#bb_3").change(function () {
        showtb('show_day');
        return false;
    });
    $("#bb_4").change(function () {
        showtb('show_num');
        return false;
    });
    $("#bb_5").change(function () {
        showtb('show_state');
        return false;
    });


    $("#nextpage").click(function () {
        $.post('/app_statement/show_page/', {
                "flag": "0",
                "value1": $('#bb_1').val(),
                "value2": $('#bb_6').val(),
                "value3": $('#bb_2').val(),
                "value4": $('#bb_3').val(),
                "value5": $('#bb_4').val(),
                "value6": $('#bb_5').val(),
            },
            function (data, status) {
            ds = data.list;

            showtab(ds);
            });
        return false;
    });
    $("#lastpage").click(function () {
        $.post('/app_statement/show_page/', {
                "flag": "1",
                "value1": $('#bb_1').val(),
                "value2": $('#bb_6').val(),
                "value3": $('#bb_2').val(),
                "value4": $('#bb_3').val(),
                "value5": $('#bb_4').val(),
                "value6": $('#bb_5').val(),
            },
            function (data, status) {
            ds = data.list;
            showtab(ds);
            });
        return false;
    });

//    ****************************************************************************

    function showtbt(url){
        $.post('/app_statement/'+url+'/', {
            "value1": $('#cc_1').val(),
            "value2": $('#cc_2').val(),
            "value3": $('#cc_3').val(),
            "value4": $('#cc_4').val(),
            "value5": $('#cc_5').val(),
            "value6": $('#cc_6').val(),
            "value7": $('#cc_7').val(),
        }, function (data, status) {
            ds = data.list;
            cl1();
            for (i = 0; i < ds.length; i++) {
                showtabt(ds)
            }
        });
    }
    $("#cc_1").change(function () {
        showtbt('show_court');
        return false;
    });
    $("#cc_2").change(function () {
        showtbt('show_stut');
        return false;
    });

    $("#cc_4").change(function () {
        showtbt('show_weekt');
        return false;
    });
    $("#cc_5").change(function () {
        showtbt('show_dayt');
        return false;
    });
    $("#cc_6").change(function () {
        showtbt('show_numt');
        return false;
    });
    $("#cc_7").change(function () {
        showtbt('show_statet');
        return false;
    });

    $("#nextpage1").click(function () {
        $.post('/app_statement/show_paget/', {
                "flag": "0",
                "value1": $('#cc_1').val(),
                "value2": $('#cc_2').val(),
                "value3": $('#cc_3').val(),
                "value4": $('#cc_4').val(),
                "value5": $('#cc_5').val(),
                "value6": $('#cc_6').val(),
                "value7": $('#cc_7').val(),
            },
            function (data, status) {
            ds = data.list;
            showtabt(ds);
            });
        return false;
    });
    $("#lastpage1").click(function () {
        $.post('/app_statement/show_paget/', {
                "flag": "1",
                "value1": $('#cc_1').val(),
                "value2": $('#cc_2').val(),
                "value3": $('#cc_3').val(),
                "value4": $('#cc_4').val(),
                "value5": $('#cc_5').val(),
                "value6": $('#cc_6').val(),
                "value7": $('#cc_7').val(),
            },
            function (data, status) {
            ds = data.list;
            showtabt(ds);
            });
        return false;
    });





});