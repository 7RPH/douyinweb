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
    tag = getKeywords()
    max = {'max': [like['likelist'][0]] * len(like['likelist'])}
    return render_template('index.html', **sex, **like, **num, **max,**tag)


@app.route('/reloading_tag', methods=['POST'])
def update():
    data = request.values
    for i in data:
        print(i)
        dic = json.loads(i)
    # data=request.form
    print(dic)
    res=updateKeywords(dic)
    if res:
        return {'msg': True}
    else:
        return {'msg': False}



if __name__ == '__main__':
    app.run()
