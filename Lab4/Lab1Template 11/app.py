#!/usr/local/bin/python

from flask import Flask, render_template, request, jsonify,session,redirect,json,url_for
import MySQLdb


app = Flask(__name__, static_url_path='')
#app.debug = True

app.secret_key = '123456'

def get_db():
    db = MySQLdb.connect(
    host = "dursley.socs.uoguelph.ca",
    user="yhuang20",
    passwd="1008239",
    db="yhuang20")

    return db

def querry(sql):
    db=get_db()
    cur=db.cursor()
    cur.execute(sql)
    rs=cur.fetchall()
    return rs



@app.route('/')
def index(name=None):
    return render_template('index.html', name=name)

@app.route('/index')
def index2(name=None):
    return render_template('index.html', name=name)

@app.route('/user', methods=['POST','GET'])
def user():
    if request.method == 'POST':
        mydata=dict(request.get_json())
        username=mydata['username']
        password=mydata['password']
        sql="select * from UserTable where username='{}' and password='{}'".format(username,password)
        rs=querry(sql)
        if len(rs)!=0:
            session['username']=username
            return jsonify({"username":username,"msg":0})
        else:
            return jsonify({"msg": 1})

        return render_template('index.html')

@app.route('/logout', methods=['POST','GET'])
def logout():
   # remove the username from the session if it is there
   print("===============================")
   if request.method == 'POST':
       session.pop('username', None)
       return redirect(url_for('index'))

@app.route('/user1', methods=['PUT','DELETE'])
def user1():
    if request.method == 'PUT':
        result = request.get_json()
        return jsonify(result)
    return render_template('index.html')

if __name__=="__main__":
    app.run()
