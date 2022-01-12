# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 13:10:45 2022

@author: akhil
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, OrdinalEncoder
from sklearn.compose import ColumnTransformer


def process_data(df):
    scaler = MinMaxScaler()
    encoder = OrdinalEncoder()
    
    data2 = pd.read_csv("./data/NIFTY50_all.csv")
    
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