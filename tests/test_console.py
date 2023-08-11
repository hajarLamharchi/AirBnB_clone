"""Defines the class testConsole"""
import unittest
import sys
from models.base_model import BaseModel
from models import storage
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO


class testConsole(unittest.TestCase):
    """Defines test cases for the class HBNBCommand"""
    def test_HBNBComman_methods(self):
        """checks if all methods exist"""
        self.assertTrue(hasattr(HBNBCommand, "precmd"))
        self.assertTrue(hasattr(HBNBCommand, "do_EOF"))
        self.assertTrue(hasattr(HBNBCommand, "do_quit"))
        self.assertTrue(hasattr(HBNBCommand, "help_quit"))
        self.assertTrue(hasattr(HBNBCommand, "emptyline"))
        self.assertTrue(hasattr(HBNBCommand, "do_create"))
        self.assertTrue(hasattr(HBNBCommand, "do_show"))
        self.assertTrue(hasattr(HBNBCommand, "do_destroy"))
        self.assertTrue(hasattr(HBNBCommand, "do_update"))
        self.assertTrue(hasattr(HBNBCommand, "do_all"))
        self.assertTrue(hasattr(HBNBCommand, "do_count"))

    def test_HBNBCommand_001(self):
        """tests the console 0.0.1"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("EOF")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")

    def test_HBNBCommand_01(self):
        """tests the console 0.1"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show BaseModel 1234-1234-1234")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel 1234-1234-1234")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all BaseModel")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update BaseModel 1234-1234-1234 name 'Holberton'")

    def test_HBNBCommand_10(self):
        """tests the console 1.0"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show User")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy City")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update Amenity")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all State")

    def test_HBNBCommand_all(self):
        """tests the method all"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.all()")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.all()")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.all()")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.all()")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.all()")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.all()")

    def test_HBNBCommand_count(self):
        """tests the method count"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.count()")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.count()")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.count()")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.count()")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.count()")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.count()")

    def test_HBNBCommand_show(self):
        """tests the method show"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Place.show()")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("State.show()")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("City.show()")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Amenity.show()")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("Review.show()")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("User.show()")


if __name__ == "__main__":
    unittest.main()
