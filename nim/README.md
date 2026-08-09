# Nim — Reinforcement Learning

An AI that learns to play the game of Nim optimally through self-play, using Q-learning (no rules or strategy are hard-coded — it learns entirely from reward signals).

## How it works
- `nim.py` — the `Nim` game engine plus a `NimAI` agent that maintains a Q-value table over (state, action) pairs
- Training: the agent plays thousands of games against itself, updating Q-values via the Bellman equation (`update_q_value`), balancing exploration/exploitation with an epsilon-greedy policy (`choose_action`)
- `play.py` — lets a human play against the trained AI

## Run
```bash
python play.py
```
(This trains the AI for a set number of self-play games, then starts an interactive match — training parameters are set inside `nim.py`/`play.py`.)

## What it demonstrates
Q-learning fundamentals: state representation, the Bellman update rule, and the exploration/exploitation trade-off (epsilon-greedy).
