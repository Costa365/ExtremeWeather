import unittest

from regions import Regions

regionsHtml = """
<TD>
   <select name="state">
    <OPTION value="World" Selected>World</OPTION>
    <OPTION value="North" >Northern Hemisphere</OPTION>
    <OPTION value="South" >Southern Hemisphere</OPTION>
    <optgroup label="Continent">
    <option value="Afr">Africa</option>
    <option value="Ames">America (South)</option>
    <option value="Amen">America (North and Central)</option>
    <option value="Anta">Antarctica</option>
    <option value="Asi">Asia</option>
    <option value="Eur">Europe</option>
    <option value="Pacs">Australia and Pacific</option>
    </optgroup>
    <optgroup label="State">
      <!-- Esto sirve para poner como activo una opcion adecuada teniendo en cuenta lo obtenido por geoip -->
<OPTION value='Afg' >Afghanistan</option>
"""

class TestRegions(unittest.TestCase):
    def test_get_regions(self):
        """
        Test that we can parse the regions
        """
        regions1 = Regions(regionsHtml)
        regionsList = regions1.getRegions()

        self.assertEqual(len(regionsList), 10)

    def test_get_regions_names(self):
        """
        Test that we can parse the region names
        """
        regions1 = Regions(regionsHtml)
        regionsList = regions1.getRegions()

        self.assertEqual(regionsList[0][0], "World")
        self.assertEqual(regionsList[0][1], "World")
        self.assertEqual(regionsList[1][0], "North")
        self.assertEqual(regionsList[1][1], "Northern Hemisphere")
        self.assertEqual(regionsList[9][0], "Pacs")
        self.assertEqual(regionsList[9][1], "Australia and Pacific")

if __name__ == '__main__':
    unittest.main()
