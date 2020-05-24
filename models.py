
BUY 	= 'buy'
SELL 	= 'sell'

class Stock:
    def __init__(self,a):
        if 'null' in a:
            return None
        self.date		= a[0]
        self.open 		= a[1]
        self.high 		= a[2]
        self.low 		= a[3]
        self.close 		= a[4]
        self.vol 		= a[5]
    def to_s(self):
        return  """({},{},{},{},{},{})""".format( self.date, self.open, self.high, self.low, self.close, self.vol )

    def to_str(self):
        a=  """
		Date: 		{}
		Open: 		{}
		High: 		{}
		Low: 		{}
		Close:      {}
		Volume: 	{}
		""".format( self.date, self.open, self.high, self.low, self.close, self.vol )
        return a


class Transaction:
    def __init__(self, scrip, buy_sell, date, price, qty):
        self.scrip = scrip
        self.action = buy_sell
        self.date = date
        self.price = price
        self.qty = qty

    def tx_value(self):
        amt = float(self.price) * self.qty
        if self.action == BUY:
            return - amt
        return amt

    def to_str(self):
        return  """({},{},{},{},{})""".format( self.scrip, self.action, self.date, self.price, self.qty)

class Scenario():
    def __init__(self, starting_year, num_months, amount, profit, investment, ledger):
        self.d = {}
        self.d['starting_year']     = starting_year
        self.d['num_months']        = num_months
        self.d['amount']            = amount
        self.d['profit']            = profit
        self.d['investment']        = investment
        self.d['roi']               = round((self.get('profit')/ self.get('investment')) * 100,2)
        self.d['ledger']            = ledger

    def get(self,key):
        a =  self.d.get(key,None)
        if not a:
            print(key)
        return a

    def to_str(self):
        return  """ Return for Rs {} / {} months starting from {} is {}""".format(
            self.get('amount'), self.get('num_months'), self.get('starting_year'), self.get('roi')
        )

