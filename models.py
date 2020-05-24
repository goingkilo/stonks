
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
    def to_str(self):
        a=  """
		Date: 		{}
		Open: 		{}
		High: 		{}
		Close: 		{}
		Adjusted Close: {}
		Volume: 		{}
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
        return amt;

class Scenario():
    def __init__(self, starting_year, num_years, amount, profit, investment):
        self.d = {}
        self.d['starting_year'] = starting_year
        self.d['ending_year'] = starting_year + num_years -1
        self.d['amount'] = amount
        self.d['profit']  = profit
        self.d['investment'] = investment
        self.d['roi'] = round((self.get('profit')/ self.get('investment')) * 100,2)

    def get(self,key):
        a =  self.d.get(key,None)
        if not a:
            print(key)
        return a

    def to_str(self):
        a=  """
		starting_year: 		{}
		ending_year: 		{}
		amount: 		{}
		profit: 		{}
		investment: 		{}
		roi: 			{}
		""".format( self.get('starting_year'),
                    self.get('ending_year'),
                    self.get('amount'),
                    self.get('profit'),
                    self.get('investment'),
                    self.get('roi') )
        return a
