import unittest

from prices_01.prices import filter_prices, prices


class TestFilterPrices(unittest.TestCase):

    def test_regular_case(self):
        """Test filtering and sorting with the given prices."""

        expected_result = [8.00, 10.00, 14.00, 16.00, 20.00, 24.00]
        self.assertEqual(
            filter_prices(prices),
            expected_result,
            f"Expected {expected_result}, but got {filter_prices(prices)}"
        )

    def test_no_matching_prices(self):
        """Return empty list when no prices meet the criteria."""

        custom_prices = [1.25, 2.50, 3.99, 26.00, 30.50]
        self.assertEqual(
            filter_prices(custom_prices),
            [],
            f"Expected an empty list, but got {filter_prices(custom_prices)}"
        )