class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        if self.rank[pu] > self.rank[pv]:
            self.parent[pv] = pu
        elif self.rank[pv] > self.rank[pu]:
            self.parent[pu] = pv
        else:
            self.parent[pu] = pv
            self.rank[pv] += 1
        return True


class WeightedGraph:
    def __init__(self):
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append((weight, u, v))

    def kruskal_mst(self):
        self.edges.sort()
        mst = []
        disjoint_set = DisjointSet(len(self.edges))

        for weight, u, v in self.edges:
            if disjoint_set.union(u, v):
                mst.append((u, v, weight))

        return mst


# Example usage:
if __name__ == "__main__":
    graph = WeightedGraph()
    graph.add_edge(0, 1, 4)
    graph.add_edge(0, 2, 3)
    graph.add_edge(1, 2, 1)
    graph.add_edge(1, 3, 2)
    graph.add_edge(2, 3, 5)
    graph.add_edge(2, 4, 6)
    graph.add_edge(3, 4, 7)
    graph.add_edge(3, 5, 2)
    graph.add_edge(4, 5, 3)
    graph.add_edge(4, 6, 1)

    mst = graph.kruskal_mst()
    print("Minimum Spanning Tree:")
    for edge in mst:
        print(edge)