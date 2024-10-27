from flask import Flask, render_template

app = Flask("my first program")

@app.route("/page")
def page():
    return "hello world"

@app.route("/")
def index():
    return render_template("index.html")



app.run()