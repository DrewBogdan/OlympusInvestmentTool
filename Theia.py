"""
Author: Drew Bogdan
Theia (God of Vision and Sight) Class
    this class is built for visualizing stock data, ideally for the discord bot so that
        when stock information is grabbed it can be plotted correctly
"""

import Log as l
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf
from datetime import timezone, datetime
from zoneinfo import ZoneInfo

class Theia:

    LOG = None

    def __init__(self):
        self.LOG = l.Log("[THEIA]", "cyan")
        self.LOG.print("Initiating Theia...")


    def candle_chart(self, candledata):
        self.LOG.print("Producing Candle Plot...")
        df = self.convert_to_dataframe(candledata)

        colors = mpf.make_marketcolors(up='#00ff00', down='#FF073A', inherit=True)

        s = mpf.make_mpf_style(base_mpf_style='nightclouds', marketcolors=colors)

        mpf.plot(df, type='candle', style=s, figratio=(40,20), savefig='candlefig.png')

        self.LOG.print("Candle Plot Created...")



    def convert_to_dataframe(self, candledata):
        index, open, close, high, low = [], [], [], [], []

        for x in candledata:
            index.append(x.timestamp.replace(tzinfo=timezone.utc).astimezone(ZoneInfo("America/New_York")))
            open.append(x.open)
            high.append(x.high)
            low.append(x.low)
            close.append(x.close)

        df = pd.DataFrame({'date': index, 'open': open, 'high': high, 'low': low, 'close': close})

        df.index = pd.DatetimeIndex(df['date'])

        return df