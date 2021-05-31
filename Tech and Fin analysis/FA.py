import pandas as pd
import datetime
import yfinance as yf

def piotroski(ticker):
    bs = yf.Ticker(ticker).balance_sheet
    inc = yf.Ticker(ticker).financials
    cf = yf.Ticker(ticker).cashflow
    longTermDebt = bs.loc['Long Term Debt'][0]
    longTermDebtPre = bs.loc['Long Term Debt'][1]
    totalAssets = bs.loc['Total Assets'][0]
    totalAssetsPre = bs.loc['Total Assets'][1]
    totalAssetsPre2 = bs.loc['Total Assets'][2]
    currentAssets = bs.loc['Total Current Assets'][0]
    currentAssetsPre = bs.loc['Total Current Assets'][1]
    currentLiabilities = bs.loc['Total Current Liabilities'][0]
    currentLiabilitiesPre = bs.loc['Total Current Liabilities'][1]
    revenue = inc.loc['Total Revenue'][0]
    revenuePre = inc.loc['Total Revenue'][1]
    grossProfit = inc.loc['Gross Profit'][0]
    grossProfitPre = inc.loc['Gross Profit'][1]
    netIncome = inc.loc['Net Income'][0]
    netIncomePre = inc.loc['Net Income'][1]
    operatingCashFlow = cf.loc['Total Cash From Operating Activities'][0]
    operatingCashFlowPre = cf.loc['Total Cash From Operating Activities'][1]
    commonStock = bs.loc['Common Stock'][0]
    commonStockPre = bs.loc['Common Stock'][1]
    ROAFS = int(netIncome/((totalAssets + totalAssetsPre)/2)>0)
    CFOFS = int(operatingCashFlow>0)
    ROADFS = int((netIncome/((totalAssets + totalAssetsPre)/2))>(netIncomePre/((totalAssetsPre + totalAssetsPre2))))
    CFOROAFS = int((operatingCashFlow/totalAssets)>(netIncome/((totalAssets + totalAssetsPre)/2)))
    LTDFS = int(longTermDebt <= longTermDebtPre)
    CRFS = int(currentAssets/currentLiabilities)>(currentAssetsPre/currentLiabilitiesPre)
    NSFS = int(commonStock <= commonStockPre)
    GMFS = int(grossProfit/revenue>grossProfitPre/revenuePre)
    ATOFS = int((revenue/((totalAssets + totalAssetsPre)/2))>(revenuePre/((totalAssetsPre + totalAssetsPre2))))
    return ROAFS + CFOFS +  ROADFS + CFOROAFS + LTDFS + CRFS + NSFS + GMFS + ATOFS
print(piotroski('msft'))