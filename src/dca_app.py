import sys
import json
sys.path.append('.')
import alpha_v2 as a

from flask import Flask
app = Flask(__name__)



@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/dca/<scrip>/<int:amount>')
def get_dca(scrip,amount):
    d = a.AlphavantageData()
    d.load( scrip)
    b = a.simulation( d, scrip=scrip,amount=amount)

    return json.dumps(b,default=lambda o: o.__dict__)