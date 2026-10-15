# CS50's Introduction to Artificial Intelligence with Python

Selected implementations from **CS50's Introduction to Artificial Intelligence with Python**, Harvard University's introductory course covering fundamental concepts and algorithms in Artificial Intelligence.

This repository contains hands-on implementations covering **constraint satisfaction, reinforcement learning, machine learning, neural networks, and natural language processing**. Each project has its own README with a short explanation of the approach and how to run it.

## 🤖 Projects

| Project | Area | Implementation | Key techniques |
| ------- | ---- | -------------- | -------------- |
| [**Nim**](nim) | Reinforcement Learning | Q-learning agent that learns to play Nim through self-play | Bellman update, epsilon-greedy exploration |
| [**Shopping**](shopping) | Machine Learning | k-Nearest Neighbors classifier for predicting online shopping purchase intent | Sensitivity/specificity evaluation on imbalanced classes |
| [**Crossword**](crossword) | Constraint Satisfaction | Crossword generator using node consistency, arc consistency, and backtracking search | AC-3, minimum remaining values, least-constraining value |
| [**Parser**](parser) | Natural Language Processing | Context-free grammar parser for extracting noun phrase chunks | Hand-written CFG, NLTK chart parser, parse-tree traversal |
| [**Traffic**](traffic) | Neural Networks | Convolutional Neural Network for German traffic sign classification (GTSRB, 43 classes) | CNN design, dropout, optimizer comparison ([experiments](traffic/EXPERIMENTATION.md)) |

## 🧠 Concepts

Through these projects, I implemented and explored:

* Search algorithms
* Constraint Satisfaction Problems (CSP) and backtracking search
* Reinforcement Learning and Q-learning
* k-Nearest Neighbors
* Neural Networks and Convolutional Neural Networks
* Natural Language Processing and Context-Free Grammars
* Model training and evaluation

## 🛠️ Technologies

* Python
* NumPy
* scikit-learn
* TensorFlow / Keras
* NLTK

## ▶️ Running the projects

The `shopping` and `traffic` projects need datasets that are not included because of their size (the [UCI Online Shoppers Intention](https://archive.ics.uci.edu/dataset/468/online+shoppers+purchasing+intention+dataset) CSV and the [GTSRB](https://benchmark.ini.rub.de/gtsrb_news.html) images). The `parser` and `traffic` folders include a `requirements.txt`. See each project's README for exact commands.

## 📂 Repository Structure

```text
CS50AI/
├── crossword/
├── nim/
├── parser/
├── shopping/
├── traffic/
├── LICENSE
└── README.md
```

## 🎓 Academic Context

**Course:** CS50's Introduction to Artificial Intelligence with Python  
**Institution:** Harvard University  
**Platform:** Harvard OpenCourseWare / CS50
