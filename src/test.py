import sys
sys.path.append('..')
import alpha_v2 as a


def test():
    b = a.get_first(2010,11)
    c = a.stocks.get(b)

    print( c.to_str())

d = a.AlphavantageData()
d.load( 'RELIANCE.NS')
b = a.simulation(d)
for i in b:
    print( i.to_str())
