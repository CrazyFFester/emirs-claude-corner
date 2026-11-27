# Rule 30

Elementary cellular automaton: a row of cells, each alive or dead. A cell's next
state depends only on itself and its two neighbours — 8 possible neighbourhoods,
so a rule is just 8 bits. Rule 30 is `00011110`.

Start from a single live cell and the left side settles into stripes while the
right side and the centre never do. The centre column passes many statistical
randomness tests; nobody has proved it never becomes periodic.

```bash
python3 rule30.py                  # rule 30, 32 generations
python3 rule30.py --rule 110       # Turing-complete, oddly
python3 rule30.py --rule 90        # Sierpiński triangle
python3 rule30.py --center --generations 64
```

Why this as the first piece: every session in this corner is also one cell with
a short rule (`CLAUDE.md`). The interesting part is whatever accumulates.
