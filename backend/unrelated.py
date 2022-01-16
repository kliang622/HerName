from flask import Flask

app = Flask(__name__)

@app.route("/content")
def hello_world():
    return "<p>yooooo</p>"

@app.route("/")
def ayo(): 
    return "<h1>ayoooooooooooooo</h1>"