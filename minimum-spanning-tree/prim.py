from collections import defaultdict
import heapq
import math  # Import for accessing the `inf` constant

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v, weight):
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))  # Add the edge in both directions for undirected graphs

    def prim_mst(self, start_vertex):
        visited = set()
        mst = []
        heap = [(0, start_vertex, None)]  # Priority queue to store vertices, weights, and parents

        while heap:
            weight, vertex, parent = heapq.heappop(heap)

            if vertex not in visited:
                visited.add(vertex)

                if parent is not None:  # Skip the first iteration as it's the starting vertex
                    mst.append((parent, vertex, weight))

                for neighbor, edge_weight in self.graph[vertex]:
                    if neighbor not in visited:
                        heapq.heappush(heap, (edge_weight, neighbor, vertex))

        return mst
    

# Example usage:
if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1, 4)
    g.add_edge(0, 2, 3)
    g.add_edge(1, 2, 1)
    g.add_edge(1, 3, 2)
    g.add_edge(2, 3, 5)
    g.add_edge(2, 4, 6)
    g.add_edge(3, 4, 7)
    g.add_edge(3, 5, 2)
    g.add_edge(4, 5, 3)
    g.add_edge(4, 6, 1)

    mst = g.prim_mst(0)
    print("Minimum Spanning Tree:")
    for edge in mst:
        print(edge)
