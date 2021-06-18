import os
from flask import Flask, render_template, request, session, redirect
from db.dbhandle import *
import json

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = os.urandom(24)


@app.route('/')
def hello_world():
    sex = getSex()
    like = getLike()
    num = getNum()
    return render_template('index.html', **sex, **like, **num)


if __name__ == '__main__':
    app.run()
