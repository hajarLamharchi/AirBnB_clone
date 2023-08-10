"""Defines the class testState"""
import unittest
from models.state import State
from models.base_model import BaseModel


class testState(unittest.TestCase):
    """Defines the test cases for the class State"""
    def test_state_subclass(self):
        """checks if state is a subclass of BaseModel"""
        self.assertTrue(issubclass(State, BaseModel))

    def test_state_attribute(self):
        """checks if the class have all the attribute"""
        state = State()
        self.assertTrue(hasattr(state, 'name'))

    def test_state_attr_type(self):
        """checks if the type of the attribute is a string"""
        state = State()
        self.assertIsInstance(state.name, str)

    def test_state_attr_default_value(self):
        """Checks the default value of the attribute"""
        state = State()
        self.assertEqual(state.name, "")


if __name__ == "__main__":
    unittest.main()
