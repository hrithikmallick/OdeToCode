from copyreg import pickle
from statistics import mode
from flask import Flask,render_template,request
import pandas as pd
import pickle
app = Flask(__name__)


#model loading
model=pickle.load(open("LogisticRegressionModel.pkl","rb"))







@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict",methods=["POST"])
def predict():
    try:
        age=int(request.form.get("age"))
        sex=int(request.form.get("sex"))
        cp=int(request.form.get("cp"))
        trestbps=int(request.form.get("trestbps"))
        chol=int(request.form.get("chol"))
        fbs=int(request.form.get("fbs"))
        restecg=int(request.form.get("restecg"))
        thalach=int(request.form.get("thalach"))
        exang=int(request.form.get("exang"))
        oldpeak=float(request.form.get("oldpeak"))
        slope=int(request.form.get("slope"))
        ca=int(request.form.get("ca"))
        thal=int(request.form.get("thal"))
        # print(age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal)



        prediction=model.predict(pd.DataFrame([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]],columns=["age","sex","cp","trestbps","chol","fbs","restecg","thalach","exang","oldpeak","slope","ca","thal"]))
        # prediction=model.predict(pd.DataFrame([[age,0,1,132,342,0,1,166,0,1.2,2,0,2]],columns=["age","sex","cp","trestbps","chol","fbs","restecg","thalach","exang","oldpeak","slope","ca","thal"]))
        # print(prediction)
        str=""
        if prediction[0]==1:
            str="You have a heart disease"
        elif prediction[0]==0:
            str="You have a healthy heart"
        return str
    except:
        str="Please enter valid Data.!"
        return str




app.run(debug=True,port=8888)