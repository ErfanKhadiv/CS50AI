# Minesweeper

An AI that plays Minesweeper using **logical inference**, with no hard-coded strategy.

The AI keeps a knowledge base of `Sentence`s of the form "exactly `count` of these cells are mines". After each move it:

1. Marks the revealed cell as safe and adds a new sentence from the number it shows.
2. Marks any cell that a sentence proves safe or mined, and propagates that to every other sentence.
3. Infers new sentences from subset relations between existing ones (`set2 - set1 = count2 - count1`).

`make_safe_move` picks a cell proven safe and `make_random_move` is the fallback when no safe move can be proven.

## Run

```
pip install -r requirements.txt
python runner.py
```

The `Minesweeper` game class, `runner.py` (the pygame interface) and the assets are provided by the course. The `Sentence` and `MinesweeperAI` classes in `minesweeper.py` are mine.
