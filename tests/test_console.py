#!/usr/bin/env python3
"""
Test file for the HBNBCommand console.
"""

import subprocess
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models.base_model import BaseModel
from models.state import State
from models.place import Place

class TestConsole(unittest.TestCase):
    """Test cases for the HBNBCommand console."""

    @classmethod
    def setUpClass(cls):
        """Setup for the test cases."""
        cls.console = HBNBCommand()
        cls.obj_list = [
            BaseModel(),
            State(name="California"),
            Place(city_id="0001", user_id="0001", name="My_little_house", number_rooms=4, number_bathrooms=2, max_guest=10, price_by_night=300, latitude=37.773972, longitude=-122.431297)
        ]

    def setUp(self):
        """Clear storage before each test."""
        HBNBCommand.classes = {}  # Clear the storage
        HBNBCommand().precmd("create BaseModel")
        HBNBCommand().precmd("create State name=\"California\"")
        HBNBCommand().precmd("create Place city_id=\"0001\" user_id=\"0001\" name=\"My_little_house\" number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300 latitude=37.773972 longitude=-122.431297")

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_command(self, mock_stdout):
        """Test the create command without parameters."""
        with patch('sys.stdin', StringIO("create BaseModel\nall\n")):
            self.console.cmdloop()
            output = mock_stdout.getvalue().strip()
            self.assertIn(str(self.obj_list[0]), output, "Failed in the create command test without parameters.")

    # ... Other test methods ...

    def test_params_create(self):
        """Test the params_create command."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            with patch('sys.stdin', StringIO("create BaseModel\ncreate State name=\"California\"\ncreate State name=\"Arizona\"\ncreate Place city_id=\"0001\" user_id=\"0001\" name=\"My_little_house\" number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300 latitude=37.773972 longitude=-122.431297\nall\n")):
                self.console.cmdloop()
                output = mock_stdout.getvalue().strip()
                self.assertTrue(output.count("California") == 1, "Failed in the params_create command test for State California.")
                self.assertTrue(output.count("Arizona") == 1, "Failed in the params_create command test for State Arizona.")
                self.assertTrue(output.count("My little house") == 1, "Failed in the params_create command test for Place My little house.")
                self.assertTrue(output.count("37.773972") == 1, "Failed in the params_create command test for Place 37.773972.")

if __name__ == '__main__':
    unittest.main()
