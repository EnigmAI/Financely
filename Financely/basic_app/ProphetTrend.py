from prophet import Prophet
#import pystan
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import base64
from io import BytesIO

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer,format = "png")
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph


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
    plt.xlabel("Date")
    plt.ylabel("Price")
    graph = get_graph()
    return graph
    # plt.show()
    # pchange = ((forecast.trend.values[-1] - dfx.y.values[-1])*100)/dfx.y.values[-1]
    # if pchange > 0:
    #     rating = 1
    # elif pchange == 0:
    #     rating = 0
    # else:
    #     rating = -1
    # return plot, rating
# plot, rating = forecast('googl')
