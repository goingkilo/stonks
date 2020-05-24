import urllib.request
import shutil
import os
import csv
from datetime import datetime
import logging

logging.basicConfig(filename="alpha.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger=logging.getLogger()
logger.setLevel(logging.DEBUG)


from models import Stock,Scenario,Transaction

def to_date(d):
    return datetime.strptime( d, '%Y-%m-%d')


base_url = """https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=RELIANCE.NS&apikey=9VEZAZD61Q1LAOXJ&datatype=csv"""


def download(symbol, force=False):

    file_name = os.path.join( './data/' ,symbol+ '.csv')
    logger.debug( "download: file name {}".format( file_name))

    url = base_url.replace( 'RELIANCE.NS', symbol)
    logger.debug("download: url {}".format( url))

    if os.path.exists( file_name) and not force:
        logger.info('download: dataset exists, skipping download')
        return file_name

    with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)
    return file_name



filename = download('RELIANCE.NS')
logger.debug( 'main:filename {}'.format(filename))
#data
stocks = {}

# get stocks
with open(filename) as f:
    rows = csv.reader( f, delimiter=',')
    for row in rows:
        if 'null' in row or 'Date' in row or 'timestamp' in row:
            logger.info( "skipping row {}".format(row))
            continue
        stock = Stock(row)
        stocks[stock.date] =  stock


#data
dates = sorted( stocks.keys(), key = to_date)
logger.debug( " dates-start :\n {} \ndates-end".format('\n'.join(dates)))


#data
year_months = {}
for i in dates:
    ym = i.split('-')[0]+'_'+i.split('-')[1]
    l = year_months.get( ym,[])
    l.append( i)
    year_months[ym] = l

for i in year_months.keys():
    logger.debug( " year-month key :  {}".format(i))
    l  = year_months[i]
    l.sort(key = to_date)
    year_months[i] = l
    logger.debug( " year-month key start:\n   {}  \nyear-month ey end ".format( ' '.join(year_months[i]) ))

def get_first(year,month):
    key = i.split('-')[0]+'_'+i.split('-')[1]
    a = year_months.get( key, "YM Value not present")
    if a:
        return a[0]
    return None

def get_last(year,month):
    key = i.split('-')[0]+'_'+i.split('-')[1]
    a = year_months.get( key, "YM Value not present")
    if a:
        return a[-1]
    return None


