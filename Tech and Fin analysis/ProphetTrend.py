from prophet import Prophet
import yfinance as yf 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

def forecast(ticker):
    df = yf.Ticker(ticker).history(period='5y', interval = '1d')
    df = df[['Close']]
    dfx = pd.DataFrame()
    dfx['ds'] = pd.to_datetime(df.index)
    dfx['y'] = df.Close.values
    fbp = Prophet(daily_seasonality = True)
    fbp.fit(dfx)
    fut = fbp.make_future_dataframe(periods=(365)) 
    forecast = fbp.predict(fut)
    plot = fbp.plot(forecast)
    plt.show()
    pchange = ((forecast.trend.values[-1] - dfx.y.values[-1])*100)/dfx.y.values[-1]
    if pchange > 0:
        rating = 1
    elif pchange == 0:
        rating = 0
    else:
        rating = -1
    return plot, rating
plot, rating = forecast('googl')