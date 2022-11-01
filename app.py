from flask import Flask,render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict")
def predict():
    return render_template("index.html")





app.run(debug=True,port=8888)