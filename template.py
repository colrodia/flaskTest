from flask import Flask
from flask.templating import render_template

app = Flask(__name__)


@app.route('/')
def index(): pass

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
if __name__ == '__main__':
    app.debug = True    # 자동으로 변경사항을 체크하여 리로드 되게
    app.run()
