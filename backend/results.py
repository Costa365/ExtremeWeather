import re

class Results():
  def __init__(self, html):
    self.html = html.replace("&#176;C", "°C")
    self.sections = {
      "maximum": ["Maximum temperature in 24h. ",0],
      "minimum": ["Minimum temperature in 24h. ",0],
      "precipitation": ["24 hours amount precipitation. ",0],
      "wind": ["Maximum wind Gust in 24 hours. ",0]
    }
    self.__findSectionPositions()
    self.resultsMax = self.__parseResults(self.sections["maximum"][1],self.sections["minimum"][1])
    self.resultsMin = self.__parseResults(self.sections["minimum"][1],self.sections["precipitation"][1])
    self.resultsPrc = self.__parseResults(self.sections["precipitation"][1],self.sections["wind"][1])
    self.resultsWin = self.__parseResults(self.sections["wind"][1],len(self.html))
    self.title = self.__parseTitle()

  def __parseRes#### ults(self, start, end):
    results=[]
    if start > 0 and end > 0:
      html = self.html[start:end]
      results = re.findall(r"<a href=\"\./gsynres.*?>(.*?)<.*?<b>(.*?)(?=</b>)", html, re.IGNORECASE | re.MULTILINE | re.DOTALL)
    return results

  def __parseTitle(self):
    title = []
    results = re.findall(r"<H3>(.*?)</h3>", self.html, re.IGNORECASE)
    title.append(results[0])
    results = re.findall(r"<H4>(.*?UTC)</h4>", self.html, re.IGNORECASE)
    title.append(results[0])
    return title

  def __findSectionPositions(self):
    self.sections["maximum"][1] = self.html.find(self.sections["maximum"][0])
    self.sections["minimum"][1] = self.html.find(self.sections["minimum"][0])
    self.sections["precipitation"][1] = self.html.find(self.sections["precipitation"][0])
    self.sections["wind"][1] = self.html.find(self.sections["wind"][0])

  def getMaximums(self):
    return self.resultsMax

  def getMinimums(self):
    return self.resultsMin

  def getMaxPrecip(self):
    return self.resultsPrc
  
  def getMaxWind(self):
    return self.resultsWin
  
  def getTitle(self):
    return self.title

  def getAll(self):
    all = []
    all.append(self.title)
    extremes = {}
    extremes["Maximum Temperature"] = self.resultsMax
    extremes["Minimum Temperature"] = self.resultsMin
    extremes["Maximum Precipitation"] = self.resultsPrc
    extremes["Maximum Wind Gust"] = self.resultsWin
    all.append(extremes)
    return all
