# Crossword — Constraint Satisfaction Solver

Generates a valid crossword puzzle by treating it as a Constraint Satisfaction Problem: each blank is a variable, its possible words are its domain, and overlapping cells are constraints between variables.

## How it works
- `crossword.py` — provided data structures: `Variable` (a slot with its position/length/direction) and `Crossword` (parses a structure file into the grid + finds overlaps between variables)
- `generate.py` — the solver:
  - `enforce_node_consistency` — removes words that don't match a variable's length
  - `ac3` / `revise` — enforces arc consistency (removes values that can't satisfy an overlap constraint)
  - `backtrack` — backtracking search with `select_unassigned_variable` (minimum remaining values heuristic) and `order_domain_values` (least-constraining-value heuristic) to prune the search space

## Run
```bash
python generate.py data/structure1.txt data/words1.txt [output.png]
```
Structure/word files for 3 difficulty levels are in [`data/`](data).

## What it demonstrates
CSP formulation, arc consistency (AC-3), and backtracking search with heuristics — the same search family used in scheduling and resource-allocation problems.
