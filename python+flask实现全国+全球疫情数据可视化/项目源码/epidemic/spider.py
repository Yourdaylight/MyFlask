import requests
import pandas as pd
import json
from sqlalchemy import create_engine

url='https://voice.baidu.com/newpneumonia/get?target=trend&isCaseIn=0&stage=publish&callback=jsonp_1593074577909_83653'
r=requests.get(url).text

#标准化字符串为json格式
r=r.replace("jsonp_1593074577909_83653(","")
r=r[0:-2]
r=json.loads(r)

names=[]
dates=[]
dignose=[]
heal=[]
dead=[]
add=[]
#遍历每个地点
for place in r['data']:
#     print(place['name'])
    length=len(place['trend']['updateDate'])
    place_name=(place['name'] for i in range(length))
    names.extend(place_name)
    #获取日期数据
    dates.extend(place['trend']['updateDate'])
    for trend in place['trend']['list']:
        if(trend['name']=='确诊'):
            dignose.extend(trend['data'])
        if(trend['name']=='治愈'):
            heal.extend(trend['data'])
        if(trend['name']=='死亡'):
            dead.extend(trend['data'])
        if(trend['name']=='新增确诊'):
            add.extend(trend['data'])

#新增确诊数据如果存在缺失值，则将缺失值填充为0
diff=len(names)-len(add)
if(diff!=0):
    add=add+[0 for i in range(diff)]
print(len(names),len(dates),len(dignose),len(heal),len(dead),len(add))

# 将数据保存至数据库中
df=pd.DataFrame({
    "疫情地区":names,
    "日期":dates,
    "确诊":dignose,
    "治愈":heal,
    "死亡":dead,
    "新增死亡":add
})
df['日期']=['2020.'+i for i in df['日期']]
df['日期']=df['日期'].str.replace(".","-")
df['日期']=pd.to_datetime(df['日期'])
conn = create_engine('mysql://root:123456@localhost:3306/myspider?charset=utf8')
pd.io.sql.to_sql(df,'epidemic',con=conn,if_exists = 'replace',index=None)