"""Create a file in your repository called portfolio.py by using VSCode from GitHub Desktop, as we did a few weeks ago.

Within it, define a new class called Portfolio which:

has a method called buy, which adds a new stock to the portfolio, taking 3 arguments

name, a str, the symbol of the stock which is being bought

shares, an int, the quantity which is being bought

price, a float, the price paid per share

and has a second method called cost which returns a float, the total cost paid for all stocks in the portfolio

Consider that to implement the cost method, you'll need to be storing the purchases made each time the buy method is called somewhere. You may do so by any means convenient to you."""

class Portfolio:
    
    def __init__(self, stocks):
        self. stocks = []   

    def buy (self, name, shares, price):
        self.stocks.append(dict{"name" = name, "shares" = shares, "price" = price})

    def cost (self):
        sum = 0
        for i in stocks:
            temp = i[dict["shares"]] * i[dict["price"]]
            sum = sum + temp
        return sum 
