# Parser — CFG Sentence Parser & Noun Phrase Extraction

Parses English sentences using a hand-written context-free grammar (CFG) and extracts noun phrase chunks.

## How it works
- A CFG (terminal + nonterminal rules) defines valid sentence structures
- `preprocess()` — tokenizes and lowercases a sentence, discarding words with no alphabetic characters
- NLTK's chart parser applies the grammar to build parse trees for the sentence
- `np_chunk()` — walks the parse tree to extract all noun phrase (NP) chunks that don't themselves contain a nested NP

## Run
```bash
pip install -r requirements.txt
python parser.py sentences/1.txt
# or interactively:
python parser.py
```
10 example sentences are in [`sentences/`](sentences).

## What it demonstrates
Formal grammar design (balancing coverage vs. ambiguity), parse tree traversal, and rule-based (pre-transformer) NLP — useful context for understanding what modern language models replaced.
