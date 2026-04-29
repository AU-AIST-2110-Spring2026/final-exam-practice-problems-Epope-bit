import unittest


from stations_04.stations import get_routes


class TestGetRoutes(unittest.TestCase):

    def test_accessible_routes_from_main_station(self):
        """Test accessible routes from Main Station."""

        current_station = "Main Station"
        expected_routes = ["n"]
        self.assertEqual(get_routes(current_station), expected_routes)

    def test_accessible_routes_from_museum_stop(self):
        """Test accessible routes from Museum Stop."""

        current_station = "Museum Stop"
        expected_routes = ["s", "e"]
        self.assertEqual(get_routes(current_station), expected_routes)

    def test_accessible_routes_from_university_stop(self):
        """University Stop should only list stations that do not require a pass."""

        current_station = "University Stop"
        expected_routes = ["w"]
        self.assertEqual(get_routes(current_station), expected_routes)

    def test_invalid_station(self):
        """Test with a station name that does not exist."""

        current_station = "Bus Depot"
        expected_routes = []
        self.assertEqual(get_routes(current_station), expected_routes)