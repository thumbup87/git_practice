#import unittest

from city import city_country

#class CityCountryTest(unittest.TestCase):
    #unittest.TestCase is module_name.class_name
    #def test_city_country(self):
    #    city_country_name = city_country('santiago', 'chile')
    #    self.assertEqual(city_country_name, 'Santiage, Chile')

#if __name__ == '__main__':
    #unittest.main()

v1 = city_country('santiago', 'chile')
print(v1)
