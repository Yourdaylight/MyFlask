var ec_right2=echarts.init(document.getElementById("r2"),"dark")


var ec_right2_dataList=[{name: 'Afghanistan', value: 28397.812},
                {name: 'Angola', value: 19549.124},
                {name: 'Albania', value: 3150.143},
                {name: 'United Arab Emirates', value: 8441.537},
            ]
var ec_right2_option = {
    title: {
        text:"全球疫情大数据可视化",
        left: 'center',
        top: 'top'
    },
   // tooltip: {
   //      trigger: 'item',
   //      formatter: function (params) {
   //          var value = (params.value + '').split('.');
   //          value = value[0].replace(/(\d{1,3})(?=(?:\d{3})+(?!\d))/g, '$1,')
   //                  + '.' + value[1];
   //          return params.seriesName + '<br/>' + params.name + ' : ' + value;
   //      }
   //  },

    visualMap: {
        show:true,
        min: 0,
        max: 1500,
        left:'left',
        top:'bottom',
        textStyle:{fontsize:5},
        inRange: {
                    color: ['#e0ffff', '#9D3030']
                },
        splitList:[{start:10,end:999},
                    {start:1000,end:9999},
                    {start:10000,end:99999},
                    {start:100000,end:999999},
                    {start:1000000}]

    },

    series: [
        {
            name: 'infections',
            type: 'map',
            mapType: 'world',
            roam: true,
            itemStyle:{
                emphasis:{label:{show:true}}
            },
            data:ec_right2_dataList
        }
    ]
};

ec_right2.setOption(ec_right2_option)