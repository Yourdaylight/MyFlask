import time

from flask import Flask
from flask import jsonify
from flask import render_template

import utils

app = Flask(__name__)

# 工具类，初始化参数为数据库名，数据库表名，数据库账号，数据库密码
u = utils.utils("myspider", "root", "123456")


@app.route('/')
def hello_world():
    return render_template("main.html")


@app.route('/time')
def get_time():
    time_str = time.strftime("%Y{}%m{}%d{}%X")
    return time_str.format("年", "月", "日")


@app.route('/c1')
def get_c1_data():
    data = u.get_c1_data()
    print(data)
    return jsonify({"dignose": data[0], "heal": data[1], "dead": data[2], "newly_add": data[3]})


@app.route('/c2')
def get_c2_data():
    res = []
    data = u.get_c2_data()
    for key, value in data.items():
        res.append({"name": key, "value": value})
    return jsonify({"data": res})


@app.route('/l1')
def get_l1_data():
    data = u.get_l1_data()
    day = data.date.tolist()
    dignose = data.confirm.tolist()
    heal = data.heal.tolist()
    dead = data.dead.tolist()
    return jsonify({"days": day, "dignose": dignose, "heal": heal, "dead": dead})


@app.route('/l2')
def get_l2_data():
    data = u.get_l2_data()
    day = data.date.tolist()
    dignose = data.confirm.tolist()
    heal = data.heal.tolist()
    dead = data.dead.tolist()
    return jsonify({"days": day, "dignose": dignose, "heal": heal, "dead": dead})


@app.route('/r1')
def get_r1_data():
    data = u.get_r1_data()
    keys = data.疫情地区.tolist()
    values = data.确诊.tolist()
    return jsonify({"keys": keys, "values": values})


@app.route('/r2')
def get_r2_data():
    res = []
    data = u.get_r2_data()
    for key, value in zip(data.name,data.确诊):
        res.append({"name": key, "value": value})
    # 还需要添加中国的总数据
    china = int(u.get_c1_data()[0])
    res.append({"name": "China", "value": china})
    return jsonify({"data": res})


if __name__ == '__main__':
    app.run()
