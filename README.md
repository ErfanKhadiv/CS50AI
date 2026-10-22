# CS50's Introduction to Artificial Intelligence with Python

Problem sets completed for [Harvard CS50AI](https://cs50.harvard.edu/ai/), covering search, knowledge, uncertainty, optimization, machine learning, neural networks, and language.
> These are official course problem sets, not original research — see [HBALS-TSP](https://github.com/ErfanKhadiv/HBALS-TSP) for that. Included here as evidence of hands-on coverage of core AI fundamentals.

| Project                                                                   | Topic                          | What it does                                                                        |
| ------------------------------------------------------------------------- | ------------------------------ | ----------------------------------------------------------------------------------- |
| [`degrees/`](https://github.com/ErfanKhadiv/CS50AI/blob/main/degrees)           | Search                         | BFS over the IMDb actor/movie graph to find the shortest path between two actors    |
| [`tictactoe/`](https://github.com/ErfanKhadiv/CS50AI/blob/main/tictactoe)       | Adversarial Search             | Unbeatable Tic-Tac-Toe AI using minimax with alpha-beta pruning                     |
| [`minesweeper/`](https://github.com/ErfanKhadiv/CS50AI/blob/main/minesweeper)   | Knowledge / Logical Inference  | Minesweeper AI that infers safe cells and mines from logical sentences              |
| [`pagerank/`](https://github.com/ErfanKhadiv/CS50AI/blob/main/pagerank)         | Uncertainty / Markov Chains    | PageRank via random-surfer sampling and iterative convergence                       |
| [`heredity/`](https://github.com/ErfanKhadiv/CS50AI/blob/main/heredity)         | Uncertainty / Bayesian Networks| Inference by enumeration of gene and trait probabilities across a family tree       |
| [`nim/`](https://github.com/ErfanKhadiv/CS50AI/blob/main/nim)                   | Reinforcement Learning         | Q-learning agent that learns to play Nim through self-play                          |
| [`shopping/`](https://github.com/ErfanKhadiv/CS50AI/blob/main/shopping)         | Machine Learning               | k-NN classifier predicting online shopping purchase intent                          |
| [`crossword/`](https://github.com/ErfanKhadiv/CS50AI/blob/main/crossword)       | Constraint Satisfaction        | Crossword generator using node/arc consistency + backtracking search               |
| [`traffic/`](https://github.com/ErfanKhadiv/CS50AI/blob/main/traffic)           | Neural Networks                | CNN classifying German traffic sign images (GTSRB dataset)                          |
| [`parser/`](https://github.com/ErfanKhadiv/CS50AI/blob/main/parser)             | Natural Language Processing    | Context-free grammar parser extracting noun phrase chunks from sentences            |
| [`attention/`](https://github.com/ErfanKhadiv/CS50AI/blob/main/attention)       | Transformers                   | Visualizes BERT's self-attention heads on masked sentences, with written analysis   |

## Running

Each project is self-contained. Install dependencies per-project where a `requirements.txt` is present:

```
cd <project-folder>
pip install -r requirements.txt   # if present
python <script>.py [args]
```

See each project's own README for exact run instructions and arguments.

## License

MIT — see [LICENSE](LICENSE). Note: the course provided starter code for each project, including `crossword.py` (the `Crossword`/`Variable` data structures), the `runner.py` interfaces (`tictactoe`, `minesweeper`), `util.py` and the data loading in `degrees`, the `Minesweeper` game class, the probability tables and scaffolding in `heredity`, `crawl` in `pagerank`, and `generate_diagram` in `attention`. The solving/learning logic is original coursework: `shortest_path` (`degrees`), the game model and `minimax` (`tictactoe`), `Sentence` and `MinesweeperAI` (`minesweeper`), `transition_model`/`sample_pagerank`/`iterate_pagerank` (`pagerank`), `joint_probability`/`update`/`normalize` (`heredity`), `generate.py`'s CSP solver, `nim.py`'s Q-learning, `shopping.py`'s model training, `parser.py`'s grammar and chunking, `traffic.py`'s CNN architecture, and the attention helper functions and analysis in `mask.py` / `analysis.md`.
