import datetime
import time
import getTickerInfo
import googleSheetHandler
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class MyGrid(Widget):
    lastUpdateLabel = ObjectProperty(None)
    progressLabel = ObjectProperty(None)

    def update(self):
        self.updateTickerPrices(self)
        self.lastUpdateLabel.text = str("Last update performed: \n" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def updateTickerPrices(self, instance):
        sourcesURL = {
            "PORTFOLIO_BET": "https://www.portfolio.hu/tozsde_arfolyamok/bet_reszveny_arfolyamok.html",
            "PORTFOLIO_BETA": "https://www.portfolio.hu/tozsde_arfolyamok/beta_market_arfolyamok.html",
            "PORTFOLIO_CERT": "https://www.portfolio.hu/tozsde_arfolyamok/bet_certifikat_arfolyamok.html"
        }

        # collect tickers and source information
        tickers = googleSheetHandler.getColumnValues(1)
        tickerSource = googleSheetHandler.getColumnValues(2)

        labelInfo = ""

        # go through every ticker and update the price cells with latest price available
        for i in range(1, len(tickers)):
            if tickers[i] == "BREAK": break

            # what if the ticker was not found
            tickerInfo = getTickerInfo.myGetTickerInfo(tickers[i], sourcesURL[tickerSource[i]])
            if not tickerInfo:
                googleSheetHandler.updateSheetWithTickerInfo(i + 1, 4, "Unable to locate ticker")
                continue

            # update the cells with the last price available
            print(tickerInfo["ticker"] + " " + tickerInfo["ido"] + " " + tickerInfo["last"])
            labelInfo = labelInfo + str(tickerInfo["ticker"] + " :: " + tickerInfo["last"]+ "\n")

            googleSheetHandler.updateCellValue(i + 1, 3, tickerInfo["ido"])
            googleSheetHandler.updateCellValue(i + 1, 4, tickerInfo["last"])

        #print(labelInfo)

class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == '__main__':
    MyApp().run()

# class MyGrid(GridLayout):
#     def __init__(self, **kwargs):
#         super(MyGrid, self).__init__(**kwargs)
#         self.cols = 1
#
#         self.lastUpdateLabel = Label(text=""
#                                    "Last update time: \n" +
#                                    str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
#         self.add_widget(self.lastUpdateLabel)
#
#         self.progressLabel = Label(text="Update starts when button pressed")
#         self.add_widget(self.progressLabel)
#
#         self.submit = Button(text= "Update", font_size=40)
#         self.submit.bind(on_press=self.update)
#         self.add_widget(self.submit)

# def update(self, instance):
    #     self.submit.text = str("Gathering ticker information ...")
    #     self.submit.disabled = True
    #     self.updateTickerPrices(self)
    #     self.lastUpdateLabel.text = str("Last update time: \n" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    #     self.submit.disabled = False