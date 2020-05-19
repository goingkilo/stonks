import csv

cols = 'Date,Open,High,Low,Close,Adj Close,Volume'.split(',')

def load(filename):
	data = []
	with open(filename) as f:
		f1 = csv.reader( f, delimiter=',')
		for i in f1:
			data.append(i)
	return data



def get(key,data_row):
	return data_row[ cols.index( key))


g_date = lambda  r:get( 'Date', r)
g_open = lambda  r:get( 'Open', r)
g_high = lambda  r:get( 'High', r)
g_low = lambda  r:get( 'Low', r)
g_close = lambda  r:get( 'Close', r)
g_vol = lambda  r:get( 'Volume', r)
	


a = load( 'RELIANCE.NS.all.csv')
print( 'loaded ' , len(a), ' rows')
