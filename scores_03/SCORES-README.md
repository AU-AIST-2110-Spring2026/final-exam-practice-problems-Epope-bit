# Filtering Exam Scores

In this exercise, you will implement a function to filter and sort a list of exam scores.

## Task Description

Given a list of exam scores, the goal is to:

1. Filter scores that are **even numbers**.
2. Only keep scores from **70 to 90 inclusive**.
3. Sort the filtered scores in **descending order**.
4. Return the sorted list of scores.

## Expected Output

```python
[90, 88, 84, 82, 80, 78, 76, 74, 72]
```

## Hints

* Use a `for` loop to iterate through the list.
* Use an `if` statement to check each score.
* Use `%` to check if a score is even.
* Use `append()` to add matching scores to a list.
* Use `sort(reverse=True)` to sort from highest to lowest.

## Rubric

| Task                     | Points |
| ------------------------ | ------ |
| Filter by score range    | 3      |
| Filter even scores       | 2      |
| Append results to a list | 2      |
| Perform reversed sorting | 2      |
| Return the filtered list | 1      |
| **Total**                | **10** |
