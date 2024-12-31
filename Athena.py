import config
# Config acts as a secret class for this project outside of the discord bot. allows access to be easier without reading a txt file every time
import Log as l
import yfinance as yf
import datetime
from alpaca.data.requests import StockLatestQuoteRequest
from alpaca.data.historical import StockHistoricalDataClient

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
        self.LOG = l.Log("[ATHENA]")
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
        self.LOG.print("Gathering Information...")
        ticker = yf.Ticker(symb).history(period='1y')
        rez = {"curr_price": round(ticker['Close'].iloc[-1], 6),
               "prices": [round(ticker['Close'].iloc[x], 6) for x in range(len(ticker['Close'].tolist()))]}
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
        ticker = yf.Ticker(symb)
        info = f"```Stock Info: {ticker.info}```"
        print(info)
        return info

    def single_stock_price(self, symb):
        req = StockLatestQuoteRequest(symbol_or_symbols=[symb])
        ticker = yf.Ticker(symb)
        quote = self.CLIENT.get_stock_latest_quote(req)[symb.upper()]
        price = f"```Current Price Info for {symb.upper()} Stock:\n Ask Price: ${quote.ask_price}\n Bid Price: ${quote.bid_price}\nTime: {quote.timestamp.strftime('%Y-%m-%d %H:%M:%S')} GMT\n```"
        return price

# Stock Calender: {ticker.calendar}\nAnalyst Price Targets: {ticker.analyst_price_targets}\nCurrent Price: {round(ticker.history(period='1d')['Close'].iloc[-1], 6)}
