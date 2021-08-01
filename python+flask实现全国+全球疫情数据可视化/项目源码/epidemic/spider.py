# -*- coding: utf-8 -*-
# @Time    :2021/7/30 23:34
# @Author  :lzh
# @File    : new_spider.py
# @Software: PyCharm
import datetime

import pandas as pd
import requests
from sqlalchemy import create_engine

from translate import COUNTRIES_CH_EN_DICT


def traslate(word):
    '''
    将世界各国的中文名转化为英文
    '''
    return COUNTRIES_CH_EN_DICT.get(word, "未知地区")


# %%
def save_data(df, table_name, if_exists="append", need_translate=False):
    if need_translate:
        df['name'] = df['疫情地区'].apply(traslate)
    conn = create_engine('mysql://root:123456@localhost:3306/myspider?charset=utf8')
    pd.io.sql.to_sql(df, table_name, con=conn, if_exists=if_exists, index=None)


def crawl_china_data():
    url = "https://api.inews.qq.com/newsqa/v1/query/inner/publish/modules/list?modules=chinaDayList,chinaDayAddList,nowConfirmStatis,provinceCompare"
    data = requests.get(url)
    data = data.json().get("data", {})
    provinceCompare = data.get("provinceCompare")  # 每个省份的总数据（每日更新）
    chinaDayList = data.get("chinaDayList")  # 最近一个月的全国疫情的总数据
    chinaDayAddList = data.get("chinaDayAddList")  # 最近一个月的全国疫情的新增数据
    return provinceCompare, chinaDayList, chinaDayAddList


# %%
def crawl_countries_data():
    url = "https://api.inews.qq.com/newsqa/v1/automation/modules/list?modules=FAutoforeignList"
    data = requests.get(url)
    data = data.json().get("data")
    foreignList = data.get("FAutoforeignList", [])
    return foreignList


def parse_china_daily_data(day_list, day_add_list):
    """
    解析每日新增、每日累计数据
    :param api_rtn_data:
    :return:
    """
    day_df = pd.DataFrame(day_list)
    day_df["date"] = pd.to_datetime(day_df["y"] + "." + day_df["date"])
    day_add_df = pd.DataFrame(day_add_list)
    day_add_df["date"] = pd.to_datetime(day_add_df["y"] + "." + day_add_df["date"])
    save_data(day_df, "china_day", "append")
    save_data(day_add_df, "china_day_add", "append")


def parse_countries_total_data(api_rtn_data):
    """
    解析每个省份的新增数据
    :param api_rtn_data:
    :return:
    """
    dates = []
    countries = []
    dignose = []
    heal = []
    dead = []
    add = []
    for country in api_rtn_data:
        countries.append(country.get("name", ""))
        month, day = country.get("date").split(".")
        month = month if "0" not in month else month[-1]
        date = datetime.date(int(country.get("y")), int(month), int(day))
        dates.append(date)
        dignose.append(country.get("nowConfirm", 0))
        heal.append(country.get("heal", 0))
        dead.append(country.get("dead", 0))
        add.append(country.get("confirmAdd", 0))
    df = pd.DataFrame({
        "疫情地区": countries,
        "日期": dates,
        "确诊": dignose,
        "治愈": heal,
        "死亡": dead,
        "新增死亡": add
    })

    save_data(df, "world_epidemic", "replace", True)
    return df


def parse_provinces_total_data(api_rtn_data):
    dates = []
    provinces = []
    dignose = []
    heal = []
    dead = []
    add = []
    for province, total_data in api_rtn_data.items():
        provinces.append(province)
        date = datetime.datetime.now()
        dates.append(date)
        dignose.append(total_data.get("nowConfirm", 0))
        heal.append(total_data.get("heal", 0))
        dead.append(total_data.get("dead", 0))
        add.append(total_data.get("confirmAdd", 0))
    df = pd.DataFrame({
        "疫情地区": provinces,
        "日期": dates,
        "确诊": dignose,
        "治愈": heal,
        "死亡": dead,
        "新增死亡": add
    })
    save_data(df, 'china_total_epidemic')
    return df


# %%
def main():
    provinceCompare, chinaDayList, chinaDayAddList = crawl_china_data()
    parse_china_daily_data(chinaDayList, chinaDayAddList)
    parse_provinces_total_data(provinceCompare)
    parse_countries_total_data(crawl_countries_data())


if __name__ == '__main__':
    main()
    print("爬取完成")
