# compose_flask/app.py
import json
from flask import Flask, render_template
from regionInfo import RegionInfo

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

regionInfo1 = RegionInfo()
regions = regionInfo1.getRegions()

@app.route('/')
def home():
  results = regionInfo1.getResults("World")
  return render_template('main.html', regions=regions, results=results) 

@app.route('/<region>')
def region(region):
  results = regionInfo1.getResults(region)
  return render_template('main.html', regions=regions, results=results) 

if __name__ == "__main__":
  app.run(host="0.0.0.0", port="5005", debug=True)
