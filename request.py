# -*- coding:utf-8 -*-
from flask import Flask, request
from flask.templating import render_template

app = Flask(__name__)


@app.route('/')
def index(): pass

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        print(request.args.get('username', ''))
        print(request.args.get('password', ''))
        if valid_login(request.args.get('username', ''),
                       request.args.get('password', '')):
            return log_the_user_in(request.args.get('username', ''))
        else:
            error = 'Invalid username/password'
    # 아래의 코드는 요청이 GET 이거나, 인증정보가 잘못됐을때 실행된다.
    return render_template('login.html', error=error)

def valid_login(username, password):
    if username == 'colrodia' and password == '111':
        return True
    else:
        return False

def log_the_user_in(username):
    return 'Welcome' + username

if __name__ == '__main__':
    app.debug = True    # 자동으로 변경사항을 체크하여 리로드 되게
    app.run()
