import sys
import json
sys.path.append('.')
import alpha_v2 as a

from flask import render_template
from flask import Flask
app = Flask(__name__)


d = a.AlphavantageData()
cache = {}

@app.route('/chart')
def dca_roi_chart():
    return render_template('cost_returns_chart.html')


@app.route('/data/')
def dca_roi_data():

    scrip='RELIANCE.NS'
    amount=10000

    if scrip in cache:
        return cache[scrip]

    d.load( scrip)
    b = a.simulation( d, scrip=scrip,amount=amount)

    c = [x.d for x in b]
    for i in c:
        i['starting_year'] = i['starting_year'].split('_')[0] + '-' +  i['starting_year'].split('_')[1]
        i['price'] = i['ledger'][0].price
    _json =  json.dumps( c, default=lambda o: o.__dict__)
    cache[scrip] = _json
    return _json


@app.route('/dca/<scrip>/<int:amount>')
def get_dca(scrip,amount):
    d.load( scrip)
    b = a.simulation( d, scrip=scrip,amount=amount)

    header  =  "Rs.{}/- per month, starting {}, for {} months ".format(
        b[0].get('amount'),
        b[0].get('starting_year'),
        len(b[0].get('ledger'))-1
    )
    return render_template('returns.html',
                           data = b,
                           scrip = b[0].get('ledger')[0].scrip,
                           scenario_info = header)



"""
starting_year
num_months
        self.d['amount']            = amount
        self.d['profit']            = profit
        self.d['investment']        = investment
        self.d['roi']               = roi
        self.d['ledger']            = ledger
"""