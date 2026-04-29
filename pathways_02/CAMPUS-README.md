# Accessible Rooms

Imagine that we want to implement a new functionality in our escape room game. Instead of printing all the pathways of a given location, as implemented in Project Part 3, we want to print **only the pathways to rooms that are accessible** (i.e., rooms that do not require a key to enter). This functionality could help guide the player to the rooms they can immediately access, without showing locked or inaccessible rooms.

You are provided with the `rooms` dictionary from Project Part 3, which defines the layout of a building, with information about:
- Pathways to other rooms.
- Whether a key is required to access the room.

The goal is to modify the function `get_directions()` to:
1. Check which rooms are directly accessible from the current room (a.k.a rooms that don't require a key).
2. Return a list of pathways leading to rooms to those rooms that are directly accessible.

## Inputs
The program uses the `rooms` dictionary to determine the accessible pathways.

## Expected Output
When you run your program with the starting room as `Bedroom`, the console should display the following:

```python
You can go: ['s']
```
Notice that the pathway `d`, which represents the `Bathroom` is not listed since `Bathroom` only `open_with` `Key 1`.

For a different starting room, for example, `Hallway`, the output should be:
```python
You can go: ['w', 'a']
```

since the pathways `Bedroom` and `Kitchen` are accessible without keys (`open_with` value is `""`).

If the `current_room` is not in the `rooms` dictionary, the output should be:
```python
You can go: []
```

## Hints
- To test other rooms outcomes change the value of `START_LOCATION = "Bedroom"` to other rooms, ex: `START_LOCATION = "Hallway"`
- The `rooms` dictionary contains all the necessary information about room pathways and key requirements.
- Use the `pathways` key to find connected rooms and their directions.
- Use the `open_with` key to check if a room requires a key to enter.
- If a room does not require a key (i.e., `open_with` is an empty string), include the `direction` key in the list of accessible pathways.
- Use `append()` to add elements to a list.


## Rubrics

| Task                     | Points |
|--------------------------|--------|
| Retrieve current room pathways          | 2 |
| Iterate through connected rooms         | 4 |
| Filter only accessible rooms            | 2 |
| Add accessible room directions to a list| 1 |
| Return list of accessible rooms         | 1 |
| **Total**                               | **10** |

Scoring note: This rubric is on a 10-point scale and will be scaled to the exercise value of 6 points.
**The final grading will calculated based on both the tests and the rubric above*

## How to Test
To ensure that you got the exercise correctly, you can run local tests before you submit your code. If the code passes the test, you are good to submit. If not, you can check the test that failed and fix your code.
Follow these steps to test your code:
- Click on the becker glass icon on the left tab.
- Locate the `02-pathways` test. You might need to expand the `final-exam` to find it.
- Click on the play arrow to run the test.
- If it is green, the test passed and you should be good to submit this exercise.
- If it is red, you possibly made a mistake. Check the error in the test "Test Results" tab on the view at the bottom of the screen (same location as the Terminal view)

## How to Submit

- Use the VS code Source Control Tab to submit your assignment:
    - Click on the `+` sign next to the files you want to include, in this case `pathways.py`
    - Write a commit message, e.g., "Finished with pathways."
    - Select "Commit and Push".
- Alternativally, you can use git to add, commit, and push your changes:
    ```bash
    git add tempify.py
    git commit -m "Finished with pathways."
    git push
    ```
