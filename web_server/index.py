from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/blog")
def hello_blog():
    return "<p>Hello, World! Nice to see you</p>"