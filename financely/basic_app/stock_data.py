import yfinance as yf
from datetime import datetime
#import pandas as pd


def candlestick_data(ticker):
    #now  = datetime.now()
    aapl = yf.Ticker(ticker)
    now = datetime.now().date().strftime('%Y-%m-%d')
    # data = aapl.history(end=now,period='1mo', interval='1d')
    # newdata= data.to_dict()
    # print(newdata)'%Y-%m-%d'
    old  =  aapl.history(start="2001-05-21", end=now)

    old = old.reset_index()
    for i in ['Open', 'High', 'Close', 'Low']:

        old[i]  =  old[i].astype('float64')

    cols = old.columns

    cols =cols[:5].values
    data = []
    for i,val in old.iterrows():
        d = {}
        for c in cols:
            d[c] = val[c]

        data.append(d)

    for i in range(len(data)):
        timestampStr = data[i]['Date'].date().strftime("%d-%b-%Y")
        data[i]['Date'] = timestampStr


    return(data)
    #print(old)
    # return data
    # final_data = {}
    # if(len(passover['Open']) > 0):
    #
    #     open_last = list(passover['Open'].keys())[-1]
    #     high_last = list(passover['High'].keys())[-1]
    #
    #     low_last = list(passover['Low'].keys())[-1]
    #
    #     close_last = list(passover['Close'].keys())[-1]
    #
    #     final_data = {
    #         "Open":passover['Open'][open_last],
    #         "High":passover['High'][high_last],
    #         "Low":passover['Low'][low_last],
    #         "Close":passover['Close'][close_last],
    #
    #     }
    #
    #
    #
    # return passover['Open'].keys()

#print(get_data("aapl"))

def get_data(ticker):
    #now  = datetime.now()
    aapl = yf.Ticker(ticker)
    data = aapl.info
    return data


#
# for a in get_data("aapl"):
#     print(a.shortName)
