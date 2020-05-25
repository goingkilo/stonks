import urllib.request
import shutil
import os
import csv
from datetime import datetime
import logging

# import sys
# sys.path.append('.')
from models import Stock,Scenario,Transaction,BUY,SELL

def to_date(d):
    return datetime.strptime( d, '%Y-%m-%d')

#logging
logging.basicConfig(filename="../logs/alpha.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger=logging.getLogger()
logger.setLevel( logging.DEBUG)

REL='RELIANCE.NS'
DATA_FOLDER = '../data/'
base_url = """https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=RELIANCE.NS&apikey=9VEZAZD61Q1LAOXJ&datatype=csv&outputsize=full"""

class AlphavantageData:

    def __init__(self):
        self.stocks     = None
        self.dates      = None
        self.year_months = None
        self.months     = None

    def _download( self, symbol, force=False):

        file_name = os.path.join( DATA_FOLDER ,symbol+ '.csv')
        logger.debug( "download: file name {}".format( file_name))

        url = base_url.replace( 'RELIANCE.NS', symbol)
        logger.debug("download: url {}".format( url))

        if os.path.exists( file_name) and not force:
            logger.info('download: dataset exists, skipping download')
            return file_name

        with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)
        return file_name

    def load(self, symbol):
        filename = self._download(symbol)
        logger.debug( 'main:filename {}'.format(filename))
        #data
        self.stocks = {}

        # get stocks
        with open(filename) as f:
            rows = csv.reader( f, delimiter=',')
            for row in rows:
                if 'null' in row or 'Date' in row or 'timestamp' in row:
                    logger.info( "skipping row {}".format(row))
                    continue
                stock = Stock(row)
                self.stocks[stock.date] =  stock

        #data
        self.dates = sorted( self.stocks.keys(), key = to_date)
        logger.debug( " dates-start :\n {} \ndates-end".format('\n'.join(self.dates)))

        #data
        self.year_months = {}
        for i in self.dates:
            ym = i.split('-')[0]+'_'+i.split('-')[1]
            l = self.year_months.get( ym,[])
            l.append( i)
            self.year_months[ym] = l

        for i in self.year_months.keys():
            logger.debug( " year-month key :  {}".format(i))
            l  = self.year_months[i]
            l.sort(key = to_date)
            self.year_months[i] = l
            logger.debug( " year-month key start:\n   {}  \nyear-month ey end ".format( ' '.join(self.year_months[i]) ))

        ymsorter = lambda x : int(x.split('_')[0])*100 + int(x.split('_')[1])

        #data
        self.months = sorted( self.year_months.keys(), key = ymsorter)

    def get_first( self, year_month):
        a = self.year_months.get( year_month, "YM Value not present")
        if a:
            return a[0]
        return None

    def get_last( self, year_month):
        a = self.year_months.get( year_month, "YM Value not present")
        if a:
            return a[-1]
        return None



def run_sim( d, scrip, a, amount, ledger):
    net_buys = 0
    for i in a:
        f = d.get_first(i)
        s = d.stocks.get(f)
        qty = int(float(amount)/ float(s.high))
        net_buys += qty
        t0 = Transaction( scrip, BUY, s.date, s.high, qty)
        ledger.append(t0)
    a0 = d.get_last(a[-1])
    s0 = d.stocks.get(a0)
    t1 = Transaction( scrip, SELL, s0.date, s0.high, net_buys)
    ledger.append(t1)
    # for i in ledger:
    #     print( i.to_str(), i.tx_value())
    investment = sum([float(x.price) * x.qty for x in ledger if x.action == BUY])

    sale = 0
    profit = 0
    roi = 0
    if not investment == 0:
        sale = sum([ float(x.price) * x.qty for x in ledger if x.action == SELL])
        profit = (sale-investment)
        roi =  round( (profit * 100 ) / investment ,2)
    #print( "Roi for {} months starting {} is {}".format( len(a) , a[0], round( roi,2)))
    scenario = Scenario(a[0], len(a), amount, profit, investment, ledger, roi)
    return scenario


def simulation( d, scrip=REL, batch_size = 12, amount = 100000):
    start = 0
    scenarios = []
    while start + batch_size < len(d.months):
        a =d.months[ start:start + batch_size]
        scenario = run_sim( d, scrip, a, amount, [])
        scenarios.append( scenario)
        start += 1
    #print( 'stopping sim at ',start,'+', batch_size, '/' ,len(months))
    scenarios.sort( key  = lambda x : -x.get('roi'))
    # for i in scenarios:
    #     # persist somewhere
    #     print( '::',i.to_str())

    return scenarios

