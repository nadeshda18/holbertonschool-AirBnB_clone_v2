#!/usr/bin/env python3
import subprocess
import unittest

def test_params_create():
    # Define commands to create State and Place objects
    state_commands = [
        'create State name="California"',
        'create State name="Arizona"',
        'all State'
    ]

    place_commands = [
        'create Place city_id="0001" user_id="0001" name="My_little_house" number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300 latitude=37.773972 longitude=-122.431297',
        'all Place'
    ]

    # Concatenate all commands
    all_commands = '\n'.join(state_commands + place_commands)

    # Run the commands using subprocess
    result = subprocess.run(['echo', all_commands, '|', './console.py'], text=True, capture_output=True)

    # Check if the output contains the expected results
    assert "California" in result.stdout
    assert "Arizona" in result.stdout
    assert "My little house" in result.stdout
    assert "number_rooms: 4" in result.stdout
    assert "number_bathrooms: 2" in result.stdout
    assert "max_guest: 10" in result.stdout
    assert "price_by_night: 300" in result.stdout
    assert "latitude: 37.773972" in result.stdout
    assert "longitude: -122.431297" in result.stdout

if __name__ == "__main__":
    test_params_create()