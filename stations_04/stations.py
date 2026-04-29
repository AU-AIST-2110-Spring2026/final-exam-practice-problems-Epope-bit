stations = {
    "Main Station": {"routes": {"n": "Museum Stop", "e": "Airport Stop"}, "open_with": ""},
    "Museum Stop": {"routes": {"s": "Main Station", "e": "University Stop"}, "open_with": ""},
    "Airport Stop": {"routes": {"w": "Main Station", "n": "Control Tower"}, "open_with": "Airport Badge"},
    "University Stop": {"routes": {"w": "Museum Stop", "n": "Research Center"}, "open_with": ""},
    "Control Tower": {"routes": {"s": "Airport Stop"}, "open_with": "Security Badge"},
    "Research Center": {"routes": {"s": "University Stop"}, "open_with": "Research Pass"},
}

START_LOCATION = "Main Station"


def get_routes(location:str) -> list[str]:
    """Return routes to connected stations that do not require a pass."""
    # Modify this function to iterate through all stations connected
    # to the variable location.
    #
    # If the connected station requires a pass to access,
    #     do not add that direction to the list.
    #
    # If the connected station does not require a pass,
    #     add the connected station's direction to a list.
    #
    # Return the list of accessible route directions.




def main():
    """DO NOT MODIFY THIS FUNCTION"""

    current_station = START_LOCATION
    accessible_routes = get_routes(current_station)

    print("You can go:", accessible_routes)


if __name__ == "__main__":
    main()