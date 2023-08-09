"""Defines the class testBaseModel"""
import unittest
from models.base_model import BaseModel
import datetime


class testBaseModel(unittest.TestCase):
    """Defines test cases for the class BaseModel"""
    def test_base_id_not_none(self):
        """tests if id is null"""
        bm = BaseModel()
        self.assertNotEqual(bm.id, None)

    def test_base_same_id(self):
        """tests if 2 ids are same"""
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_base_id_is_string(self):
        """tests if the id is a string"""
        bm = BaseModel()
        self.assertIsInstance(bm.id, str)

    def test_base_created_at(self):
        """checks if created_at in not none"""
        bm = BaseModel()
        self.assertIsNotNone(bm.created_at)

    def test_base_created_at_datetime(self):
        """checks if created_at is a datetime"""
        bm = BaseModel()
        self.assertIsInstance(bm.created_at, datetime.datetime)

    def test_base_updated_at(self):
        """checks if updated_at in not none"""
        bm = BaseModel()
        self.assertIsNotNone(bm.updated_at)

    def test_base_updated_at_datetime(self):
        """checks if updated_at is a datetime"""
        bm = BaseModel()
        self.assertIsInstance(bm.updated_at, datetime.datetime)

    def test_base_created_at_greater(self):
        """checks if created_at of an object created after another is greater"""
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertGreater(bm2.created_at, bm1.created_at)

    def test_base_save(self):
        """checks if updated_at changes after calling save()"""
        bm = BaseModel()
        bm.save()
        self.assertNotEqual(bm.created_at, bm.updated_at)


class TestBaseModelDict(unittest.TestCase):
    """Defines Tests cases for for the dict representation"""
    def test_base_to_dict(self):
        """checks if to_dict return a dictionary"""
        bm = BaseModel()
        self.assertIsInstance(bm.to_dict(), dict)

    def test_base_to_dict_key(self):
        """checks if an attribute is in dict"""
        bm = BaseModel()
        bm.name = "Walter"
        bm.age = 52
        my_dict = bm.to_dict()
        self.assertIsNotNone(my_dict.get('name'))
        self.assertIsNotNone(my_dict.get('age'))
        new_bm = BaseModel(**my_dict)
        self.assertEqual(bm.id, new_bm.id)
        self.assertIsInstance(new_bm, BaseModel)


if __name__ == "__main__":
    unittest.main()
