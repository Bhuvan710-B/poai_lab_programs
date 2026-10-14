"""
Experiment 2D - Unification and Resolution Algorithm
Course: AI23231 - Principles of Artificial Intelligence Lab

Aim:
    To implement the unification and resolution algorithms in Python.

Run:
    python 2D_unification_resolution.py

Part 1 - Unification: finds a substitution that makes two terms identical.
    Convention: a LOWERCASE string is a variable ('x'); constants and
    predicate names are capitalised ('John', 'Loves'). Terms are lists.

Part 2 - Resolution (propositional): proves a query by refutation.
    A clause is a list of literals, e.g. ["~P", "Q"] means (NOT P) OR Q.
    To prove the query, its negation is added to the knowledge base (KB);
    if the EMPTY clause can be derived, the KB contradicts the negated
    query, so the query follows from the KB.

Output:
    Unify ['Loves', 'x', 'Mary'] with ['Loves', 'John', 'y']:
      {'x': 'John', 'y': 'Mary'}
    Unify 'x' with ['F', 'x'] (occurs check):
      None (cannot unify)
    Knowledge Base: [['~P', 'Q'], ['P'], ['~Q', 'R'], ['~R']]
    Query: ['R']
    The query follows from the knowledge base (empty clause derived).

NOTE: The lab manual's recorded output says "The query is not satisfiable."
That does not match this KB, which is itself contradictory (P, P->Q, Q->R
and ~R cannot all be true), so ANY query is provable from it.
"""


# ---------------------------------------------------------------
# Part 1: Unification
# ---------------------------------------------------------------
def is_variable(term):
    """A lowercase string is treated as a variable."""
    return isinstance(term, str) and term.islower()


def unify(term1, term2, subst):
    """Unify two terms. Returns the substitution dict, or None on failure."""
    if subst is None:
        return None
    if term1 == term2:
        return subst
    if is_variable(term1):
        return unify_var(term1, term2, subst)
    if is_variable(term2):
        return unify_var(term2, term1, subst)
    if isinstance(term1, list) and isinstance(term2, list) and len(term1) == len(term2):
        if not term1:                       # Both lists are empty
            return subst
        # Unify the first elements, then the rest with the updated substitution
        return unify(term1[1:], term2[1:], unify(term1[0], term2[0], subst))
    return None


def unify_var(var, x, subst):
    """Unify a variable with a term, respecting existing bindings."""
    if var in subst:
        return unify(subst[var], x, subst)
    if is_variable(x) and x in subst:       # (guard avoids hashing a list)
        return unify(var, subst[x], subst)
    if occurs_check(var, x, subst):
        return None
    subst[var] = x
    return subst


def occurs_check(var, x, subst):
    """True if var occurs inside x (would create an infinite term)."""
    if var == x:
        return True
    if isinstance(x, list):
        return any(occurs_check(var, xi, subst) for xi in x)
    if is_variable(x) and x in subst:
        return occurs_check(var, subst[x], subst)
    return False


# ---------------------------------------------------------------
# Part 2: Resolution (propositional)
# ---------------------------------------------------------------
def negate(literal):
    """Negate a literal: 'P' -> '~P' and '~P' -> 'P'."""
    return literal[1:] if literal.startswith("~") else "~" + literal


def resolve(clause1, clause2):
    """Return all resolvents of two clauses (clauses are frozensets)."""
    resolvents = []
    for lit in clause1:
        if negate(lit) in clause2:
            resolvents.append((clause1 - {lit}) | (clause2 - {negate(lit)}))
    return resolvents


def resolution(kb, query):
    """Return True if `query` (a list of literals) follows from `kb`.

    The negation of the query is added to the KB. For a query that is a
    disjunction of literals, each literal's negation is its own clause.
    """
    clauses = {frozenset(c) for c in kb}
    clauses |= {frozenset([negate(lit)]) for lit in query}

    while True:
        new = set()
        clause_list = list(clauses)
        for i in range(len(clause_list)):
            for j in range(i + 1, len(clause_list)):
                for resolvent in resolve(clause_list[i], clause_list[j]):
                    if not resolvent:       # Empty clause = contradiction found
                        return True
                    new.add(resolvent)
        if new <= clauses:                  # Nothing new can be derived
            return False
        clauses |= new


if __name__ == "__main__":
    # --- Unification demo ---
    print("Unify ['Loves', 'x', 'Mary'] with ['Loves', 'John', 'y']:")
    print(" ", unify(["Loves", "x", "Mary"], ["Loves", "John", "y"], {}))

    print("Unify 'x' with ['F', 'x'] (occurs check):")
    result = unify("x", ["F", "x"], {})
    print(" ", result if result is not None else "None (cannot unify)")

    # --- Resolution demo (knowledge base and query from the lab manual) ---
    knowledge_base = [
        ["~P", "Q"],   # P -> Q
        ["P"],         # P
        ["~Q", "R"],   # Q -> R
        ["~R"],        # NOT R
    ]
    query = ["R"]

    print("Knowledge Base:", knowledge_base)
    print("Query:", query)

    if resolution(knowledge_base, query):
        print("The query follows from the knowledge base (empty clause derived).")
    else:
        print("The query does not follow from the knowledge base.")
