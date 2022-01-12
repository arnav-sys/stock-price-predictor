# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 12:57:57 2022

@author: akhil
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 18:05:15 2022
@author: akhil
"""

import joblib
import pandas as pd
from preprocess_data import process_data
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.linear_model import LinearRegression


# Load model as a Spark UDF.
model = joblib.load("model.sav")

df = pd.read_csv("final_data.csv")
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
