import yfinance as yf 
import pandas as pd 
import numpy as np 
from urllib.request import urlopen
import json
def sectorPerformance(ticker):
    sec = yf.Ticker(ticker).info['sector']
    # print(sec)
    rating = 0
    response = urlopen("https://financialmodelingprep.com/api/v3/stock/sectors-performance?apikey=d55bd9a8a60f1a0d29e6673e4a46cd3e")
    data = json.loads(response.read().decode("utf-8"))
    for x in data['sectorPerformance']:
        if x['sector'] == sec:
            rating = float(x['changesPercentage'][:-1])
            break
        return rating   
print(sectorPerformance('msft'))