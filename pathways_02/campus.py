campus = {
    "Library": {"pathways": {"n": "Science Hall", "e": "Student Center"}, "open_with": ""},
    "Science Hall": {"pathways": {"s": "Library", "e": "Research Lab"}, "open_with": ""},
    "Student Center": {"pathways": {"w": "Library", "n": "Gym"}, "open_with": ""},
    "Research Lab": {"pathways": {"w": "Science Hall"}, "open_with": "Lab Pass"},
    "Gym": {"pathways": {"s": "Student Center"}, "open_with": "Gym Card"},
}

START_LOCATION = "Library"


def get_directions(location: str) -> list[str]:
    """Return directions to connected buildings that do not require a pass."""
    # Modify this function to iterate through all buildings connected
    # to the variable location.
    #
    # If the connected building requires a pass to access,
    #     do not add that direction to the list.
    #
    # If the connected building does not require a pass,
    #     add the connected building's direction to a list.
    #
    # Return the list of accessible directions.
    #
    # Example:
    # If location is "Library", this function should return ["n", "e"].




def main():
    '''DO NOT MODIFY THIS FUNCTION'''

    current_building = START_LOCATION
    accessible_directions = get_directions(current_building)

    print("You can go:", accessible_directions)


if __name__ == "__main__":
    main()