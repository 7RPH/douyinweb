import os
from flask import Flask, render_template, request, session, redirect
from db.dbhandle import *
import json
import douyin

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = os.urandom(24)
def test():
    n=0
    while True:
        yield n
        n+=1
data={'data': '没有数据'}

@app.route('/start', methods=['POST'])
def iterat():
    for i in test():
        data['data'] = str(i)
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
        d = json.loads(i)
    # data=request.form
    print(d)
    res=updateKeywords(d)
    if res:
        return {'msg': True}
    else:
        return {'msg': False}

@app.route('/showdata')
def showdata():
    return render_template('showdata.html', **data)

if __name__ == '__main__':
    app.run()
