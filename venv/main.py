import getTickerInfo
import googleSheetHandler

ticker = "EBEURHUFTL40"
# url='https://www.portfolio.hu/tozsde_arfolyamok/bet_reszveny_arfolyamok.html'
url = 'https://www.portfolio.hu/tozsde_arfolyamok/bet_certifikat_arfolyamok.html'

sourcesURL = {
    "PORTFOLIO_BET" : "https://www.portfolio.hu/tozsde_arfolyamok/bet_reszveny_arfolyamok.html",
    "PORTFOLIO_BETA" : "https://www.portfolio.hu/tozsde_arfolyamok/beta_market_arfolyamok.html",
    "PORTFOLIO_CERT" : "https://www.portfolio.hu/tozsde_arfolyamok/bet_certifikat_arfolyamok.html"
}

#ticker = getTickerInfo.myGetTickerInfo(ticker, url)

#print(ticker["ticker"] + " " + ticker["ido"] + " " + ticker["last"] )

#googleSheetHandler.updateSheetWithTickerInfo( ticker["ticker"], ticker["ido"], ticker["last"])

ticker = googleSheetHandler.getColumnValues(1)
tickerSource = googleSheetHandler.getColumnValues(2)


for i in range(1, len(ticker)):
    if ticker[i] == "BREAK": break
    tickerInfo = getTickerInfo.myGetTickerInfo(ticker[i], sourcesURL[tickerSource[i]])
    print(tickerInfo["ticker"] + " " + tickerInfo["ido"] + " " + tickerInfo["last"])
    googleSheetHandler.updateSheetWithTickerInfo(i+1, 3, tickerInfo["ido"])
    googleSheetHandler.updateSheetWithTickerInfo(i+1, 4, tickerInfo["last"])


