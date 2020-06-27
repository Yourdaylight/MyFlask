
function gettime() {
    $.ajax({
        url:"/time",
        timeout:10000,
        success:function (data) {
            $("#time").html(data)
        },
        error:function (xhr,type,errorThrown) {

        }
    })
}

function get_c1_data(){
       $.ajax({
        url:"/c1",
        timeout:10000,
        success:function (data) {
            $(".num h1").eq(0).text(data.dignose)
            $(".num h1").eq(1).text(data.heal)
            $(".num h1").eq(2).text(data.dead)
            $(".num h1").eq(3).text(data.newly_add)
        },
        error:function (xhr,type,errorThrown) {

        }
    })
}

function get_c2_data(){
    $.ajax({
        url:"/c2",
        timeout:10000,
        success:function (data) {
            ec_center_option.series[0].data=data.data
            ec_center.setOption(ec_center_option)
        },
        error:function (xhr,type,errorThrown) {

        }
    })
}

function get_l1_data(){
    $.ajax({
        url:"/l1",
        timeout:10000,
        success:function (data) {
            ec_left1_option.xAxis.data=data.days
            ec_left1_option.series[0].data=data.dignose
            ec_left1_option.series[1].data=data.heal
            ec_left1_option.series[2].data=data.dead
            ec_left1.setOption(ec_left1_option)
        },
        error:function (xhr,type,errorThrown) {

        }
    })
}

function get_l2_data(){
    $.ajax({
        url:"/l2",
        timeout:10000,
        success:function (data) {
            ec_left2_option.xAxis.data=data.days
            ec_left2_option.series[0].data=data.dignose
            ec_left2_option.series[1].data=data.heal
            ec_left2_option.series[2].data=data.dead
            ec_left2.setOption(ec_left2_option)
        },
        error:function (xhr,type,errorThrown) {

        }
    })
}

function get_r1_data(){
    $.ajax({
        url:"/r1",
        timeout:10000,
        success:function (data) {
            ec_right1_option.xAxis.data=data.keys
            ec_right1_option.series[0].data=data.values
            ec_right1.setOption(ec_right1_option)
        },
        error:function (xhr,type,errorThrown) {

        }
    })
}

function get_r2_data(){
    $.ajax({
        url:"/r2",
        timeout:10000,
        success:function (data) {
            ec_right2_option .series[0].data=data.data
            ec_right2.setOption(ec_right2_option)

        },
        error:function (xhr,type,errorThrown) {

        }
    })
}

gettime()

get_c1_data()
get_c2_data()
get_l1_data()
get_l2_data()
get_r1_data()
get_r2_data()
setInterval(gettime,1000)