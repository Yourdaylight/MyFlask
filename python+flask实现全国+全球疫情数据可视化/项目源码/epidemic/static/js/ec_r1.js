var ec_right1=echarts.init(document.getElementById("r1"),"dark")

var ec_right1_option = {
    title: {
        text: '非湖北地区确诊人数top5',
        left: "left"
    },
    xAxis: {
        type: 'category',
        data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    },
    yAxis: {
        type: 'value'
    },
    series: [{
        data: [120, 200, 150, 80, 70, 110, 130],
        type: 'bar',
        showBackground: true,
        backgroundStyle: {
            color: 'rgba(220, 220, 220, 0.8)'
        }
    }]
};
ec_right1.setOption(ec_right1_option)