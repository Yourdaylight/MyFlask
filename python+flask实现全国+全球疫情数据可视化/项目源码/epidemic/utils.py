import datetime
import traceback

import pandas as pd
import pymysql
from sqlalchemy import create_engine


class utils:
    def __init__(self, db_name, user, password):
        self.db_name = db_name
        self.user = user
        self.password = password
        self.data = self.query("epidemic")

    def get_conn(self):
        '''

        :return:连接
        '''
        # 创建连接
        conn = pymysql.connect(host="127.0.0.1", port=3306, user=self.user, password=self.password,
                               db=self.db_name, charset="utf8")
        cursor = conn.cursor()
        return conn, cursor

    def close_conn(self, conn, cursor):
        cursor.close()
        conn.close()

    def query(self, table_name, use_sql=None):
        """
        :param sql:
        :return:epidemic: DataFrame
        """
        # 使用pandas从数据库中读取疫情数据
        try:
            conn = create_engine('mysql://{}:{}@localhost:3306/{}?charset=utf8'.format(self.user, self.password, self.db_name))
            sql = use_sql if use_sql else "select * from {}".format(table_name)
            epidemic = pd.read_sql(sql, con=conn)
            return epidemic
        except Exception as e:
            traceback.print_exc(e)
            return None

    def get_c1_data(self):
        '''
        获取c1的四个数据：累计确诊、累计治愈、累计死亡、新增死亡
        :return:
        '''
        sql = "select date, confirm, nowConfirm,heal,dead from china_day order by date desc limit 1"
        df = self.query("china_day", sql)
        confirm = int(df["confirm"][0])
        heal = int(df["heal"][0])
        dead = int(df["dead"][0])
        now_confirm = int(df["nowConfirm"][0])

        return [confirm, heal, dead, now_confirm]

    def get_c2_data(self):
        '''
        获取中国各省的疫情数据
        :return:
        '''
        # 将地区-确诊人数以键值对的形式保存
        dict = {}

        # 获取最新数据
        # 从数据库中获取最近一次更新的数据
        sql = "select distinct 疫情地区,日期,确诊 from china_total_epidemic order by 日期 desc limit 34"
        df = self.query("china_total_epidemic", sql)
        for p, v in zip(df.疫情地区, df.确诊):
            dict[p] = v
        return dict

    def get_l1_data(self):
        '''
        获取疫情期间每日累计数据
        :return:
        '''
        sql = "select date, confirm, heal,dead from china_day order by date desc"
        df = self.query("", sql)
        return df

    def get_l2_data(self):
        '''
        获取疫情期间每日新增数据
        :return:
        '''
        sql = "select date, confirm,heal,dead from china_day_add order by date desc"
        df = self.query("",sql)
        return df

    def get_r1_data(self):
        '''
        获取除湖北地区确诊人数最多的省份
        :return:
        '''
        sql = "select 疫情地区,确诊 from world_epidemic order by 日期 desc limit 5"
        df = self.query("",sql)
        return df

    def get_r2_data(self):
        '''
        获取世界各国的疫情数据
        :return:
        '''
        df = self.query("world_epidemic")
        return df[["name","疫情地区","确诊"]]


if __name__ == "__main__":
    u = utils("myspider", "root", "123456")

    u.get_c1_data()
