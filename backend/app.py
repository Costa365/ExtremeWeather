# compose_flask/app.py
import json
from flask import Flask, jsonify
from ogimet import Ogimet

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['JSON_SORT_KEYS'] = False

ogimet1 = Ogimet()

@app.route('/')
def id():
  info = {'name': 'Daily Weather Extremes', 'version': 'v0.1'}
  return jsonify(info)

@app.route('/regions')
def getRegions():
  return jsonify(ogimet1.getRegions())

@app.route('/results/<region>')
def geToday(region):
  return jsonify(ogimet1.getResults(region))

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
