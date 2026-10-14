"""
Experiment 3A - Blocks World Program
Course: AI23231 - Principles of Artificial Intelligence Lab

Aim:
    To implement a Blocks World program (blocks stacked on a table that are
    moved one at a time).

Run:
    python 3A_blocks_world.py

Representation:
    The world is a list of stacks. Each stack is a list ordered BOTTOM -> TOP,
    so [2, 0] means block 0 sits on block 2. Blocks not on another block sit
    on the table, each in its own one-block stack.

Rules of a legal move (move(block, destination)):
    * the block being moved must be CLEAR (nothing on top of it);
    * the destination must be another CLEAR block, or the string "table".

The example below uses the initial state, goal and the three moves given in
the lab manual. The manual's moves are applied to the INITIAL state (the
manual overwrote the state with the goal before moving).

Output:
    Initial state:
      stack: [0]
      stack: [1]
      stack: [2]
    Goal state (bottom -> top):
      stack: [0, 1]
      stack: [2]

    Performing Moves:
    Move 0 onto 2 ...
      stack: [1]
      stack: [2, 0]
    Move 1 onto 2 ...
    Illegal move: block 2 is not clear.
    Move 2 onto table ...
    Illegal move: block 2 is not clear.

    Goal reached? No

NOTE: The manual's move sequence does not reach its own goal (and its
2nd and 3rd moves are illegal in a real Blocks World), so the final line
is "No". See the README for the question about the intended sequence.
"""

TABLE = "table"


class BlocksWorld:
    def __init__(self, num_blocks):
        # Every block starts on the table in its own stack
        self.state = [[block] for block in range(num_blocks)]
        self.num_blocks = num_blocks

    def display_state(self):
        """Print every stack (bottom -> top)."""
        for stack in self.state:
            print(f"  stack: {stack}")

    def find_stack(self, block):
        """Return the stack containing `block`, or None if it does not exist."""
        for stack in self.state:
            if block in stack:
                return stack
        return None

    def is_clear(self, block):
        """A block is clear if it is the top of its stack."""
        stack = self.find_stack(block)
        return stack is not None and stack[-1] == block

    def move(self, block, destination):
        """Move `block` onto another block or onto the table.

        Returns True if the move was made, False if it was illegal.
        """
        source = self.find_stack(block)
        if source is None:
            print(f"Illegal move: block {block} does not exist.")
            return False
        if not self.is_clear(block):
            print(f"Illegal move: block {block} is not clear.")
            return False

        if destination == TABLE:
            if len(source) == 1:
                print(f"Block {block} is already on the table.")
                return False
            source.pop()
            self.state.append([block])          # Starts a new stack on the table
        else:
            target = self.find_stack(destination)
            if target is None:
                print(f"Illegal move: block {destination} does not exist.")
                return False
            if destination == block:
                print("Illegal move: a block cannot be placed on itself.")
                return False
            if not self.is_clear(destination):
                print(f"Illegal move: block {destination} is not clear.")
                return False
            source.pop()
            target.append(block)

        self.state = [s for s in self.state if s]  # Drop emptied stacks
        self.display_state()
        return True

    def matches(self, goal):
        """True if the current stacks equal `goal` (order of stacks ignored)."""
        return sorted(map(tuple, self.state)) == sorted(map(tuple, goal))


def main():
    # Three blocks (0, 1, 2), all on the table
    world = BlocksWorld(3)
    print("Initial state:")
    world.display_state()

    # Goal from the lab manual, written bottom -> top
    goal = [[0, 1], [2]]
    print("Goal state (bottom -> top):")
    for stack in goal:
        print(f"  stack: {stack}")

    print("\nPerforming Moves:")
    print("Move 0 onto 2 ...")
    world.move(0, 2)
    print("Move 1 onto 2 ...")
    world.move(1, 2)
    print("Move 2 onto table ...")
    world.move(2, TABLE)

    print("\nGoal reached?", "Yes" if world.matches(goal) else "No")


if __name__ == "__main__":
    main()
