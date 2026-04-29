# Filtering Grocery Prices

In this exercise, you will implement a function to filter and sort a list of grocery item prices.

## Task Description

Given a list of grocery prices, the goal is to:

1. Filter prices that are within the range of **$5.00 to $25.00 inclusive**.
2. Only keep prices that are **whole-dollar amounts**, such as `8.00`, `10.00`, or `24.00`.
3. Sort the filtered prices in **ascending order**.
4. Return the sorted list of prices.

## Inputs

The input to the program is a predefined list of grocery prices.

## Expected Output

When you run your program, the console should display the filtered and sorted list of prices. For the given input, the expected output is exactly:

```python
[8.0, 10.0, 14.0, 16.0, 20.0, 24.0]
```

## Hints

* Use a `for` loop to iterate through the list of prices.
* Use an `if` statement to check each price.
* The price should be greater than or equal to `$5.00`.
* The price should be less than or equal to `$25.00`.
* The price should be a whole-dollar amount.
* Use `append()` to add matching prices to a list.
* Use the `sort()` method to sort the filtered list in ascending order.
* A float is a whole-dollar amount if `price % 1 == 0`.

## Rubric

| Task                       | Points |
| -------------------------- | ------ |
| Filter by price range      | 3      |
| Filter whole-dollar prices | 2      |
| Append results to a list   | 2      |
| Sort the filtered list     | 2      |
| Return the filtered list   | 1      |
| **Total**                  | **10** |

Scoring note: This rubric is on a 10-point scale and will be scaled to the exercise value of 4 points.

**The final grading will be calculated based on both the tests and the rubric above.**

## How to Test

To ensure that you completed the exercise correctly, you can run local tests before you submit your code.

Follow these steps to test your code:

* Click on the beaker glass icon on the left tab.
* Locate the `prices_01` test.
* Click on the play arrow to run the test.
* If it is green, the test passed and you should be good to submit this exercise.
* If it is red, check the error in the "Test Results" tab at the bottom of the screen.

## How to Submit

Use the VS Code Source Control tab to submit your assignment:

* Click on the `+` sign next to the files you want to include, in this case `prices.py`.
* Write a commit message, such as `"Finished with prices."`
* Select "Commit and Push".

Alternatively, you can use git:

```bash
git add prices.py
git commit -m "Finished with prices."
git push
```
