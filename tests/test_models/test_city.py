"""Defines the class testCity"""
import unittest
from models.base_model import BaseModel
from models.city import City


class testCity(unittest.TestCase):
    """Defines the test cases for the class City"""
    def test_city_subclass(self):
        """checks if city inherits from BaseModel"""
        self.assertTrue(issubclass(City, BaseModel))

    def test_city_attributes(self):
        """checks if attributes exist"""
        city = City()
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertTrue(hasattr(city, 'name'))

    def test_city_attr_type(self):
        """checks the type of the attributes"""
        city = City()
        self.assertIsInstance(city.state_id, str)
        self.assertIsInstance(city.name, str)

    def test_city_attr_default_value(self):
        """checks the default value of the attributes"""
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")


if __name__ == "__main__":
    unittest.main()
