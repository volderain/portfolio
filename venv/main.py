import getTickerInfo
import googleSheetHandler

sourcesURL = {
    "PORTFOLIO_BET" : "https://www.portfolio.hu/tozsde_arfolyamok/bet_reszveny_arfolyamok.html",
    "PORTFOLIO_BETA" : "https://www.portfolio.hu/tozsde_arfolyamok/beta_market_arfolyamok.html",
    "PORTFOLIO_CERT" : "https://www.portfolio.hu/tozsde_arfolyamok/bet_certifikat_arfolyamok.html"
}

#collect tickers and source information
tickers = googleSheetHandler.getColumnValues(1)
tickerSource = googleSheetHandler.getColumnValues(2)

#go through every ticker and update the price cells with latest price available
for i in range(1, len(tickers)):
    if tickers[i] == "BREAK": break

    #what if the ticker was not found
    tickerInfo = getTickerInfo.myGetTickerInfo(tickers[i], sourcesURL[tickerSource[i]])
    if not tickerInfo:
        googleSheetHandler.updateSheetWithTickerInfo(i + 1, 4, "Unable to locate ticker")
        continue

    #update the cells with the last price available
    print(tickerInfo["ticker"] + " " + tickerInfo["ido"] + " " + tickerInfo["last"])
    googleSheetHandler.updateCellValue(i+1, 3, tickerInfo["ido"])
    googleSheetHandler.updateCellValue(i+1, 4, tickerInfo["last"])


