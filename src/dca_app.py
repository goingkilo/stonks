import sys
import json
sys.path.append('.')
import alpha_v2 as a

from flask import render_template
from flask import Flask
app = Flask(__name__)


results_cache = []

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/chart')
def chart():
    return render_template('chart.html')

@app.route('/dca_roi_chart')
def dca_roi_chart():
    return render_template('cost_returns_chart.html')

@app.route('/dca_roi_data')
def dca_roi_data():
    return results_cache[0]

@app.route('/dca/<scrip>/<int:amount>')
def get_dca(scrip,amount):

    d = a.AlphavantageData()
    d.load( scrip)
    b = a.simulation( d, scrip=scrip,amount=amount)


    _json =  json.dumps(b,default=lambda o: o.__dict__)
    results_cache.append( _json)

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