# Tic-Tac-Toe

An AI that plays Tic-Tac-Toe optimally using **minimax with alpha-beta pruning**.

- `player`, `actions`, `result`, `winner`, `terminal`, `utility`: the game model
- `minimax`: X maximizes the score and O minimizes it. Alpha-beta pruning skips branches that cannot change the result, and ties between equally good moves are broken at random so games vary. The AI reports how many actions it explored each move.

The AI cannot be beaten: the best a human opponent can get is a draw.

## Run

```
pip install -r requirements.txt
python runner.py
```

`runner.py` (the pygame interface) and the font are provided by the course. All the logic in `tictactoe.py` is mine.
