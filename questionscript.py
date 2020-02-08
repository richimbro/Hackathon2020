import requests
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/home")
def home():
    return render_template("StartPage.HTML")

@app.route("/filloutform")
def form():
    return render_template("FormPage.HTML")

if  __name__ == "__main__":
    app.run()
