import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import talib as ta
plt.style.use('seaborn')

def generator(ticker):
    df = yf.Ticker(ticker).history(period='max')
    df['SMA'] = ta.SMA(df['Close'],20)
    df['EMA'] = ta.EMA(df['Close'],20)
    df['MACD'], df['MACDSIGNAL'], df['MACDHIST'] = ta.MACD(df['Close'],20)
    df['RFI'] = ta.RSI(df['Close'],20)
    df['ADX'] = ta.ADX(df['High'], df['Low'], df['Close'],20)
    df['UpBand'], df['MidBand'], df['LowBand'] = ta.BBANDS(df['Close'], timeperiod =20)
    df['OBV'] = ta.OBV(df['Close'], df['Volume'])
    # print(df)
    return df

# generator('msft')