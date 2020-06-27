from pyecharts import Bar
# from snapshot_selenium import snapshot
# from pyecharts.render import make_snapshot
columns = ['大大的三个字', '这里一共是十个字的吧', '这里一共是十个字的吧（这里是七个字）', '其他', '十全十美的十个字啊', 'python仪表盘', '快乐三个字', '可乐续保三个字', '骑缝三个字',
           '里面好玩三个字', '信用卡三个字', '没空理我的', '订单问问三个字', '紫金学习三个字', '袋鼠妈妈三个字', '楼面价微信交流群', '密码三个字', '看见了来看看了解是是是',
           '大门口流量数据', '烤面筋解决三个字', '到读到蓝莓味']
# # 设置数据
data1 = [841, 0, 136, 0, 3317, 784, 1, 19, 691, 131, 21, 6461, 123, 0, 692, 0, 0, 0, 0, 0, 0]
data2 = [13056, 16614, 701, 0, 5815, 4274, 256, 689, 13838, 21723, 0, 16073, 28297, 0, 279, 463, 25261, 60400, 0, 2493,
         16]
# # 设置柱状图的主标题与副标题
bar = Bar("这里是大标题", "这里上介绍文字",width=1200,height=600)
# # 添加柱状图的数据及配置项
def label_formatter(params):
    return str(params.value)+"\t\t"
bar.add("外网", columns, data1, bar_category_gap='10%',label_formatter=label_formatter,xaxis_label_textsize=6,grid_bottom=500,label_text_size=8,is_label_show=True,xaxis_rotate=30)
bar.add("内网", columns, data2,bar_category_gap='10%',label_formatter=label_formatter,xaxis_label_textsize=6,grid_bottom=500,label_text_size=8,is_label_show=True, xaxis_rotate=30)
print(help(bar))
# # 生成本地文件（默认为.html文件）
bar.render('tesss.jpg')
# make_snapshot(snapshot, bar.render(), "003_Options配置项_自定义样式_保存图片.png")