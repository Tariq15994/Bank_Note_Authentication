# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify, render_template
import numpy as np
import pickle
import pandas as pd

app=Flask(__name__)


pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=["POST"])
def predict():
    
    '''
    For rendering results on HTML GUI
    '''
    int_features = [ int(x) for x in request.form.values()]
    features_array = [np.array(int_features)]
    prediction = classifier.predict(features_array)[0]
    return render_template('index.html', prediction_text='The Predictied Value is {}'.format(prediction))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    
    return jsonify(prediction)

    

if __name__=='__main__':
    app.run(host='0.0.0.0',debug=True)
    
    