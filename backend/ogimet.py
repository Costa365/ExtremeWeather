import requests
import atexit
import datetime
from concurrent.futures import ThreadPoolExecutor
from regions import Regions
from results import Results
from apscheduler.schedulers.background import BackgroundScheduler

class Ogimet():
  def __init__(self):
    self.resultsList = {}
    self.regionsList = []
    self.__getRegions()
    executor = ThreadPoolExecutor(5)
    executor.submit(self.__getResults)
    self.__schedulePeriodicUpdate()

  def __schedulePeriodicUpdate(self):
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=self.__getResults, trigger="interval", hours=1)
    scheduler.start()
    atexit.register(lambda: scheduler.shutdown())
  2
  def __getRegions(self):
    res = self.__getHtml("https://www.ogimet.com/ranking.phtml.en")
    regions1 = Regions(res)
    self.regionsList = regions1.getRegions()
  
  def __getResults(self):
    now = datetime.datetime.now()
    for region1 in self.regionsList:
      url = "https://www.ogimet.com/cgi-bin/gsynext?lang=en&state={0}&rank=10&ano={1}&mes={2}&day={3}&hora={4}&Send=send".\
        format(region1[0], now.year, now.month, now.day, now.hour)
      results1 = Results(self.__getHtml(url))
      self.resultsList[region1[0]] = results1.getAll()

  def __getHtml(self, url):
    r = requests.get(url)
    r.encoding = 'UTF-8'
    return r.text

  def getRegions(self):
    return self.regionsList

  def getResults(self, region):
    results = []
    if region in self.resultsList:
      results = self.resultsList[region]
    return results

