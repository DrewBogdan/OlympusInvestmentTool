
import Log as l
import yfinance as yf
class Athena:

    LOG = None
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
        self.LOG.print("Gathering Information")
        ticker = yf.Ticker(symb).history(period='1y')
        rez = {"curr_price": round(ticker['Close'].iloc[-1], 6),
               "prices": [round(ticker['Close'].iloc[x], 6) for x in range(len(ticker['Close'].tolist()))]}
        return rez