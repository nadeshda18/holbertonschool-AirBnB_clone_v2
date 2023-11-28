#!/usr/bin/env python3
"""
Test file for the console command with parameters.
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

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_command(self, mock_stdout):
        """Test the create command without parameters."""
        with patch('sys.stdin', StringIO("create BaseModel\nall\n")):
            self.console.cmdloop()
            output = mock_stdout.getvalue().strip()
            self.assertIn(str(self.obj_list[0]), output, "Failed in the create command test without parameters.")

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_command_with_params(self, mock_stdout):
        """Test the create command with parameters."""
        with patch('sys.stdin', StringIO("create State name=\"California\"\nall State\n")):
            self.console.cmdloop()
            output = mock_stdout.getvalue().strip()
            self.assertIn("California", output, "Failed in the create command test with parameters.")

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_command_with_complex_params(self, mock_stdout):
        """Test the create command with complex parameters."""
        with patch('sys.stdin', StringIO("create Place city_id=\"0001\" user_id=\"0001\" name=\"My_little_house\" number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300 latitude=37.773972 longitude=-122.431297\nall Place\n")):
            self.console.cmdloop()
            output = mock_stdout.getvalue().strip()
            self.assertIn("My little house", output, "Failed in the create command test with complex parameters.")
            self.assertIn("37.773972", output, "Failed in the create command test with complex parameters.")

    def test_quit_command(self):
        """Test the quit command."""
        with patch('sys.stdout', new_callable=StringIO):
            with self.assertRaises(SystemExit):
                self.console.onecmd("quit")

if __name__ == '__main__':
    unittest.main()
