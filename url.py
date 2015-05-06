# # -*- coding:utf-8 -*-
# from flask import Flask, url_for
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def index(): pass
#
# @app.route('/login')
# def login(): pass
#
# @app.route('/user/<username>')
# def profile(username): pass
#
# with app.test_request_context():
#     print(url_for('index'))
#     print(url_for('login'))
#     print(url_for('login', next='/'))
#     print(url_for('profile', username='Colrodia'))
#
# if __name__ == '__main__':
#     app.debug = True    # 자동으로 변경사항을 체크하여 리로드 되게
#     app.run()
