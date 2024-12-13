"""
Title: Options Profit Calculator
CodeName: Hephaestus
Reason: Hephaestus is the god of invention and forge, this is a tool to be used by the rest of the bots
"""

import numpy as np
from scipy.stats import norm
import Log as l
import yfinance as yf

class Hephaestus:

    TRADING_DAYS = 252
    INTEREST_RATE = 0.05
    LOG = None

    def __init__(self):
        self.LOG = l.Log("[HEPHAESTUS]")
        self.LOG.print("Initiating Hephaestus...")


    def get_option_price(self, symb, strike, expr):
        self.LOG.print("Job Submitted to Hephaestus...")
        info = self.get_information(symb)
        #self.black_scholes_formula(info["curr_price"], strike, )
        # TODO: Figure out how to get trading days between today and expr (NOTE: not just business days)


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

        if call:
            P = self.black_scholes_call(S, K, r, t, sigma)
        else:
            P = self.black_scholes_put(S, K, r, t, sigma)

        self.LOG.print("Black-Scholes Formula Calculated!")

        return P

    def black_scholes_call(self, S, K, r, t, sigma):
        self.LOG.print("Calculating Call Price...")
        d1, d2 = self.calc_d1_d2(S, K, r, t, sigma)
        C = K * np.exp(-r * t) * norm.cdf(-d2) - S * norm.cdf(-d1)
        return C

    def black_scholes_put(self, S, K, r, t, sigma):
        self.LOG.print("Calculating Put Price...")
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



    #############################################################
    #                     Stock API Functions                   #
    #############################################################

    def get_information(self, symb):
        # get all stock information needed for program
        # return list in dict or tuple*
        self.LOG.print("Gathering Information")
        ticker = yf.Ticker(symb).history(period='1y')
        rez = {"curr_price": round(ticker['Close'].iloc[-1], 6), "prices": [round(ticker['Close'].iloc[x], 6) for x in range(len(ticker['Close'].tolist()))]}
        return rez


h = Hephaestus()
h.get_information('MSFT')