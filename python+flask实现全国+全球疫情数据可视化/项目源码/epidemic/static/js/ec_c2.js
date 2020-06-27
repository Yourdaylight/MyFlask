var ec_center=echarts.init(document.getElementById("c2"),"dark")

var dataList=[{'name':'上海','value':318},{'name':'云南','value':100}]




var ec_center_option = {
            tooltip: {
                    formatter:function(params,ticket, callback){
                        return params.seriesName+'<br />'+params.name+'：'+params.value
                    }
                },
            visualMap: {
                min: 0,
                max: 1500,
                left: 'left',
                top: 'bottom',
                textStyle:{fontsize:8},
                inRange: {
                    color: ['#e0ffff', '#9D3030']
                },
                show:true,
                splitList:[{start:1,end:9},
                    {start:10,end:99},
                    {start:100,end:999},
                    {start:1000,end:9999},
                    {start:10000}]
            },
            geo: {
                map: 'china',
                roam: false,
                zoom:1.23,
                label: {
                    normal: {
                        show: true,
                        fontSize:'10',
                        color: 'rgba(0,0,0,0.7)'
                    }
                },
                itemStyle: {
                    normal:{
                        borderColor: 'rgba(0, 0, 0, 0.2)'
                    },
                    emphasis:{
                        areaColor: '#F3B329',
                        shadowOffsetX: 0,
                        shadowOffsetY: 0,
                        shadowBlur: 20,
                        borderWidth: 0,
                        shadowColor: 'rgba(0, 0, 0, 0.5)'
                    }
                }
            },
            series : [
                {
                    name: '累计确诊',
                    type: 'map',
                    geoIndex: 0,
                    data:dataList
                }
            ]
        };

ec_center.setOption(ec_center_option)