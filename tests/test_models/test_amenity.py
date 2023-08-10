"""Defines the class testAmenity"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class testAmenity(unittest.TestCase):
    """Defines the test cases for the class Amenity"""
    def test_amenity_subclass(self):
        """checks if Amenity is a subclass of BaseModel"""
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_amenity_attribute(self):
        """checks if the attributes exist"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'name'))

    def test_amenity_attr_type(self):
        """checks if the type of the attribute is a string"""
        amenity = Amenity()
        self.assertIsInstance(amenity.name, str)

    def test_amenity_attr_default_value(self):
        """checks the default value of the attribute"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")


if __name__ == "__main__":
    unittest.main()
