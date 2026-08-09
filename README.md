# CS50's Introduction to Artificial Intelligence with Python

Problem sets completed for [Harvard CS50AI](https://cs50.harvard.edu/ai/), covering search, constraint satisfaction, machine learning, neural networks, and NLP.

> These are official course problem sets, not original research — see [HBALS-TSP](https://github.com/ErfanKhadiv/HBALS-TSP) for that. Included here as evidence of hands-on coverage of core AI fundamentals.

| Project | Topic | What it does |
|---|---|---|
| [`nim/`](nim) | Reinforcement Learning | Q-learning agent that learns to play Nim through self-play |
| [`shopping/`](shopping) | Machine Learning | k-NN classifier predicting online shopping purchase intent |
| [`crossword/`](crossword) | Constraint Satisfaction | Crossword generator using node/arc consistency + backtracking search |
| [`parser/`](parser) | Natural Language Processing | Context-free grammar parser extracting noun phrase chunks from sentences |
| [`traffic/`](traffic) | Neural Networks | CNN classifying German traffic sign images (GTSRB dataset) |

## Running

Each project is self-contained. Install dependencies per-project where a `requirements.txt` is present:

```bash
cd <project-folder>
pip install -r requirements.txt   # if present
python <script>.py [args]
```

See each project's own README for exact run instructions and arguments.

## License

MIT — see [LICENSE](LICENSE). Note: `crossword.py` (the `Crossword`/`Variable` data structures) and the CSV/data loading scaffolding in a few files were provided as CS50 starter code; the solving/learning logic (`generate.py`'s CSP solver, `nim.py`'s Q-learning, `shopping.py`'s model training, `parser.py`'s grammar and chunking, `traffic.py`'s CNN architecture) is original coursework.
