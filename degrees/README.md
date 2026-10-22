# Degrees

Finds the shortest chain of movies connecting any two actors ("Six Degrees of Kevin Bacon") using **breadth-first search** over the IMDb actor/movie graph.

`shortest_path` runs BFS with a `QueueFrontier`, which guarantees the fewest movies between the two actors. It returns `None` when the actors are not connected.

## Run

```
python degrees.py small
Name: Tom Hanks
Name: Kevin Bacon
1 degrees of separation.
1: Tom Hanks and Kevin Bacon starred in Apollo 13
```

Only the `small/` dataset is included. To use the full dataset, download it from the [CS50AI Degrees project page](https://cs50.harvard.edu/ai/projects/0/degrees/), place it in a `large/` folder, and run `python degrees.py large`.

`util.py` (Node and frontier classes), `load_data` and the CLI are provided by the course. `shortest_path` is mine.
