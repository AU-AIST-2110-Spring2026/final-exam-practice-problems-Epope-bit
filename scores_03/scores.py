# List of exam scores
scores = [45, 72, 88, 91, 67, 84, 100, 59, 76, 82, 95, 60, 73, 89, 90,
          55, 64, 78, 85, 92, 48, 69, 80, 87, 93, 58, 62, 74, 81, 99]


def filter_scores(scores: list[int]) -> list[int]:
    """Function to filter and sort exam scores."""

    # List where you should store the filtered scores
    filtered_scores = []

    # Step 1: Filter scores
    # Scores should be greater than or equal to 70
    # Scores should be less than or equal to 90
    # Scores should be even numbers

    # Step 2: Sort scores from highest to lowest
    # Use the sort function with the reverse parameter

    # Step 3: Return the filtered and sorted list


def main():
    """DO NOT MODIFY THIS FUNCTION"""
    print(filter_scores(scores))


if __name__ == "__main__":
    main()