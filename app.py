from data import Stock, Data

BUY 	= 'buy'
SELL 	= 'sell'

class DCA :
	def __init__(self):
		self.ledger = []
		self.d = Data()

	def run( self, starting_year, num_years, amount):
		for y in range( num_years):
			for m in range( 1,13):
				s = self.d.get_first_working_day( starting_year+ y,m)
				if not s:
					print ("Empty",y,m, starting_year)

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
		a = sum([ float(x.price)*x.qty  for x in self.ledger if x.action == BUY])
		return a

	def clear(self):
		self.ledger = []

	def simulate(self, starting, num_years, amount):
		ret = []

		while starting < (2020-3):
			self.run( starting, num_years, amount)
			f = self.maturity_value()
			i = self.investment()
			print( starting, num_years, amount, round(f,2), round(i,2) ,round(((f/i)*100),2))
			r = Scenario( starting, num_years, amount, round(f,2), round(i,2))
			self.clear()
			ret.append(r)
			starting +=1
		return ret

a = DCA()
b = a.dates[0].split('-')
ym = b[0],b[1]
b = a.simulate( y,3,10000)
for i in b:
	print( i.to_str())
