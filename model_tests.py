# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 12:57:57 2022

"""


import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.linear_model import LinearRegression

from sklearn.preprocessing import MinMaxScaler, OrdinalEncoder
from sklearn.compose import ColumnTransformer


def process_data(df):
    scaler = MinMaxScaler()
    encoder = OrdinalEncoder()
    
    data2 = pd.read_csv("./model/data/NIFTY50_all.csv")
    
    data2["Year"] = data2["Date"].apply(lambda x: int(x[0:4]))
    data2["Month"] = data2["Date"].apply(lambda x: int(x[5:7]))
    data2["Day"] = data2["Date"].apply(lambda x: int(x[8:10]))
    
    num_data =["Open","High","Low","Last","VWAP","Volume","Turnover","Month","Day","Year","Prev Close"]
    cat_data = ["Date","Symbol"]
    
    pipeline = ColumnTransformer([
        ("num", MinMaxScaler(), num_data),
        ("cat",OrdinalEncoder(),cat_data)
    ])
    
    data2 = pipeline.fit_transform(data2)
    
    df = pd.DataFrame(pipeline.transform(df))

    
    return df


# Load model as a Spark UDF.
model = joblib.load("./model/model.sav")

df = pd.read_csv("./model/final_data.csv")
print(df.info())
#splitting dataset into train, test and validate

X = df.drop(columns=["Close"])
y = df["Close"] 

X = process_data(X)

X_train, X_test,y_train, y_test = train_test_split(X,y)




def test_model():
     elements_pred =  model.predict(X_test)
     
     from sklearn.metrics import mean_squared_error
     error = mean_squared_error(y_test, elements_pred)

     assert error < 3.0
