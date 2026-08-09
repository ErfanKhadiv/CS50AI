# Shopping — Purchase Intent Classifier

Predicts whether an online shopping session will end in a purchase, using a k-Nearest Neighbors classifier.

## How it works
- `load_data()` — parses session data (page visits, durations, bounce/exit rates, visitor type, etc.) into feature vectors and purchase/no-purchase labels
- `train_model()` — trains a k-NN classifier (`k=1`, scikit-learn)
- `evaluate()` — reports **sensitivity** (true positive rate — correctly caught purchases) and **specificity** (true negative rate — correctly caught non-purchases) rather than plain accuracy, since the classes are imbalanced

## Run
```bash
python shopping.py shopping.csv
```
(Expects a `shopping.csv` file with the standard [UCI Online Shoppers Intention](https://archive.ics.uci.edu/dataset/468/online+shoppers+purchasing+intention+dataset) columns — not included here; download separately if reproducing.)

## What it demonstrates
Feature engineering from mixed categorical/numeric data, train/test evaluation, and why accuracy alone is misleading on imbalanced classification problems.
