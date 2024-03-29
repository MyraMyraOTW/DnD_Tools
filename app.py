import os

from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, jsonify
from flask_sqlalchemy import SQLAlchemy

# get the folder where this file runs
basedir = os.path.abspath(os.path.dirname(__file__))

# configuration
DATABASE = 'flaskr.db'
DEBUG = True
SECRET_KEY = 'F1E586991B74BEA4EB1BE1DDE742E'
USERNAME = 'GameMaster'
PASSWORD = 'iaXLSvqtfG'

# define the full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)

# database config
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATABASE_PATH
SQLALCHEMY_TRACK_MODIFICATIONS = False

# create app
app = Flask(__name__)
app.config.from_object(__name__)
db = SQLAlchemy(app)

# import models

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
