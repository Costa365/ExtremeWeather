import re

class Regions():
  def __init__(self, html):
    self.html = html
    self.regions = self.__parseRegions()

  def __parseRegions(self):
    continentsOnlyHtml = self.html[0:self.html.find("value='Afg'")]
    regions = re.findall(r"<OPTION value=['\"](.*?)['\"].*?>(.*?)<", continentsOnlyHtml, re.IGNORECASE)
    return regions

  def getRegions(self):
    return self.regions
