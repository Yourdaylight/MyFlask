#!/usr/local/bin/python

from flask import Flask, render_template, request, jsonify
import MySQLdb


app = Flask(__name__, static_url_path='')
#app.debug = True


def get_db():
    db = MySQLdb.connect(
    host = "dursley.socs.uoguelph.ca",
    user="yhuang20",
    passwd="1008239",
    db="yhuang20")
    return db;



@app.route('/')
def index(name=None):
    return render_template('index.html', name=name)

@app.route('/user', methods=['POST','GET'])
def user():
    if request.method == 'POST':
        print(request.form.get("username"))
        result = request.get_json()

        return jsonify(result)

    return render_template('index.html')

@app.route('/user1', methods=['PUT','DELETE'])
def user1():
    if request.method == 'PUT':

        result = request.get_json()
        return jsonify(result)
    return render_template('index.html')

if __name__=="__main__":
    app.run()
