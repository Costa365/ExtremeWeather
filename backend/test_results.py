import unittest

from results import Results

resultsHtml = """
<H3>Ranking of selected weather parameters for Europe</h3>
<h4>08/23/2021 at 06:00 UTC</h4>
<table bgcolor="#FFFFDD" align="center">
<caption><b><font color="#55AA55"><a name="tmax">Maximum temperature in 24h. 08/21/2021 at 17:00 UTC</a></font><br>
(10 of 234 stations)</b></caption>
<tr bgcolor="#FFFFFF"><td>
1 </td>
<Td><a href="./gsynres?lang=en&ind=08410&ano=2021&mes=8&day=21&hora=17&min=0&ndays=30">Cordoba / Aeropuerto (Spain)</a></td>
<td bgcolor="#FF0000" align="right"><font color="#FFFFFF"><b>39.1 &#176;C</b></font>
</td></tr>
<tr bgcolor="#E0E0FF"><td>
2 </td>
<Td><a href="./gsynres?lang=en&ind=08397&ano=2021&mes=8&day=21&hora=17&min=0&ndays=30">Moron De La Frontera (Spain)</a></td>
<td bgcolor="#FF0000" align="right"><font color="#FFFFFF"><b>38.5 &#176;C</b></font>
</td></tr>
<caption><b><font color="#55AA55"><a name="tmin">Minimum temperature in 24h. 08/21/2021 at 17:00 UTC</a></font><br>
(10 of 236 stations)</b></caption>
<tr bgcolor="#FFFFFF"><td>
1 </td>
<Td><a href="./gsynres?lang=en&ind=08032&ano=2021&mes=8&day=21&hora=17&min=0&ndays=30">Nestares (Spain)</a></td>
<td bgcolor="#37FF8E" align="right"><font color="#000000"><b>-6.8 &#176;C</b></font>
</td></tr>
<tr bgcolor="#E0E0FF"><td>
2 </td>
<Td><a href="./gsynres?lang=en&ind=08033&ano=2021&mes=8&day=21&hora=17&min=0&ndays=30">Polientes-Casyc (Spain)</a></td>
<td bgcolor="#37FF8E" align="right"><font color="#000000"><b>-6.7 &#176;C</b></font>
</td></tr>
</table><br>
<table bgcolor="#FFFFDD" align="center">
<caption><b><font color="#55AA55"><a name="R24">24 hours amount precipitation. 08/22/2021 at 00:00 UTC</a></font><br>
(10 of 5932 stations)</b></caption>
<tr bgcolor="#FFFFFF"><td>
1 </td>
<Td><a href="./gsynres?lang=en&ind=47168&ano=2021&mes=8&day=22&hora=0&min=0&ndays=30">Yosu (Korea, South)</a></td>
<td bgcolor="#0A000A" align="right"><font color="#FFFFFF"><b>677.0 mm</b></font>
</td></tr>
<tr bgcolor="#E0E0FF"><td>
2 </td>
<Td><a href="./gsynres?lang=en&ind=47108&ano=2021&mes=8&day=22&hora=0&min=0&ndays=30">Seoul (Korea, South)</a></td>
<td bgcolor="#0A000A" align="right"><font color="#FFFFFF"><b>620.0 mm</b></font>
</td></tr>
<table bgcolor="#FFFFDD" align="center">
<caption><b><font color="#55AA55"><a name="Gust">Maximum wind Gust in 24 hours. 08/22/2021 at 00:00 UTC</a></font><br>
(10 of 2804 stations)</b></caption>
<tr bgcolor="#FFFFFF"><td><td bgcolor="#640000" align="right"><font color="#FFFFFF"><b>
1 </td>
<Td><a href="./gsynres?lang=en&ind=60135&ano=2021&mes=8&day=22&hora=0&min=0&ndays=30">Rabat-Sale (Morocco)</a></td>
<td bgcolor="#640000" align="right"><font color="#FFFFFF"><b>183 km/h</b></font>
</td></tr>
<tr bgcolor="#E0E0FF"><td>
2 </td>
<Td><a href="./gsynres?lang=en&ind=68906&ano=2021&mes=8&day=22&hora=0&min=0&ndays=30">Gough Island (Saint Helena, Ascension and Tristan da Cunha)</a></td>
<td bgcolor="#640000" align="right"><font color="#FFFFFF"><b>133 km/h</b></font>
</td></tr>
"""

class TestResults(unittest.TestCase):
  def test_get_results_max(self):
    """
    Test that we can parse the results for maximum temps
    """
    results1 = Results(resultsHtml)
    resultsList = results1.getMaximums()

    self.assertEqual(len(resultsList), 2)
    self.assertEqual(resultsList[0][0], "Cordoba / Aeropuerto (Spain)")
    self.assertEqual(resultsList[0][1], "39.1 °C")
    self.assertEqual(resultsList[1][0], "Moron De La Frontera (Spain)")
    self.assertEqual(resultsList[1][1], "38.5 °C")

  def test_get_results_min(self):
    """
    Test that we can parse the resulprecipts for minimum temps
    """
    results1 = Results(resultsHtml)
    resultsList = results1.getMinimums()

    self.assertEqual(len(resultsList), 2)
    self.assertEqual(resultsList[0][0], "Nestares (Spain)")
    self.assertEqual(resultsList[0][1], "-6.8 °C")
    self.assertEqual(resultsList[1][0], "Polientes-Casyc (Spain)")
    self.assertEqual(resultsList[1][1], "-6.7 °C")

  def test_get_results_precip(self):
    """
    Test that we can parse the results for max precipitation
    """
    results1 = Results(resultsHtml)
    resultsList = results1.getMaxPrecip()

    self.assertEqual(len(resultsList), 2)
    self.assertEqual(resultsList[0][0], "Yosu (Korea, South)")
    self.assertEqual(resultsList[0][1], "677.0 mm")
    self.assertEqual(resultsList[1][0], "Seoul (Korea, South)")
    self.assertEqual(resultsList[1][1], "620.0 mm")

  def test_get_results_wind(self):
    results1 = Results(resultsHtml)
    resultsList = results1.getMaxWind()

    self.assertEqual(len(resultsList), 2)
    self.assertEqual(resultsList[0][0], "Rabat-Sale (Morocco)")
    self.assertEqual(resultsList[0][1], "183 km/h")
    self.assertEqual(resultsList[1][0], "Gough Island (Saint Helena, Ascension and Tristan da Cunha)")
    self.assertEqual(resultsList[1][1], "133 km/h")

  def test_get_results_all(self):
    results1 = Results(resultsHtml)
    resultsList = results1.getAll()

    self.assertEqual(len(resultsList), 2)
    extremesDict = resultsList[1]
    self.assertEqual(len(extremesDict), 4)
    self.assertIn("Maximum Temperature", extremesDict)
    self.assertIn("Minimum Temperature", extremesDict)
    self.assertIn("Maximum Precipitation", extremesDict)
    self.assertIn("Maximum Wind Gust", extremesDict)
    self.assertEqual(extremesDict["Maximum Temperature"][0], ('Cordoba / Aeropuerto (Spain)', '39.1 °C'))

  def test_get_title(self):
    results1 = Results(resultsHtml)
    title = results1.getTitle()
    
    self.assertEqual(title[0], "Ranking of selected weather parameters for Europe")
    self.assertEqual(title[1], "08/23/2021 at 06:00 UTC")

if __name__ == '__main__':
  unittest.main()
