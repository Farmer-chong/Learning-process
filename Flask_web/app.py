from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    greeting = "hello world 233"
    return render_template("index.html", name="-Farmer", greeting=greeting)

@app.route('/login/', methods=['POST','get'])
def login():
    greeting = "Hello World!"

    if request.method == "POST":
        name = request.form['name']
        greeting = request.form['greet']
        return render_template("index.html", greeting=greeting, name=name)
    else:
        return render_template("login.html")

if __name__ == "__main__":
    app.run()