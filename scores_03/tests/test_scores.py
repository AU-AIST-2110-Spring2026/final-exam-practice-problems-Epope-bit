import unittest

from scores_03.scores import filter_scores, scores


class TestFilterScores(unittest.TestCase):

    def test_regular_case(self):
        """Test filtering and sorting with the given scores."""

        expected_result = [90, 88, 84, 82, 80, 78, 76, 74, 72]
        self.assertEqual(filter_scores(scores), expected_result)

    def test_no_matching_scores(self):
        """Return empty list when no scores meet the criteria."""

        custom_scores = [45, 59, 67, 91, 95, 99]
        self.assertEqual(filter_scores(custom_scores), [])