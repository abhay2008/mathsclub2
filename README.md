# Maths Club 2 — Interactive Linear Algebra Toolkit

A collection of small Python scripts and notes built for **high-school maths club sessions** (circa 2023). Each module demonstrates a classic algorithm with colored terminal output and step-by-step explanations.

## Contents

| File | Description |
|------|-------------|
| `LinearEquations.py` | Solves a 2×2 linear system using Cramer's rule / cross-multiplication |
| `EuclidDivisionLemmaAlgorithm` | Euclidean algorithm for GCD |
| `derivation.MD` | Hand-written derivation notes |
| `determinants.MD` | Determinant reference notes |

## Requirements

- Python 3.7+
- No external packages

## Quick start

### Solve two linear equations

```bash
python3 LinearEquations.py
```

Example input:

```
Enter the first equation in the form ax + by + c = 0:  2x + 3y - 6 = 0
Enter the second equation in the form ax + by + c = 0:  x - y - 1 = 0
```

The script prints the determinant, cross-multiplication steps, and final `(x, y)` solution.

### Euclidean algorithm

```bash
python3 EuclidDivisionLemmaAlgorithm
```

## Features

- ANSI-colored terminal output for classroom projection
- Inline derivation steps so students can follow the logic
- Pure standard library — runs anywhere

## Topics covered

- Systems of linear equations in two variables
- Determinants and Cramer's rule
- Euclidean division lemma / GCD

## Author

**Abhay Kashyap** — [github.com/abhay2008](https://github.com/abhay2008)
