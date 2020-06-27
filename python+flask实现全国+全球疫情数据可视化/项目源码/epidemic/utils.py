import pymysql
from sqlalchemy import create_engine
import pandas as pd
import datetime
class utils:
    def __init__(self,db_name,table_name,user,password):
        self.db_name=db_name
        self.table_name=table_name
        self.user=user
        self.password=password
        self.data = self.querry()
    def get_conn(self):
        '''

        :return:连接
        '''
        #创建连接
        conn=pymysql.connect(host="127.0.0.1",port=3306,user=self.user,password=self.password,
                             db=self.db_name,charset="utf8")
        cursor=conn.cursor()
        return conn,cursor

    def close_conn(self,conn,cursor):
        cursor.close()
        conn.close()

    def querry(self):
        #使用pandas从数据库中读取疫情数据
        conn = create_engine('mysql://{}:{}@localhost:3306/{}?charset=utf8'.format(self.user,self.password,self.db_name))
        sql="SELECT * FROM {}".format(self.table_name)
        epidemic = pd.read_sql(sql, con=conn)
        return epidemic

    def get_c1_data(self):
        '''
        获取c1的四个数据：累计确诊、累计治愈、累计死亡、新增死亡
        :return:
        '''
        df=self.data
        #获取最新数据
        # 由于接口数据只能拿到前一天，因此我们的日期数据应该-1天
        t = datetime.datetime.now() + datetime.timedelta(days=-1)
        t= t.strftime('%Y-%m-%d')
        today = df[df.日期 == t]
        dignose=str(today.确诊.sum())
        heal=str(today.治愈.sum())
        dead=str(today.死亡.sum())
        add=str(today.新增死亡.sum())

        return [dignose,heal,dead,add]

    def get_c2_data(self):
        '''
        获取中国各省的疫情数据
        :return:
        '''
        #将地区-确诊人数以键值对的形式保存
        dict={}

        # 获取最新数据
        # 由于接口数据只能拿到前一天，因此我们的日期数据应该-1天
        df=self.data
        t = datetime.datetime.now() + datetime.timedelta(days=-1)
        t = t.strftime('%Y-%m-%d')
        today = df[df.日期 == t]
        for p,v in zip(today.疫情地区,today.确诊):
            dict[p]=v
        return dict

    def get_l1_data(self):
        '''
        获取疫情期间每日累计数据
        :return:
        '''
        df=self.data
        days=df.groupby("日期").sum()
        return days

    def get_l2_data(self):
        '''
        获取疫情期间每日新增数据
        :return:
        '''
        df=self.data
        days=df.groupby("日期").sum().diff().dropna()
        return days

    def get_r1_data(self):
        '''
        获取除湖北地区确诊人数最多的省份
        :return:
        '''
        dict={}
        df=self.data
        t = datetime.datetime.now() + datetime.timedelta(days=-1)
        t = t.strftime('%Y-%m-%d')
        today = df[df.日期 == t]
        #按确诊人数排序
        today=today.sort_values(by='确诊',ascending=False)[:6]
        for key,value in zip(today.疫情地区,today.确诊):
            if key=='湖北':
                continue
            dict[key]=value

        return dict

    def get_r2_data(self):
        '''
        获取世界各国的疫情数据
        :return:
        '''
        #将地区-确诊人数以键值对的形式保存
        dict={}

        # 获取最新数据
        # 由于接口数据只能拿到前一天，因此我们的日期数据应该-1天
        df=self.data
        t = datetime.datetime.now() + datetime.timedelta(days=-1)
        t = t.strftime('%Y-%m-%d')
        today = df[df.日期 == t]
        for p,v in zip(today.name,today.确诊):
            dict[p]=v
        return dict





if __name__=="__main__":
    u=utils("myspider","world_epidemic","root","123456")
    print(list(u.get_r1_data().values()))

