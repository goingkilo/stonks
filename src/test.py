import sys
sys.path.append('..')
import alpha_v2 as a
from models import Scenario


def test():
    b = a.get_first(2010,11)
    c = a.stocks.get(b)

    print( c.to_str())

def test2():
    d = a.AlphavantageData()
    d.load( 'RELIANCE.NS')
    b = a.simulation(d)
    for i in b:
        print( i.to_str())


def test3():
    try:
        a = Scenario()

    except TypeError:
        a = Scenario(1,2,3,4,5,6,7)
        print(a)
        b  = [a]
        c = [x.d for x in b]
        print(c)



test3()