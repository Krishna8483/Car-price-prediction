# -*- coding: utf-8 -*-
"""
Created on Sat May 15 14:12:58 2021

@author: Krishna
"""

from flask import Flask,render_template,request
import pickle
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
model = pickle.load(open('Heart_attack_predictions.pkl','rb'))
@app.route('/',methods=['GET'])


def hello_world():
    return render_template('index.html')
std_scale=StandardScaler()



@app.route("/predict",method=['POST'])
def predict():

   if request.method == 'POST':
    age = float(request.form['age'])
    anaemia = int(requests.form['anaemia'])



    creatinine_phosphokinase = int(requests.form['creatinine_phosphokinase'])
    diabetes = int(requests.form['diabetes'])


    ejection_fraction = int(requests.form['ejection_fraction'])
    high_blood_pressure= int(requests.form['high_blood_pressure'])


    platelets=int(requests.form['platelets'])

    serum_creatinine=int(requests.form['serum_creatinine'])

    serum_sodium=int(requests.form['serum_sodium'])

    sex=int(requests.form['Sex'])

    smoking=int(requests.form['smoking'])


    lst1 = [[age, anaemia, creatinine_phosphokinase, diabetes, ejection_fraction, high_blood_pressure, platelets,
         serum_creatinine, serum_sodium, sex, smoking]]
    lst2=std_scale.fit_transform(lst1)

    prediction=model.predict(lst1)
    prediction=int(prediction)
   if prediction==1:
    print("The patient will suffer from cardiac arrest")
   else:
    print("The patient will survive")

   if __name__ == "__main__":
    app.run(debug=True)