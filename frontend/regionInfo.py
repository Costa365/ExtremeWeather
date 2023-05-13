import requests

class RegionInfo():
  def __init__(self):
    pass

  def getRegions(self):
    request = "http://extreme-weather-backend:5004/regions"
    r = requests.get(request)
    return r.json()

  def getResults(self, region):
    request = "http://extreme-weather-backend:5004/results/{0}".format(region)
    r = requests.get(request)
    return r.json()

  
