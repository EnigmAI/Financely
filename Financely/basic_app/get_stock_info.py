import urllib.request, json

def getStockInfo(var):
    var = var.replace(' ','')
    url = "https://finance.yahoo.com/_finance_doubledown/api/resource/searchassist;searchTerm={}?device=console&returnMeta=true".format(var)
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    return data['data']['items']
