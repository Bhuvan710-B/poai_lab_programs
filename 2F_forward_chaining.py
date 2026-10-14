"""
Experiment 2F - Forward Chaining
Course: AI23231 - Principles of Artificial Intelligence Lab

Aim:
    To implement forward chaining.

Run:
    python 2F_forward_chaining.py

Forward chaining starts from the KNOWN FACTS and repeatedly fires rules whose
conditions are all satisfied, adding their conclusions, until nothing new can
be inferred. Then it checks whether the goal was reached.

Knowledge base (same as Experiment 2E):
    Facts: a = True, b = True, c = False
    Rules: d <- a, b
           e <- b, c
           f <- d, e

Output (computed by this program):
    The goal 'f' cannot be achieved.
    The goal 'e' cannot be achieved.
    The goal 'd' can be achieved.

NOTE: The lab manual's recorded output says 'f' CAN be achieved. That came
from treating every key of `facts` as true, including c = False. With c
correctly treated as false, e and f cannot be derived, which also agrees with
the backward-chaining result in Experiment 2E.
"""

# Facts: known truth values
facts = {
    "a": True,
    "b": True,
    "c": False,
}

# Rules: (conclusion, [conditions that must all be true])
rules = [
    ("d", ["a", "b"]),  # d can be concluded if a and b are true
    ("e", ["b", "c"]),  # e can be concluded if b and c are true
    ("f", ["d", "e"]),  # f can be concluded if d and e are true
]


def forward_chaining(facts, rules, goal):
    """Return True if `goal` can be inferred from the facts and rules."""
    # Start with only the facts that are actually TRUE
    inferred = {name for name, value in facts.items() if value}

    changed = True
    while changed:                      # Repeat until no new fact is added
        changed = False
        for head, body in rules:
            if head not in inferred and all(cond in inferred for cond in body):
                inferred.add(head)      # Rule fires: add its conclusion
                changed = True

    return goal in inferred


if __name__ == "__main__":
    for goal in ["f", "e", "d"]:
        if forward_chaining(facts, rules, goal):
            print(f"The goal '{goal}' can be achieved.")
        else:
            print(f"The goal '{goal}' cannot be achieved.")
