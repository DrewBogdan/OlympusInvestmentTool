import discord
from discord.ext import commands
from datetime import date, datetime
from Hephaestus import Hephaestus
from Athena import  Athena
from Poseidon import Poseidon
import traceback
class Stocks(commands.Cog):

    HEPHAESTUS = None
    ATHENA = None
    POSEIDON = None
    def __init__(self, bot) -> None:
        self.bot = bot
        self.ATHENA = Athena()
        self.HEPHAESTUS = Hephaestus(self.ATHENA)
        self.POSEIDON = Poseidon(self.ATHENA, self.HEPHAESTUS)

    @commands.command(name='call', description='Checks the options call price for given symbol', pass_context=True)
    async def call(self, ctx, symb: str = None, strike: str = None, expr: str = None):
        try:
            if expr is None or strike is None or symb is None:
                await ctx.send("Missing Arguments for Call Command. ```Correct Usage: !call [Stock Symbol] [Strike Price] [Expiration in m%/d%/yyyy format] ```")
                return
            expr = datetime.strptime(expr, '%m/%d/%Y').date()
            h = self.HEPHAESTUS
            price = h.get_option_price(symb, int(strike), expr, True)
            await ctx.send(f"Current Call option for {symb} with a strike of {strike} on {expr} has a theoretical price of ${price}")
        except Exception as err:
            print(Exception, err)
            await ctx.send("Unknown Error. :)")

    @commands.command(name='put', description='Checks the options put price for given symbol', pass_context=True)
    async def put(self, ctx, symb: str = None, strike: str = None, expr: str = None):
        try:
            if expr is None or strike is None or symb is None:
                await ctx.send("Missing Arguments for Call Command. ```Correct Usage: !call [Stock Symbol] [Strike Price] [Expiration in m%/d%/yyyy format] ```")
                return
            expr = datetime.strptime(expr, '%m/%d/%Y').date()
            h = self.HEPHAESTUS
            price = h.get_option_price(symb, int(strike), expr, False)
            await ctx.send(f"Current Put option for {symb} with a strike of {strike} on {expr} has a theoretical price of ${price}")
        except Exception as err:
            print(Exception, err)
            await ctx.send("Unknown Error. :)")

    @commands.command(name='info', description='Retrives info for a single stock symbol', pass_context=True)
    async def get(self, ctx, symb: str = None, section: str = None):
        try:
            if symb is None:
                await ctx.send("Missing Arguments for Info Command. ```Correct Usage: !info [Stock Symbol] [Section Choice]```")
                return
            if section is None or section.lower() not in ['o', 'a', 'c', 'i', 'q', 'p']:
                # [O]verview, [A]nalyst, [C]alender, current [P]rice, company [I]nfo, [Q]uarterly statement
                await ctx.send("Missing Section Choice. ```Possible Sections:\nO - General Overview of the stock\nC - Calender information of the stock"
                               "\nP - Current Price information of the stock\nA - Current analyst predictions of the stock\nI - Comapny Information of the stock\nQ - Current Quarterly information of the stock```")
                return
            a = self.ATHENA
            info = a.single_stock_grab(symb, section.lower())
            await ctx.send(f"Info for the {symb} stock:\n{info}")
        except Exception as err:
            print(Exception, err)
            await ctx.send("Unknown Error. :)")

    @commands.command(name='candlestick', description='Retrives the candlestick chart for a single stock symbol for today', pass_context=True)
    async def candle(self, ctx, symb: str = None):
        try:
            if symb is None:
                await ctx.send(
                    "Missing Arguments for Info Command. ```Correct Usage: !candlestick [Stock Symbol]```")
                return
            a = self.ATHENA
            candles = a.get_day_candlesticks(symb)
            with open('candlefig.png', 'rb') as f:
                picture = discord.File(f)
                await ctx.send(f"Todays candlestick chart for {symb}:")
                await ctx.send(file=picture)
        except Exception as err:
            print(traceback.format_exc())
            await ctx.send("Very Unknown Error. :)")