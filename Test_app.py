import os
from flask import Flask, request, render_template, url_for, session, redirect, flash
#from sqlalchemy import ForeignKey
from datetime import datetime



import requests



app = Flask(__name__)



@app.route("/")
def home():
	return render_template('index.html')

@app.route("/dashboard/")
def index():
	return redirect(url_for('r_d_operations'))



if __name__ == '__main__':
	#if DEBUG_DATABASE:
	#	db.create_all()
	app.secret_key = 'test app secret key'
	#login = LoginManager(app)
#login.login_view = 'login'
	#login.init_app(app)
	#login.login_view = 'login'
	app.run(host='0.0.0.0')
