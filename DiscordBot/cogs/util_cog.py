from discord.ext import commands
from datetime import date, datetime
from Hephaestus import Hephaestus
class Util(commands.Cog):

    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.command(name='call', description='Checks the options call price for given symbol', pass_context=True)
    async def call(self, ctx, symb: str, strike: str, expr: str):
        try:
            if expr is None or strike is None or symb is None:
                await ctx.send("Missing Arguments for Call Command. ```Correct Usage: !call [Stock Symbol] [Strike Price] [Expiration in m%/d%/yyyy format] ```")
            expr = datetime.strptime(expr, '%m/%d/%Y').date()
            h = Hephaestus()
            price = h.get_option_price(symb, int(strike), expr, True)
            await ctx.send(f"Current Call option for {symb} with a strike of {strike} on {expr} has a theoretical price of ${price}")
        except Exception as err:
            print(Exception, err)
            await ctx.send("Unknown Error. :)")

    @commands.command(name='put', description='Checks the options put price for given symbol', pass_context=True)
    async def put(self, ctx, symb: str, strike: str, expr: str):
        try:
            if expr is None or strike is None or symb is None:
                await ctx.send(
                    "Missing Arguments for Call Command. ```Correct Usage: !call [Stock Symbol] [Strike Price] [Expiration in m%/d%/yyyy format] ```")
            expr = datetime.strptime(expr, '%m/%d/%Y').date()
            h = Hephaestus()
            price = h.get_option_price(symb, int(strike), expr, False)
            await ctx.send(
                f"Current Put option for {symb} with a strike of {strike} on {expr} has a theoretical price of ${price}")
        except Exception as err:
            print(Exception, err)
            await ctx.send("Unknown Error. :)")
