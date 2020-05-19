import csv
from datetime import datetime
import datetime

cols = 'Date,Open,High,Low,Close,Adj Close,Volume'.split(',')

def load(filename):
	data = []
	with open(filename) as f:
		f1 = csv.reader( f, delimiter=',')
		for i in f1:
			data.append(i)

	return data


def to_map(d):
	r = {}
	for i in d:
		key = i[0]
		value = i
		r[key] = i
	return r
		

def  get(key,data_row):
	return data_row[ cols.index( key)]


g_date = lambda  r:get( 'Date', r)
g_open = lambda  r:get( 'Open', r)
g_high = lambda  r:get( 'High', r)
g_low = lambda  r:get( 'Low', r)
g_close = lambda  r:get( 'Close', r)
g_vol = lambda  r:get( 'Volume', r)
	
def transaction( historical_prices, buy_date, sell_date, qty):
	buy_price = historical_prices.get[buy_date]  
	sell_price = historical_prices.get[sell_date]  
	return qty * (sell_price - buy_price)


def to_date(d):
	x = datetime.strptime( d, '%Y-%m-%d')
	return x



a = load( 'RELIANCE.NS.all.csv')
print( 'loaded ' , len(a), ' rows')


b = to_map(a)

dates = [x[0] for x in a]
print( dates[0])
print( dates[1])
print( dates[-1])



