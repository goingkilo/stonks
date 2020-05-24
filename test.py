
import alpha as a


def test():
    b = a.get_first(2010,11)
    c = a.stocks.get(b)

    print( c.to_str())



a.simulation()