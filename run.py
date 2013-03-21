__author__ = 'ghost'
from flask import Flask, url_for
app = Flask(__name__)
app.debug = True

@app.route('/')
def indexAction():
    return '<title>Flask</title> <h1>H! Ghost!</h1> <p><a href="/hello" >Hello</p> <p><a href="/post/">Post list</a></p> <p><a href="/post/123">post 123</a></p>'

@app.route('/hello')
def hello():
    return '<title>Hello</title> <h1>Hello World</h1> <p><a href="/">Return</a></p>'

@app.route('/post/')
def postIndexAction():
    return '<title>Post list</title> <h1>Post list</h1> <ul><li><a href="' + url_for('showPostAction', post_id=123) + '">post 123</a></li><li><a href="/post/345">post 345</a></li></ul>'

@app.route('/post/<int:post_id>')
def showPostAction(post_id):
    return '<title>Show Post</title> <h1>Post:' + str(post_id) + '</h1>' + '<p><a href="/">Return</a></p> </p>' + str(url_for('indexAction')) + "</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0')