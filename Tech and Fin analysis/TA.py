import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import talib as ta
plt.style.use('seaborn')

def sma(ticker):
    df = yf.Ticker(ticker).history(period='1y')
    # print(df.head())
    df['SMA'] = ta.SMA(df['Close'],20)
    df[['SMA']].plot(figsize=(12,12))
    # plt.show()
    return plt

def ema(ticker):
    df = yf.Ticker(ticker).history(period='1y')
    # print(df.head())
    df['EMA'] = ta.EMA(df['Close'],20)
    df[['EMA']].plot(figsize=(12,12))
    # plt.show()
    return plt

def macd(ticker):
    df = yf.Ticker(ticker).history(period='1y')
    # print(df.head())
    df['MACD'], df['MACDSIGNAL'], df['MACDHIST'] = ta.MACD(df['Close'],20)
    df[['MACD','MACDSIGNAL', 'MACDHIST']].plot(figsize=(12,12))
    # plt.show()
    return plt
    
def rsi(ticker):
    df = yf.Ticker(ticker).history(period='1y')
    # print(df.head())
    df['RSI'] = ta.RSI(df['Close'],20)
    df[['RSI']].plot(figsize=(12,12))
    # plt.show()
    return plt

def adx(ticker):
    df = yf.Ticker(ticker).history(period='1y')
    # print(df.head())
    df['ADX'] = ta.ADX(df['High'], df['Low'], df['Close'],20)
    df[['ADX']].plot(figsize=(12,12))
    # plt.show()
    return plt

def bband(ticker):
    df = yf.Ticker(ticker).history(period='1y')
    # print(df.head())
    df['UpBand'], df['MidBand'], df['LowBand'] = ta.BBANDS(df['Close'], timeperiod =20)
    df[['UpBand','MidBand','LowBand']].plot(figsize=(12,12))
    # plt.show()
    return plt

def obv(ticker):
    df = yf.Ticker(ticker).history(period='1y')
    # print(df.head())
    df['OBV'] = ta.OBV(df['Close'], df['Volume'])
    df[['OBV']].plot(figsize=(12,12))
    # plt.show()
    return plt

def pivots(ticker):  
    df = yf.Ticker(ticker).history(interval='1d').tail(1)
    # print(df)
    df = df.reset_index(drop=True, inplace=False)
    pp = float((df['High'] + df['Low'] + df['Close'])/3)
    r1 = float(2*pp - df['Low'])
    s1 = float(2*pp - df['High'])
    r2 = float(pp + (df['High'] - df['Low']))
    s2 = float(pp - (df['High'] - df['Low']))
    r3 = float(pp + 2*(df['High'] - df['Low']))
    s3 = float(pp - 2*(df['High'] - df['Low']))
    # print(pp, r1, r2, r3, s1, s2, s3)
    return pp, r1, r2, r3, s1, s2, s3

# sma('msft')
# ema('msft')
# macd('msft')
# rsi('msft')
# adx('msft')
# bband('msft')
# obv('msft')
# pivots('hdfcbank.ns')