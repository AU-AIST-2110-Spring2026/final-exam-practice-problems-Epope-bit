# Accessible Train Routes

In this exercise, you will implement a function for a train route system. Some stations are open to everyone, while others require a special pass or badge.

You are provided with the `stations` dictionary, which stores:

- Routes to connected stations.
- Whether a station requires a pass to enter.

## Task Description

The goal is to modify `get_routes()` to:

1. Check which stations are directly connected to the current station.
2. Determine whether each connected station requires a pass.
3. Return a list of directions that lead only to stations that do not require a pass.

## Expected Output

When the starting station is `Main Station`, the program should display:

```python
You can go: ['n']
```

The route `e` is not included because `Airport Stop` requires an `Airport Badge`.

For `Museum Stop`, the function should return:

```python
['s', 'e']
```

because both `Main Station` and `University Stop` are accessible.

If the station does not exist, the function should return:

```python
[]
```

## Hints

* Use the `routes` key to find connected stations.
* Use the `open_with` key to check whether a station requires a pass.
* If `open_with` is an empty string `""`, the station is accessible.
* Add only the direction, such as `"n"` or `"e"`, to the list.
* Use `append()` to add directions to the list.

## Rubric

| Task                               | Points |
| ---------------------------------- | ------ |
| Retrieve current station routes    | 2      |
| Iterate through connected stations | 4      |
| Filter only accessible stations    | 2      |
| Add accessible directions to list  | 1      |
| Return list of accessible routes   | 1      |
| **Total**                          | **10** |
