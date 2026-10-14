# POAI Lab Programs

Programs for **AI23231 – Principles of Artificial Intelligence Lab**
(Rajalakshmi Engineering College, Department of AI & ML).
Each file starts with a header comment giving the experiment name, aim and
how to run it.

## Software needed

| For | Install |
| --- | --- |
| Python programs (`.py`) | [Python 3.8+](https://www.python.org/downloads/) |
| `3B_fuzzy_inference.py` | `pip install numpy scikit-fuzzy matplotlib` |
| Prolog programs (`.pl`) | [SWI-Prolog](https://www.swi-prolog.org/Download.html) (provides the `swipl` command) |

Only `3B` needs extra Python packages; all other Python programs use the
standard library.

## Files

| File | Experiment | What it does |
| --- | --- | --- |
| `1A_n_queens.py` | 1A – N-Queens problem | Places 8 queens on a chessboard with backtracking and prints one solution. |
| `1B_dfs.py` | 1B – Depth First Search | Traverses a small graph depth-first from vertex 0. |
| `1C_minimax.py` | 1C – Minimax algorithm | Picks the best Tic-Tac-Toe move for X by searching the game tree. |
| `1D_a_star.py` | 1D – A* search | Finds a shortest grid path from (0,0) to (3,3) with the Manhattan heuristic. |
| `2A_prolog_min_max.pl` | 2B in the record index – minimum and maximum of two numbers | `minimum/3` and `maximum/3` rules. |
| `2C_prolog_queries.pl` | 2C – Query execution | `likes/2` facts plus three rules about John, with example queries. |
| `2D_unification_resolution.py` | 2D – Unification and resolution | Term unification (with occurs check) and propositional resolution. |
| `2E_backward_chaining.py` | 2E – Backward chaining | Proves a goal by working back from rules to facts. |
| `2F_forward_chaining.py` | 2F – Forward chaining | Derives new facts from known facts until the goal is reached or nothing new follows. |
| `3A_blocks_world.py` | 3A – Blocks World | Stacks of blocks moved one at a time, with legal-move checks. |
| `3B_fuzzy_inference.py` | 3B – Fuzzy inference system | Temperature-to-fan-speed controller (triangular memberships, centroid defuzzification). |

## How to run

**Python programs** – from this folder:

```bash
python 1A_n_queens.py        # use python3 on Linux/macOS if needed
python 1B_dfs.py
python 1C_minimax.py
python 1D_a_star.py
python 2D_unification_resolution.py
python 2E_backward_chaining.py
python 2F_forward_chaining.py
python 3A_blocks_world.py
python 3B_fuzzy_inference.py   # opens a plot window; close it to see the result
```

**Prolog programs** – load the file in SWI-Prolog, then type queries at the
`?-` prompt (press `;` for more answers, `.` to stop, `halt.` to quit):

```bash
swipl 2A_prolog_min_max.pl
?- minimum(5, 10, Min).
?- maximum(8, 3, Max).

swipl 2C_prolog_queries.pl
?- likes(john, food).
?- likes(john, Y).
```

## Notes on differences from the lab manual

The sample code in the manual was checked and corrected so that every program
runs. Where the manual's recorded output does not match what the code
produces, the programs print what the code actually produces:

- **1A** – the manual code printed all 92 solutions; it now stops at the first one.
- **1C** – the manual's example board is already won by X, so the result is not meaningful (the program says so).
- **2C** – the answers to `likes(john, Y)` come out as `wine, mary, food, wine, mary, john, ...`, not the three answers in the manual's screenshot.
- **2D** – the manual's knowledge base is contradictory, so the query is provable; the manual's "not satisfiable" output is not reproduced.
- **2F** – `c = False` was previously treated as true; with the fix, goals `f` and `e` cannot be achieved.
- **3A** – the manual's three moves do not reach its goal and two of them are illegal; the program reports this.
- **3B** – prints `7.56`; the manual's screenshot shows `6.00`.
