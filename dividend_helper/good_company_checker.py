import yfinance as yf
from termcolor import cprint

stocks = ["AAPL", "SPY", "TSLA", "MSFT", "AMZN",]




def  new_checker():
    # for the news checking function I want to find use a ai to check if the new for the stock is good or not that will help me see if it going to be bad
    # a ticker is a stock  symbol
    # uses the stocks array to check all the news information for each individual stock

    for stock in stocks:
        news = (yf.Ticker(stock).news)
        cprint(f'CURRNET NEWS ON STOCKS {stock}', "white","on_yellow")
        for article in news:
            article_title = article["title"]
            article_link = article["link"]
            cprint(f"{stock}'s News ({article_title})", "black", "on_white")
            cprint("Link: ", "black","on_light_green", end="")
            cprint(f"{article_link}", "light_green", "on_white")




def monthly_data_checker():
    pass


new_checker()





