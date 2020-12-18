from flask import Flask, render_template,redirect, url_for, request, session
from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime
import hashlib
import time

import mysql.connector
app = Flask(__name__)
app.config['SECRET_KEY'] = 'januar2020'
mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="",
	database="raspored"
    )
@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')


@app.route('/raspored')
def raspored():

	mc = mydb.cursor()
	mc.execute("SELECT * FROM raspored")
	res = mc.fetchall()

	mc.execute("SELECT DISTINCT nastavnik FROM raspored")
	nas = mc.fetchall()
	mc.execute("SELECT DISTINCT grupe FROM raspored")
	grp = mc.fetchall()
	return render_template('raspored.html', bosko="Bosko Jugovic s30-16", predmeti=res,nastavnik=nas,grupe=grp)


if __name__ == '__main__':
	app.run(debug=True)


