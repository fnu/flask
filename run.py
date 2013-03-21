__author__ = 'ghost'
from flask import Flask
app = Flask(__name__)
app.debug = True

@app.route('/')
def indexAction():
    return '<title>Flask</title> <h1>H! Ghost!</h1> <p><a href="/hello" >Hello</p>'

@app.route('/hello')
def hello():
    return '<title>Hello</title> <h1>Hello World</h1> <p><a href="/">Return</a></p>'

if __name__ == '__main__':
    app.run(host='0.0.0.0')