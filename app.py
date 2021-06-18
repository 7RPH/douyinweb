import os
from flask import Flask, render_template, request, session, redirect
from db.dbhandle import *

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = os.urandom(24)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/login_check', methods=['POST'])
def login_check():
    data = request.form
    login_status = login(data)
    if login_status:
        session['login_check'] = '1'
        session['phone'] = data['phone']
        return {'msg': True}
    else:
        return {'msg': False}


@app.route('/register_check', methods=['POST'])
def register_check():
    data = request.form
    login_status = register(data)
    if login_status:
        session['login_check'] = '1'
        session['phone'] = data['phone']
        return {'msg': True}
    else:
        return {'msg': False}


@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect('/', code=301)


if __name__ == '__main__':
    app.run()
