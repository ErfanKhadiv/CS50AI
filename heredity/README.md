# Heredity

Computes the probability that each person in a family has 0, 1 or 2 copies of a gene, and whether they show a trait, using a **Bayesian network** and **inference by enumeration**.

- A person's gene count depends on their parents' (each parent passes a copy with a probability that includes a small mutation chance). People without parents use an unconditional prior.
- The trait depends on the person's gene count.
- `joint_probability` computes the probability of one full assignment, `update` adds it to each person's distributions, and `normalize` rescales them to sum to 1.
- Known trait evidence in the CSV is respected: assignments that contradict it are skipped.

## Run

```
python heredity.py data/family0.csv
```

Example output for `family0` (Harry's parents are Lily and James; James is known to have the trait and Lily is known not to):

```
Harry:  Gene 2: 0.0092 | 1: 0.4557 | 0: 0.5351   Trait True: 0.2665
James:  Gene 2: 0.1976 | 1: 0.5106 | 0: 0.2918   Trait True: 1.0000
Lily:   Gene 2: 0.0036 | 1: 0.0136 | 0: 0.9827   Trait True: 0.0000
```

`main`, `load_data`, `powerset` and the probability tables are provided by the course. `joint_probability`, `update` and `normalize` are mine.
