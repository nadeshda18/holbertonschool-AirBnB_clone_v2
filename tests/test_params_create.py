# test_params_create

def create_state_commands():
    # Define commands to create State objects
    return [
        'create State name="California"',  # Create a State object with the name "California"
        'create State name="Arizona"',      # Create another State object with the name "Arizona"
        'all State'                          # Display all State objects
    ]

def create_place_commands():
    # Define commands to create Place objects
    return [
        'create Place city_id="0001" user_id="0001" name="My_little_house" number_rooms=4 number_bathrooms=2 max_guest=10 price_by_night=300 latitude=37.773972 longitude=-122.431297',  # Create a Place object with specified parameters
        'all Place'                          # Display all Place objects
    ]

if __name__ == "__main__":
    # Generate commands for State and Place objects
    state_commands = create_state_commands()
    place_commands = create_place_commands()

    # Open the file for writing
    with open('test_params_create | ./console.py', 'w') as file:
        # Write State commands to the file
        for command in state_commands:
            file.write(command + '\n')

        # Write Place commands to the file
        for command in place_commands:
            file.write(command + '\n')
