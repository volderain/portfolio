import re
import requests
from bs4 import BeautifulSoup

def myGetTickerInfo(ticker, url):
    page = requests.get(url)

    soup = BeautifulSoup(page.text, 'html.parser')

    tickerTable=soup.find(id="P_"+ ticker)

    if not tickerTable: return tickerTable

    tickerArray = str(tickerTable).split("\n")
    tickerArray.pop(0)
    tickerArray.pop(0)
    tickerArray.pop(len(tickerArray)-1)

    tickerInfo = {}

    for data in tickerArray:
            eliminateSpan = re.sub(r'<td class=\"(.*?)\">(<span.*?>)(.*?)(</span>)(</td>)', r'\1 - \3', data)
            exportTicketData = str(re.sub(r'<td class=\"(.*?)\">(.*?)</td>', r'\1 - \2', eliminateSpan).replace(" ", ""))
            match = re.split("-", exportTicketData)
            if not match[1]:
                    match[1] = 0
            tickerInfo[match[0]] = match[1]
            #print(data + " --> " + str(match))

    #for x, y in tickerInfo.items():
    #  print(x, y)

    return tickerInfo
