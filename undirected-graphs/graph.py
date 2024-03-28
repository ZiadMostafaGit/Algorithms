from collections import deque


class Graph:
    def __init__(self):
        """
        Initialize an empty graph.
        """
        self.graph = {}

    def add_edge(self, u, v):
        """
        Add an edge between nodes u and v.
        """
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def remove_edge(self, u, v):
        """
        Remove the edge between nodes u and v.
        """
        if u in self.graph and v in self.graph:
            if v in self.graph[u]:
                self.graph[u].remove(v)
            if u in self.graph[v]:
                self.graph[v].remove(u)

    def get_neighbors(self, u):
        """
        Get the neighbors of node u.
        """
        return self.graph.get(u, [])

    def has_edge(self, u, v):
        """
        Check if there is an edge between nodes u and v.
        """
        return u in self.graph and v in self.graph[u]

    def get_vertices(self):
        """
        Get all vertices/nodes in the graph.
        """
        return list(self.graph.keys())

    def find_path_dfs(self, start, end, path=[]):
        """
        Find a path between nodes start and end.
        """
        path = path + [start]
        if start == end:
            return path
        if start not in self.graph:
            return None
        for node in self.graph[start]:
            if node not in path:
                new_path = self.find_path_dfs(node, end, path)
                if new_path:
                    return new_path
        return None
    




    def find_path_bfs(self,start,end):
        if start not in self.graph or end not in self.graph:
            return None
        queue=deque([(start,[start])])
        visited=set()
        while queue:
            node,path=queue.popleft()
            visited.add(node)
            if node == end:
                return path
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    queue.append((neighbor,path+[neighbor]))
        return None            


# Create a graph
graph = Graph()

# Connect the numbers in some way
graph.add_edge(0, 1)
graph.add_edge(1, 3)
graph.add_edge(2, 4)
graph.add_edge(3, 5)
graph.add_edge(4, 6)
graph.add_edge(6, 7)
graph.add_edge(7, 8)
graph.add_edge(8, 9)


start_node = 2
end_node = 8
path = graph.find_path_bfs(start_node, end_node)
if path:
    print(f"There is a path from node {start_node} to node {end_node}: {path}")
else:
    print(f"There is no path from node {start_node} to node {end_node}.")
