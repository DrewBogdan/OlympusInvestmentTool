# *Olympus* Investment Tool
Author: Drew Bogdan
## The Challange
We(A couple friends of mine) have decided that together we want to make an investing bot to give money and see how the profit rolls if it does and how we could build a bot to read the market. but because we are all new to this and it would be tough to all start from the bottom and be at different levels of knowledge, We decided that by the new year we all want to have a basic bot running and building profit on simulated given cash, and then after 4 months we will reconvene and see where eachothers bots are, who made the most and why, and if there was a science to the best or luck then combine our now gotten knowledge to see where we can work together in a large bot to make money on the actual market. 

## Major Functions
- Develop a options price calculator and profit calculator based on a stocks current data
- Develop a bot to utilize information of a possible profit for an option based on likelihood following the stocks previous movement and current stigma for it online (webscraping?)
- Develop a bot to scan and get status updates on a large set of stocks, either create one big one, or separate bots for each different area (Tech, Healthcare, Finance, Metals, Oil, etc)
- Develop a scanning algorithm for a few stock trends and unleash it to the scanning bots to have it decide if any match the stock trends and invest amounts in either options based on possible profit with the trend direction, or into the stock itself if the trend direction doesnt give the confidence level required to build
- Develop a discord bot to report all data from these bots, giving updates on stock prices, and updates on portfoilo account
- Change the investing from simulated investing to actual investing when the bot gets to a trusted direction (After the 4 month adjusting and extra dev period following the 21 day code-off)


### API's
- ~~Market Data API: https://polygon.io/pricing?product=stocks~~
- ~~Market Data API: https://www.alphavantage.co/documentation/~~
- Market Data API: https://finazon.io/dataset/sip_non_pro
  - Seems to have a really good deal for raw data unprocessed. 
- Investing Data API (includes crypto): https://finnhub.io/pricing
- Possible Simulation API: https://ninjatrader.com/trading-platform/trading-simulator/
- Actual Investing API: https://alpaca.markets/
  - They also offer APIs that are free for real time data, but with money in their brokerage could also offer it although it wont give me a clear price on how much that costs. 
- Other Idea: ChatGPT api
  - could just ask chatgpt for the information after training the instance to respond the correct way. might be cheaper if possible to get it to respond the correct way. need to talk to AJ about that with his extensive gpt work/knowledge


### Ideal 21 day plan
- Finish Options Profit Calculator (2 Days)
- Finish Stock Trend Algorithm bot on a few stock trends and trade based on stock movement and likelihood (12 Days)
- Decide on margin of profit for when the bot should pull all vs pull to recoup investment for pure profit run until larger profit margin and code in (1 Day)
- Finish Discord Bot to monitor the progress of the stock amount, and the volatility of market and stock values (4 Days)
- Get persistent stock management for the bot and set to run (2 days)

## Major Function Breakdown

### Options Profit Calculator (Hephaestus)
- Plenty of tutorials online, start with this to get basic understanding of how stocks move, what goes into options profit, and getting started with actual investing values
- Build as a class structure to then implement into a large cohesive bot program as the project builds
- Utilize the Black-Scholes method to calculate stocks, and ensure volatility is correctly calculated each time
- Either make a set interest rate, or actively calculate with treasury bonds lol
  - Screw that im just gunna make it a base one for now as its in the rough stages

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

### Date to Market days calculator (Kronos)
- create a system that can take an experiation date and the current date and find the amount of market days between the 2
- needs to trunkate divided by 252 as that is how many market days there are per year
- does leap year affect this?
- basically need to do business days but get rid of holidays

### Real Time Investing Bot utilizing previously made bots (Zeus)
- Move the bot to instead of trading on the simulated trading API to the Alpaca direct API and use actual money to start making trades and make money. 

#
### Current Progress
#### Day 1 (12/10/24)
- Wrote the outline for how the bot should be built and researched APIs for simulated trading and actual trading

#### Day 2 (12/11/24)
- Named bot and each piece of the bot follows naming convention
- Built out calculations for the black-scholes options calculation
- Built log class to tag messages of their origin functions. will be useful as functions start to utilize eachother.

#### Day 3 (12/12/24)
- Research into shitty investment APIs and how they all cost money to do anything
- Basically heavy research day, trouble getting motivation to work on much else with the annoying findings that its not easily accessable. stupid me for assuming that
- did some work on Hephaestus to use the yfinance package for now to get data from yesterday. (or is it 15 minute delayed as it is last close, idk)

#### Day 4 (12/13/24)
- Did not get work done today

#### Day 5 (12/14/24)
- Worked to create Kronos, time calculator for dates. 
- debated between an exact count of days or a close estimate with percentage chance. will have to try tommorow to see how the exact seems

#### Day 6 (12/15/24)
- Nothin

#### Day 7 (12/16/24)
- finished up basic version of kronos calculation and started connecting information to get basic options prices set up
- honestly the innacurate timing is not too bad with early testing. should work for now until i get it to be much more sophisticated
- Connected all the pieces in Hephestus and successfully calculated current options prices
- Found bug where my call and put functions were reversed. Oops
- Had idea to develop the bot to see theoretical value vs actual value of stocks to buy under values options chains

#### Day 8 (12/17/24)
- Basic work on Athena today and some research into making the large stock searches through apache