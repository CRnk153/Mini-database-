from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_BINDS = {}



app = Flask(__name__)


app.config.from_object(Config)
db = SQLAlchemy(app)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String('128'), unique=True)
    text = db.Column(db.String('128'), unique=True)

    def __init__(self, username, text):
        self.username = username
        self.text = text


    def __repr__(self):
        return '<User %r>' % self.username




@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')