import os
from flask import Flask, request, render_template, url_for, session, redirect, flash
from datetime import datetime
from Config import dataFolder
from DataModel import DataModel


import requests



app = Flask(__name__)
dataModel = DataModel(dataFolder)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/dashboard/")
def dashboard():
    parameters = dataModel.getDailyTrackablesList()
    print(parameters)
    return render_template('dashboard.html')


if __name__ == '__main__':
	app.secret_key = 'test app secret key'
	app.run(host='0.0.0.0')
