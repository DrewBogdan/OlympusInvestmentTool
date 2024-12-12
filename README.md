# *Olympus* Investment Tool
Author: Drew Bogdan
## The Challange
We(A couple friends of mine) have decided that together we want to make an investing bot to give money and see how the profit rolls if it does and how we could build a bot to read the market. but because we are all new to this and it would be tough to all start from the bottom and be at different levels of knowledge, We decided that by the new year we all want to have a basic bot running and building profit on simulated given cash, and then after 4 months we will reconvene and see where eachothers bots are, who made the most and why, and if there was a science to the best or luck then combine our now gotten knowledge to see where we can work together in a large bot to make money on the actual market. 

## Major Pieces
- Develop a options price calculator and profit calculator based on a stocks current data
- Develop a bot to utilize information of a possible profit for an option based on likelihood following the stocks previous movement and current stigma for it online (webscraping?)
- Develop a bot to scan and get status updates on a large set of stocks, either create one big one, or separate bots for each different area (Tech, Healthcare, Finance, Metals, Oil, etc)
- Develop a scanning algorithm for a few stock trends and unleash it to the scanning bots to have it decide if any match the stock trends and invest amounts in either options based on possible profit with the trend direction, or into the stock itself if the trend direction doesnt give the confidence level required to build
- Develop a discord bot to report all data from these bots, giving updates on stock prices, and updates on portfoilo account
- Change the investing from simulated investing to actual investing when the bot gets to a trusted direction (After the 4 month adjusting and extra dev period following the 21 day code-off)


### API's
- Market Data API: https://polygon.io/pricing?product=stocks
- Investing Data API (includes crypto): https://finnhub.io/pricing
- Possible Simulation API: https://ninjatrader.com/trading-platform/trading-simulator/
- Actual Investing API: https://alpaca.markets/


### Ideal 21 day plan
- Finish Options Profit Calculator (2 Days)
- Finish Stock Trend Algorithm bot on a few stock trends and trade based on stock movement and likelihood (12 Days)
- Decide on margin of profit for when the bot should pull all vs pull to recoup investment for pure profit run until larger profit margin and code in (1 Day)
- Finish Discord Bot to monitor the progress of the stock amount, and the volatility of market and stock values (4 Days)
- Get persistent stock management for the bot and set to run (2 days)

### Options Profit Calculator (Hephaestus)
- Plenty of tutorials online, start with this to get basic understanding of how stocks move, what goes into options profit, and getting started with actual investing values
- Build as a class structure to then implement into a large cohesive bot program as the project builds
- Utilize the Black-Scholes method to calculate stocks, and ensure volatility is correctly calculated each time
- Either make a set interest rate, or actively calculate with treasury bonds lol

### Likelihood Of Profit Bot with Options (Hades)
- Bit more of an involved bot to build, use the options profit calculator to find options with large profit output that have a heavy positive sentiment in online forums (WSB) and general investing news sites
- Use the profit calculator to find the lowest risk high reward for where the stock is likely going.

### Stock Scanning Bot (Athena)
- Build a bot to scan and report data on large amount of stocks
- Find a way for values to well displayed for users and another result for computers to understand
- Find a way for the values to be checked
- Build a large list of stocks for the bot to scan

### Stock Trend Algorithm for Investment (Poseidon)
- Build a bot to use the data bot to get data in a computer format to make descisions on Support/Resistance Situations, Downtrends, Uptrends and Sideways Trends
- Eventually add in support for trends such as Pullbacks, Reversals, Breakouts, Overbought, Oversold

### Discord bot to Report (Hermes)
- Use Woka as a template for the commands and responses, feed information through either a DB or a direct connection into the stock algorithm
- Even better idea, have algorithm regularly print progress to a text file, have bot read from that text file to produce values

### Real Time Investing Bot utilizing previously made bots (Zeus)
- Move the bot to instead of trading on the simulated trading API to the Alpaca direct API and use actual money to start making trades and make money. 

#
### Current Progress
#### Day 1
- Wrote the outline for how the bot should be built and researched APIs for simulated trading and actual trading

#### Day 2
- Named bot and each piece of the bot follows naming convention
- Built out calculations for the black-scholes options calculation
- Built log class to tag messages of their origin functions. will be useful as functions start to utilize eachother.
