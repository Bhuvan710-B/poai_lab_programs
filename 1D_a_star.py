"""
Experiment 1D - A* Search Algorithm
Course: AI23231 - Principles of Artificial Intelligence Lab

Aim:
    To implement the A* search algorithm.

Run:
    python 1D_a_star.py

A* expands the node with the lowest f = g + h, where
    g = cost from the start to the node,
    h = heuristic estimate from the node to the goal.

Example: shortest path on an open grid from (0, 0) to (3, 3) using the
Manhattan-distance heuristic. Expected output:
    Path from start to goal: [(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2), (3, 3)]
(Other equally short 6-step paths exist; ties may be broken differently.)
"""

import heapq


class Node:
    """A search node: a state plus the path/cost information A* needs."""

    def __init__(self, state, parent, g, h):
        self.state = state
        self.parent = parent
        self.g = g          # Cost to reach this node
        self.h = h          # Heuristic cost from this node to the goal
        self.f = g + h      # Total estimated cost

    def __lt__(self, other):
        # heapq uses this to keep the lowest-f node on top
        return self.f < other.f


def a_star_search(start, goal, heuristic, neighbors):
    """Return the list of states from start to goal, or None if unreachable."""
    open_list = []            # Priority queue of nodes still to explore
    closed_list = set()       # States already expanded

    heapq.heappush(open_list, Node(start, None, 0, heuristic(start, goal)))

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node.state == goal:
            # Reconstruct the path by following parent links back to the start
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return path[::-1]

        closed_list.add(current_node.state)

        for neighbor, cost in neighbors(current_node.state):
            if neighbor in closed_list:
                continue
            g = current_node.g + cost
            h = heuristic(neighbor, goal)
            neighbor_node = Node(neighbor, current_node, g, h)

            # Skip if an equal-or-better route to this state is already queued
            if not any(n.state == neighbor and n.f <= neighbor_node.f for n in open_list):
                heapq.heappush(open_list, neighbor_node)

    return None  # No path found


def heuristic(state, goal):
    """Manhattan distance between two grid cells."""
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


def neighbors(state):
    """Adjacent grid cells (right, left, up, down), each with step cost 1."""
    x, y = state
    return [
        ((x + 1, y), 1),  # Right
        ((x - 1, y), 1),  # Left
        ((x, y + 1), 1),  # Up
        ((x, y - 1), 1),  # Down
    ]


if __name__ == "__main__":
    start = (0, 0)
    goal = (3, 3)
    path = a_star_search(start, goal, heuristic, neighbors)
    print("Path from start to goal:", path)
