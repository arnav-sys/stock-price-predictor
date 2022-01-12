# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 16:18:09 2022

@author: akhil
"""

import pandas as pd
from preprocess_data import process_data
import joblib
import mlflow
from sklearn.model_selection import train_test_split


df = pd.read_csv("./final_data.csv")

df = process_data(df)
X = df.drop(columns=["Close","Unnamed: 0"])
y = df["Close"]
X_train, X_test,y_train, y_test = train_test_split(X,y)
    

#Linear Regression
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
with mlflow.start_run():
    model = LinearRegression()
    
    model.fit(X_train, y_train)
    
    predictions = model.predict(X_test)
    
    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)
    
    mlflow.log_metric("mse", mse)
    mlflow.log_metric("r2",r2)


#Support Vector Machines
from sklearn.svm import SVR
with mlflow.start_run():
    model = SVR()
    
    model.fit(X_train, y_train)
    
    predictions = model.predict(X_test)
    
    print(predictions)
    print(y_test)
    
    mse = mean_squared_error(y_test, predictions)
    r2 = r2_score(y_test, predictions)
    
    mlflow.log_metric("mse", mse)
    mlflow.log_metric("r2",r2)
    
    mlflow.sklearn.log_model(model,"model")
    
    # Logging training data
    mlflow.log_artifact(local_path = './final_data.csv')
# Logging training code
    mlflow.log_artifact(local_path = './model.py')
    
    joblib.dump(model, "model.sav")