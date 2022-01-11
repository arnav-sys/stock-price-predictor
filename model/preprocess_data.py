# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 13:10:45 2022

@author: akhil
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, OrdinalEncoder


def process_data(df):
    scaler = MinMaxScaler()
    encoder = OrdinalEncoder()
    
    df[["Open","High","Low","Last","Close","VWAP","Volume","Turnover","Month","Day","Year"]] = scaler.fit_transform(df[["Open","High","Low","Last","Close","VWAP","Volume","Turnover","Month","Day","Year"]])
    df[["Date","Symbol"]] = encoder.fit_transform(df[["Date","Symbol"]])
    
    return df
