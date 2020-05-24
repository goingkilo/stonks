import csv



class Data:

	def __init__(self, filename='yahoo_reliance_all.csv'):
		self.data = {}
		self.dates = []
		self.year_month_data = {}
		self.years = {}
		#print( "Data:loading data")

		with open(filename) as f:
			rows = csv.reader( f, delimiter=',')
			for row in rows:
				if 'null' in row:
					continue
				if 'Date' in row:
					continue
				stock = Stock(row)
				stock_date = stock.date

				self.dates.append( stock_date)
				self.data[stock_date] = stock

				self.years[stock_date.split('-')[0]] = stock_date.split('-')[0]

				year_month = stock_date.split('-')[0]+ '-' + stock_date.split('-')[1]
				ymrow = self.year_month_data.get( year_month, [])
				ymrow.append( stock)
				self.year_month_data[  year_month] = ymrow

			#print( "Data:sorting year-month data")
			# maybe unnecessary
			for ym in self.year_month_data.keys():
				ymrow = self.year_month_data[ym]
				ymrow.sort( key = lambda x:x.date )
				self.year_month_data[ ym] = ymrow


	def get_by_date(self,d):
		return self.data.get(d,None)

	def get_first_working_day(self, year_i, month_i):
		r = self.__get_y_m_data(year_i,month_i)
		if r:
			return r[0]
		return None

	def get_last_working_day(self, year_i, month_i):
		r = self.__get_y_m_data(year_i,month_i)
		if r:
			return r[-1]
		return None

	def __get_y_m_data(self,year_i, month_i):
		if month_i < 10:
			key = str(year_i) + '-0' + str(month_i)
		else:
			key = str(year_i) + '-' + str(month_i)
		return self.year_month_data.get( key, None)

	def get_dates(self):
		return self.dates

	def get_years(self):
		return list( self.years.keys())

def test():
	d = Data()
	import sys

	y = int(sys.argv[1])
	m = int(sys.argv[2])

	a = d.first_working_day( y, m)
	print(a.to_str())
