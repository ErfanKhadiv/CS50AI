# Knights

Solves Knights and Knaves logic puzzles with **propositional logic** and **model checking**.

On an island, every inhabitant is either a knight, who always tells the truth, or a knave, who always lies. Given what each character says, the program works out who is who.

## How it works

Each puzzle is encoded as a knowledge base of propositional sentences in `puzzle.py`, using symbols such as `A is a Knight` and `A is a Knave`.

- **General knowledge:** every character is a knight or a knave, and never both.
- **Statements:** each statement is encoded as two implications. If the speaker is a knight, the statement is true. If the speaker is a knave, the statement is false.
- **Inference:** `model_check` enumerates every possible assignment of truth values to the symbols and keeps those consistent with the knowledge base. A symbol is printed only when it is true in every consistent model, meaning the knowledge base entails it.

## The puzzles and results

| Puzzle | Statements | Solution |
| --- | --- | --- |
| 0 | A says "I am both a knight and a knave." | A is a knave |
| 1 | A says "We are both knaves." B says nothing. | A is a knave, B is a knight |
| 2 | A says "We are the same kind." B says "We are of different kinds." | A is a knave, B is a knight |
| 3 | A says either "I am a knight." or "I am a knave.", but we don't know which. B says "A said 'I am a knave'." B says "C is a knave." C says "A is a knight." | A is a knight, B is a knave, C is a knight |

## Run

```
python puzzle.py
```

No dependencies beyond the Python standard library.

`logic.py` (the `Symbol`, `Not`, `And`, `Or`, `Implication` and `Biconditional` classes and `model_check`) is provided by the course. The knowledge bases in `puzzle.py` are mine.
