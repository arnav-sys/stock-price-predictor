# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 11:00:20 2022

@author: akhil
"""

from flask import Flask, jsonify, request
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
import pandas as pd
from data_source import downloadfile
import joblib

username = 'arnav-sys' # your username
api_key = 'fZDe8bg5zKytkXiBs0gS' # your api key 
chart_studio.tools.set_credentials_file(username=username, api_key=api_key)

model = joblib.load("./model.sav")

app = Flask(__name__)


def process_data(df):
    data = pd.read_csv("./final_data.csv")
    data2 = pd.read_csv("./data/NIFTY50_all.csv")

    scaler = MinMaxScaler()
    encoder = LabelEncoder()
    encoder2= LabelEncoder()
    
    scaler.fit(data[["Open","High","Low","Last","VWAP","Volume","Turnover","Month","Day","Year","Prev Close"]])
    encoder.fit(data2["Date"])
    encoder2.fit(data2["Symbol"])

    
    df[["Open","High","Low","Last","VWAP","Volume","Turnover","Month","Day","Year","Prev Close"]] = scaler.transform(df[["Open","High","Low","Last","VWAP","Volume","Turnover","Month","Day","Year","Prev Close"]])
    
    labels = encoder.transform(df["Date"])
    df["Date"] = labels
        
    labels = encoder2.transform(df["Symbol"])
    df["Symbol"] = labels

    
    return df


@app.route('/', methods = ['GET'])
def MainPage():
    return "<h1>App</h1>"

@app.route("/model", methods = ["POST"])
def run_model():
    if request.method == "POST":
        scaler1 = MinMaxScaler()
        data = request.get_json()
        df= pd.json_normalize(data)
        df = process_data(df)
        predictions = model.predict(df)
        
        return str(predictions)
    


if __name__ == '__main__':
  
    app.run(host='0.0.0.0',port=80)
