# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 11:00:20 2022

@author: akhil
"""

from flask import Flask, jsonify, request
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
import chart_studio
import chart_studio.plotly as py
import pandas as pd
from data_source import downloadfile
import chart_studio.tools as tls
import plotly.graph_objects as go
import plotly.express as px
import joblib

username = 'arnav-sys' # your username
api_key = 'fZDe8bg5zKytkXiBs0gS' # your api key 
chart_studio.tools.set_credentials_file(username=username, api_key=api_key)

model = joblib.load("./model.sav")

app = Flask(__name__)


def visualizations(df):
        username = 'arnav-sys' # your username
        api_key = 'fZDe8bg5zKytkXiBs0gS' # your api key - go to profile > settings > regenerate key
        chart_studio.tools.set_credentials_file(username=username, api_key=api_key)
        fig = px.line(df, x="Date",y="Low",color="Symbol")
        py.plot(fig, filename = 'plot1', auto_open=True)
        output1 = tls.get_embed("https://plotly.com/~arnav-sys/1/#plot")
        fig = px.line(df, x="Date",y="Open",color="Symbol")
        py.plot(fig, filename = 'plot2', auto_open=True)
        output2 = tls.get_embed("https://plotly.com/~arnav-sys/3/#/")
        fig = px.line(df, x="Date",y="Low",color="Symbol")
        py.plot(fig, filename = 'plot3', auto_open=True)
        output5 = tls.get_embed("https://plotly.com/~arnav-sys/5/#/")
        fig  = px.line(df, x="Date",y="Close",color="Symbol")
        py.plot(fig, filename = 'plot4', auto_open=True)
        output7 = tls.get_embed("https://plotly.com/~arnav-sys/7/#/")
        fig = px.line(df,x="Date",y="Prev Close",color="Symbol")
        py.plot(fig, filename = 'plot5', auto_open=True)
        output8 = tls.get_embed("https://plotly.com/~arnav-sys/9/#/")
        fig = px.line(df,x="Date",y="VWAP",color="Symbol")
        py.plot(fig, filename = 'plot6', auto_open=True)
        output9 = tls.get_embed("https://plotly.com/~arnav-sys/11/#/")
        fig = px.line(df,x="Date",y="Turnover",color="Symbol")
        py.plot(fig, filename = 'plot7', auto_open=True)
        output10 = tls.get_embed("https://plotly.com/~arnav-sys/13/#/")
        fig = px.line(df,x="Date",y="Volume",color="Symbol")
        py.plot(fig, filename = 'plot8', auto_open=True)
        output11 = tls.get_embed("https://plotly.com/~arnav-sys/15/#/")
        df["Year"] = df["Date"].apply(lambda x: int(x[0:4]))
        df["Month"] = df["Date"].apply(lambda x: int(x[5:7]))
        fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'])])
        py.plot(fig, filename = 'plot9', auto_open=True)
        output12 = tls.get_embed("https://plotly.com/~arnav-sys/17/#/")
        fig = px.line(df,x="Date",y="Volume",color="Symbol")
        py.plot(fig, filename = 'plot10', auto_open=True)
        output13 = tls.get_embed("https://plotly.com/~arnav-sys/19/#/")
        fig = px.line(df,x="Date",y="VWAP",color="Symbol")
        py.plot(fig, filename = 'plot11', auto_open=True)
        output14 = tls.get_embed("https://plotly.com/~arnav-sys/21/#/")
        fig = px.line(df,x="Date",y="Turnover",color="Symbol")
        py.plot(fig, filename = 'plot12', auto_open=True)
        output15 = tls.get_embed("https://plotly.com/~arnav-sys/23/#/")
        fig = px.scatter(df,x="Year",y="Close",size="Open", color="Symbol")
        py.plot(fig, filename = 'plot13', auto_open=True)
        output16 = tls.get_embed("https://plotly.com/~arnav-sys/25/#/")
        fig = px.scatter(df,x="Month",y="Close",size="Open", color="Symbol")
        py.plot(fig, filename = 'plot14', auto_open=True)
        output17 = tls.get_embed("https://plotly.com/~arnav-sys/27/#/")
        fig = px.bar(df,x="VWAP",y="Close", color="Symbol")
        py.plot(fig, filename = 'plot15', auto_open=True)
        output18 = tls.get_embed("https://plotly.com/~arnav-sys/29/#/")
        fig = px.bar(df,x="Volume",y="Close", color="Symbol")
        py.plot(fig, filename = 'plot16', auto_open=True)
        output19 = tls.get_embed("https://plotly.com/~arnav-sys/31/#/")
        fig = px.line(df,x="Date",y=df.columns[5:7])
        py.plot(fig, filename = 'plot17', auto_open=True)
        output20 = tls.get_embed("https://plotly.com/~arnav-sys/33/#/")
        fig = px.line(df,x="Trades",y="Close")
        py.plot(fig, filename = 'plot18', auto_open=True)
        output21 = tls.get_embed("https://plotly.com/~arnav-sys/35/#/")
        df["Day"] = df["Date"].apply(lambda x: int(x[8:10]))
        fig = px.bar(df,x="Day",y="Close", color="Symbol")
        py.plot(fig, filename = 'plot19', auto_open=True)
        output22 = tls.get_embed("https://plotly.com/~arnav-sys/37/#/")
        
        final_output = {
            "output1":output1,
            "output2":output2,
            "output3":output5,
            "output4":output7,
            "output5":output9,
            "output6":output10,
            "output7":output11,
            "output8":output12,
            "output9":output13,
            "output10":output14,
            "output11":output15,
            "output12":output16,
            "output13":output17,
            "output14":output18,
            "output15":output19,
            "output16":output20,
            "output17":output21,
            "output18":output22,
        }
        
        return final_output


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
    
@app.route("/data", methods = ["POST"])
def get_visualizations():
    if request.method == "POST":
        data = request.get_json()
        response = ""
        company_list = ['MUNDRAPORT', 'ADANIPORTS', 'ASIANPAINT', 'UTIBANK', 'AXISBANK',
       'BAJAJ-AUTO', 'BAJAJFINSV', 'BAJAUTOFIN', 'BAJFINANCE', 'BHARTI',
       'BHARTIARTL', 'BPCL', 'BRITANNIA', 'CIPLA', 'COALINDIA', 'DRREDDY',
       'EICHERMOT', 'GAIL', 'GRASIM', 'HCLTECH', 'HDFC', 'HDFCBANK',
       'HEROHONDA', 'HEROMOTOCO', 'HINDALC0', 'HINDALCO', 'HINDLEVER',
       'HINDUNILVR', 'ICICIBANK', 'INDUSINDBK', 'INFOSYSTCH', 'INFY',
       'IOC', 'ITC', 'JSWSTL', 'JSWSTEEL', 'KOTAKMAH', 'KOTAKBANK', 'LT',
       'M&M', 'MARUTI', 'NESTLEIND', 'NTPC', 'ONGC', 'POWERGRID',
       'RELIANCE', 'SBIN', 'SHREECEM', 'SUNPHARMA', 'TELCO', 'TATAMOTORS',
       'TISCO', 'TATASTEEL', 'TCS', 'TECHM', 'TITAN', 'ULTRACEMCO',
       'UNIPHOS', 'UPL', 'SESAGOA', 'SSLT', 'VEDL', 'WIPRO', 'ZEETELE',
       'ZEEL']
        for company in company_list:
            print(company)
            print(data["name"])
            if company == data["name"]:
                print("ok")
                path = company + ".csv"
                print(path)
                downloadfile(path)
                data2 = pd.read_csv(path)
                response = visualizations(data2)
                print(response)
        return response
        

if __name__ == '__main__':
  
    app.run(host='0.0.0.0',port=80)
