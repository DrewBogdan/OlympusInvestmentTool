"""
Title: Options Profit Calculator
CodeName: Hephaestus
Reason: Hephaestus is the god of invention and forge, this is a tool to be used by the rest of the bots
"""

import numpy as np
from scipy.stats import norm
import Log as l
import yfinance as yf

from Athena import Athena
from Kronos import Kronos
from datetime import date, datetime

class Hephaestus:

    TRADING_DAYS = 252
    INTEREST_RATE = 0.05
    KRONOS = None
    ATHENA = None
    LOG = None

    def __init__(self, athena):
        self.LOG = l.Log("[HEPHAESTUS]")
        self.KRONOS = Kronos()
        self.ATHENA = athena
        self.LOG.print("Initiating Hephaestus...")


    def get_option_price(self, symb, strike, expr, call):
        self.LOG.print("Job Submitted to Hephaestus...")
        info = self.ATHENA.get_single_stock(symb)
        days_til = self.KRONOS.calculate_market_days_inaccurate(date.today(), expr)
        price = round(self.black_scholes_formula(info["curr_price"], strike, days_til, call, info), 6)
        self.LOG.print(f"Job Completed. Current option for {symb} with a strike of {strike} on {expr} has a theoretical price of ${price}")
        return price

    #############################################################
    #               The Black-Scholes Calculation               #
    #############################################################
    """
    Pre:
        S -> Current Stock Price (Or other underlying price for estimation)
        K -> Strike Price
        r -> Risk Free Interest Rate (0.05???)
        t -> Time to Maturity (In Years)
        sigma -> Volatility
        
    Post:
        P -> Current Option Price
    """

    def black_scholes_formula(self, S, K, t, call, symb):
        self.LOG.print("Initiating Black-Scholes Formula...")
        r = self.INTEREST_RATE # placeholder basic value til I figure out how to calculate
        sigma = self.calculate_volatility(symb["prices"])
        # converts the days to years til
        t = t/self.TRADING_DAYS

        if call:
            P = self.black_scholes_call(S, K, r, t, sigma)
        else:
            P = self.black_scholes_put(S, K, r, t, sigma)

        self.LOG.print("Black-Scholes Formula Completed!")

        return P

    def black_scholes_put(self, S, K, r, t, sigma):
        self.LOG.print("Calculating Put Price...")
        d1, d2 = self.calc_d1_d2(S, K, r, t, sigma)
        C = K * np.exp(-r * t) * norm.cdf(-d2) - S * norm.cdf(-d1)
        return C

    def black_scholes_call(self, S, K, r, t, sigma):
        self.LOG.print("Calculating Call Price...")
        d1, d2 = self.calc_d1_d2(S, K, r, t, sigma)
        P = S * norm.cdf(d1) - K * np.exp(-r * t) * norm.cdf(d2)
        return P

    def calc_d1_d2(self, S, K, r, t, sigma):
        d1 = ((np.log(S/K) + t * (r + ((sigma * sigma)/2)))/(sigma * np.sqrt(t)))
        d2 = d1 - (sigma * np.sqrt(t))
        return d1, d2

    def calculate_volatility(self, prices):
        # Daily returns as percentage change from one day to next
        daily_returns = np.diff(prices) / prices[:-1]
        # Variance in these returns
        variance = np.var(daily_returns)
        # Standard Deviation of the variance
        std_dev = np.sqrt(variance)
        # Standard Dev multiplied by the trading days normalized for annualized volatility
        sigma = std_dev * np.sqrt(self.TRADING_DAYS)
        return sigma



#h = Hephaestus()
#h.get_option_price("PAA", 25, date(2026, 1, 26), True)