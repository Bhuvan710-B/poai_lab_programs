"""
Experiment 1B - Depth First Search (DFS)
Course: AI23231 - Principles of Artificial Intelligence Lab

Aim:
    To implement depth first search on a graph.

Run:
    python 1B_dfs.py

Example graph (undirected):
          0
         / \\
        1   2
       / \\   \\
      3   4   5

Expected output:
    Depth First Search starting from vertex 0:
    0 1 3 4 2 5
"""


class Graph:
    """Undirected graph stored as an adjacency list."""

    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = {i: [] for i in range(vertices)}

    def add_edge(self, u, v):
        """Add an undirected edge between u and v."""
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self, v, visited):
        """Recursive DFS: go as deep as possible, then backtrack."""
        print(v, end=" ")      # Visit the current node
        visited[v] = True      # Mark it as visited

        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited)


def depth_first_search():
    """Build the example graph and run DFS from vertex 0."""
    g = Graph(6)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 5)

    visited = [False] * g.vertices   # Tracks which nodes were visited

    print("Depth First Search starting from vertex 0:")
    g.dfs(0, visited)
    print()  # Final newline


if __name__ == "__main__":
    depth_first_search()
