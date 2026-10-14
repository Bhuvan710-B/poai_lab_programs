"""
Experiment 2E - Backward Chaining
Course: AI23231 - Principles of Artificial Intelligence Lab

Aim:
    To implement backward chaining.

Run:
    python 2E_backward_chaining.py

Backward chaining starts from the GOAL and works backwards: a goal is true
if it is a known true fact, or if some rule concludes it and every condition
of that rule can itself be proved.

Knowledge base:
    Facts: a = True, b = True, c = False
    Rules: d <- a, b
           e <- b, c
           f <- d, e

Output:
    The goal 'f' cannot be achieved.   (e needs c, which is False)
    The goal 'd' can be achieved.      (a and b are True)
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


def backward_chaining(goal, facts, rules):
    """Return True if `goal` can be proved from the facts and rules."""
    # 1. If the goal is a known fact, use its value
    if goal in facts:
        return facts[goal]

    # 2. Otherwise, try every rule that concludes the goal
    for head, body in rules:
        if head == goal:
            # The rule fires only if ALL its conditions can be proved
            if all(backward_chaining(condition, facts, rules) for condition in body):
                return True

    # 3. No fact or rule proves the goal
    return False


if __name__ == "__main__":
    for goal in ["f", "d"]:
        if backward_chaining(goal, facts, rules):
            print(f"The goal '{goal}' can be achieved.")
        else:
            print(f"The goal '{goal}' cannot be achieved.")
