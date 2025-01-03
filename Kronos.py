
import Log as l
from datetime import date

class Kronos:

    LOG = None
    def __init__(self):
        self.LOG = l.Log("[KRONOS]", "green")
        self.LOG.print("Initiating Kronos...")

    """
        Function will utilize calculate_business_days() and check_holidays()

        Pre:
            today -> Current date of when the program was run
            expire -> expire date of the options contract
    """
    def calculate_market_days(self, today, expire):
        self.LOG.print("Calculating Market Days...")
        count = self.calculate_business_days(today, expire) - self.check_holidays(today, expire)
        self.LOG.print("Market Days Sucessfully Calculated [" + count + "]!")
        return count

    """
        Function will calculate the total number of business days between today and the options expire

        Pre:
            today -> Current date of when the program was run
            expire -> expire date of the options contract
        Post:
            count -> total number of business days between the 2 dates
    """
    def calculate_business_days(self, today, expire):
        return 0

    """
        Function will check if any market holidays line up in the range from today to options expire
            and return the total number to be subtracted
        
        Pre:
            today -> Current date of when the program was run
            expire -> expire date of the options contract
        Post:
            count -> total number of market holidays between the 2 dates as an int
    """
    def check_holidays(self, today, expire):
        return 0


    def calculate_market_days_inaccurate(self, today, expire):
        self.LOG.print("Inaccurate Calculation Running...")
        delta = (expire - today).days
        ratio = 252.03/365.25
        days_til = delta*ratio
        self.LOG.print(f"Inaccurate Calculation Completed with {days_til} days!")
        return days_til