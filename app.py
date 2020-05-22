from data import Stock, Data





BUY = 'buy'
SELL = 'sell'

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

class DCA :
	def __init__(self):
		self.ledger = []
		self.d = Data()

	def run( self, starting_year, num_years, amount):
		#print( "Start" ,starting_year)
		for y in range( num_years):
			#print( starting_year + y)
			for m in range( 1,13):
				s = self.d.get_first_working_day( starting_year+ y,m)
				if not s:
					print ("Empty",y,m)

				qty = int(amount/float(s.high))
				#print( '\t',m, ':' , s.date, qty, 'at', s.high)
				self.ledger.append( Transaction( 'Reliance', BUY,  s.date, s.high, qty))

		sell = self.d.get_last_working_day( starting_year + num_years -1, 12)
		total_qty = sum( [x.qty for x in self.ledger])
		self.ledger.append( Transaction( 'Reliance', SELL,  sell.date, sell.low, total_qty))
		#print( "End :", sell.date )


	def maturity_value(self):
		return ( sum( [x.tx_value() for x in self.ledger]))

	def investment(self):
		return sum([ float(x.price)*x.qty  for x in self.ledger if x.action == BUY])

	def clear(self):
		self.ledger = []


num_years = 3
starting  = 1996
amount    = 10000

dca = DCA()
while starting < (2020-3):
	dca.run( starting, num_years, amount)
	f = dca.maturity_value()
	i = dca.investment()
	print( starting, num_years, amount, round(f,2), round(i,2) ,round(((f/i)*100),2))
	dca.clear()

	starting +=1
