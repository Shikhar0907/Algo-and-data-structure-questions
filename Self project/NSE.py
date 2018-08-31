import urllib
import urllib.request
import re

def stockprice():
    stock = str(input("Please enter the organisation name:"))
    header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3','Accept-Encoding': 'none','Accept-Language': 'en-US,en;q=0.8','Connection': 'keep-alive'}
    url = urllib.request.Request('https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol=' + stock + '&illiquid=0&smeFlag=0&itpFlag=0', headers = header)
    navigation = urllib.request.urlopen(url)
    data = navigation.read()

    search = '"lastPrice":"(.+?)"'
    com = re.compile(search)
    result = re.findall(com, str(data))
    if (result):
        print("last price" + str(result))

stockprice()
