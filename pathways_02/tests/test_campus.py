import unittest

from pathways_02.campus import get_directions


class TestGetDirections(unittest.TestCase):

    def test_accessible_directions_from_library(self):
        """Test accessible directions from the Library."""

        current_building = "Library"
        expected_directions = ["n", "e"]
        self.assertEqual(
            get_directions(current_building),
            expected_directions,
            f"Expected '{expected_directions}', but got '{get_directions(current_building)}'"
        )

    def test_accessible_directions_from_science_hall(self):
        """Science Hall should only list buildings that do not require a pass."""

        current_building = "Science Hall"
        expected_directions = ["s"]
        self.assertEqual(
            get_directions(current_building),
            expected_directions,
            f"Expected '{expected_directions}', but got '{get_directions(current_building)}'"
        )

    def test_accessible_directions_from_student_center(self):
        """Student Center should only list accessible connected buildings."""

        current_building = "Student Center"
        expected_directions = ["w"]
        self.assertEqual(
            get_directions(current_building),
            expected_directions,
            f"Expected '{expected_directions}', but got '{get_directions(current_building)}'"
        )

    def test_invalid_building(self):
        """Test with a building name that does not exist."""

        current_building = "Parking Deck"
        expected_directions = []
        self.assertEqual(
            get_directions(current_building),
            expected_directions,
            f"Expected '{expected_directions}', but got '{get_directions(current_building)}'"
        )