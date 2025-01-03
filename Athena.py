from dateutil.relativedelta import relativedelta

import config
# Config acts as a secret class for this project outside of the discord bot. allows access to be easier without reading a txt file every time
import Log as l
import yfinance as yf
from datetime import datetime
from alpaca.data.requests import StockLatestQuoteRequest, StockBarsRequest
from alpaca.data import StockHistoricalDataClient, TimeFrame
from colorama import Fore

class Athena:

    LOG = None
    CLIENT = None
    """
    Athena Class
        Idea is to build a class that can gather the data for the rest of the bots in both a user readable format
            and a computer readable format that the bots read. I want this to open and track invested positions
            and watched positions and get the data on all of them. The hope is the Athena class is essentially the 
            knowledge base for the rest of the bots, and every retrival of information goes through this function
            to make the coding of information gather simple and based just around functions included in athena so i
            dont have to recode every time. 
    """
    def __init__(self):
        self.LOG = l.Log("[ATHENA]", "white")
        self.LOG.print("Initiating Athena...")
        self.LOG.print("Generating Client...")
        self.CLIENT = StockHistoricalDataClient(config.ALPACA_API_KEY, config.ALPACA_API_SECRET)

    """
        Copied from Hephaestus old to gather information and display as single recent price and a list of prices over
            the last year
        
        Pre:
            symb -> The code for the stock that is being requested (eg. MSFT, TSLA, etc)
            
        Post:
            rez -> Dictionary with 2 definitions
                prices: the list of all prices the stock has had over the last year
                curr_price: The most recent closed position price of the stock
                
    """
    def get_single_stock(self, symb):
        self.LOG.print("Gathering Information for Internal Usage...")

        d = (datetime.now() - relativedelta(years=1))

        req = StockLatestQuoteRequest(symbol_or_symbols=[symb])

        quote = self.CLIENT.get_stock_latest_quote(req)[symb.upper()]

        req = StockBarsRequest(
            symbol_or_symbols=[symb],
            timeframe=TimeFrame.Day,
            start=d
        )

        prices = self.CLIENT.get_stock_bars(req).df['close'].tolist()

        rez = {"curr_price": quote.ask_price,
               "prices": prices}

        return rez

    # [O]verview, [A]nalyst, [C]alender, current [P]rice, company [I]nfo, [Q]uarterly statement
    def single_stock_grab(self, symb, choice):
        c = choice.lower()
        if c == 'o':
            pass
        elif c == 'c':
            pass
        elif c == 'p':
            return self.single_stock_price(symb)
        elif c == 'a':
            pass
        elif c == 'i':
            return self.single_stock_info(symb)
        elif c == 'q':
            pass

    def single_stock_info(self, symb):
        self.LOG.print("Gathering Stock Info Data...")
        ticker = yf.Ticker(symb)
        res = ticker.info
        info = f"```{res['symbol']} Stock Info:" \
               f"\n Company Name: {res['longName']} ({res['shortName']})" \
               f"\n Website: {res['website']}" \
               f"\n Headquarters Location: {res['city']}, {res['state']}" \
               f"\n Industry: {res['industry']}" \
               f"\n Employee Count: {res['fullTimeEmployees']}" \
               f"\n Company Description: {res['longBusinessSummary']}" \
               f"\n 52 Week Low: ${res['fiftyTwoWeekLow']}" \
               f"\n 52 Week High: ${res['fiftyTwoWeekHigh']}```"
        return info

    def single_stock_price(self, symb):
        self.LOG.print("Gathering Stock Price Data...")
        req = StockLatestQuoteRequest(symbol_or_symbols=[symb])
        quote = self.CLIENT.get_stock_latest_quote(req)[symb.upper()]
        price = f"```Current Price Info for {symb.upper()} Stock:\n Ask Price: ${quote.ask_price}\n Bid Price: ${quote.bid_price}\nTime: {quote.timestamp.strftime('%Y-%m-%d %H:%M:%S')} GMT\n```"
        return price

    def single_stock_analyst(self, symb):
        pass
# Stock Calender: {ticker.calendar}\nAnalyst Price Targets: {ticker.analyst_price_targets}\nCurrent Price: {round(ticker.history(period='1d')['Close'].iloc[-1], 6)}
