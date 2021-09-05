import requests

class RegionInfo():
  def __init__(self):
    pass

  def getRegions(self):
    request = "http://backend:5000/regions"
    r = requests.get(request)
    return r.json()

  def getResults(self, region):
    request = "http://backend:5000/results/{0}".format(region)
    r = requests.get(request)
    return r.json()

  
