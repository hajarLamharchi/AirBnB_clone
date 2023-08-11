"""Defines the class TestFileStorage"""
import unittest
from models import storage
from models.base_model import BaseModel
from models import FileStorage
import os


class testFileStorage(unittest.TestCase):
    """Defines the test cases for the class FileStorage"""
    def test_FileStorage_methods(self):
        """checks if methods exist"""
        self.assertTrue(hasattr(storage, "__init__"))
        self.assertTrue(hasattr(storage, "all"))
        self.assertTrue(hasattr(storage, "new"))
        self.assertTrue(hasattr(storage, "save"))
        self.assertTrue(hasattr(storage, "reload"))

    def test_Filestorage_attributes(self):
        """checks attributes type and existance"""
        self.assertTrue(hasattr(FileStorage, "_FileStorage__file_path"))
        self.assertTrue(hasattr(FileStorage, "_FileStorage__objects"))
        self.assertIsInstance(storage._FileStorage__file_path, str)
        self.assertIsInstance(storage._FileStorage__objects, dict)

    def test_FileStorage_new(self):
        """tests the new method"""
        bm1 = BaseModel()
        bm2 = BaseModel()
        id1 = bm1.id
        id2 = bm2.id
        self.assertFalse(id1 == id2)

    def test_FileStorage_all(self):
        """tests the method all"""
        dict1 = storage.all()
        dict2 = FileStorage._FileStorage__objects
        self.assertDictEqual(dict1, dict2)

    def test_FileStorage_save(self):
        """tests the method save"""
        bm = BaseModel()
        bm.save()
        self.assertTrue(os.path.exists("file.json"))


if __name__ == "__main__":
    unittest.main()
