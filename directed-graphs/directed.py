from collections import deque
import random

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, from_node, to_node):
        if from_node not in self.graph:
            self.graph[from_node] = []
        self.graph[from_node].append(to_node)

    def dfs(self, start_node):
        visited = set()

        def dfs_helper(node):
            visited.add(node)
            print(node, end=' ')

            if node in self.graph:
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        dfs_helper(neighbor)

        dfs_helper(start_node)
        print()

    def bfs(self, start_node):
        visited = set()
        queue = deque([start_node])

        while queue:
            node = queue.popleft()
            if node not in visited:
                print(node, end=' ')
                visited.add(node)
                if node in self.graph:
                    for neighbor in self.graph[node]:
                        if neighbor not in visited:
                            queue.append(neighbor)
        print()

    def print_graph(self):
        for node in self.graph:
            print(node, '->', ' -> '.join(self.graph[node]))

# Example Usage:
# if __name__ == "__main__":
#     graph = Graph()
#     graph.add_edge('A', 'B')
#     graph.add_edge('A', 'C')
#     graph.add_edge('B', 'C')
#     graph.add_edge('C', 'A')

#     print("DFS Traversal:")
#     graph.dfs('A')
#     print("BFS Traversal:")
#     graph.bfs('A')




if __name__ == "__main__":
    graph = Graph()

    # Define a list of 20 nodes
    nodes = list(range(1, 21))

    # Shuffle the list to add edges in a somewhat random way
    random.shuffle(nodes)

    # Adding edges
    for i in range(len(nodes) - 1):
        graph.add_edge(nodes[i], nodes[i+1])

    # Connect the last node to the first one to close the loop
    graph.add_edge(nodes[-1], nodes[0])

    print("DFS Traversal:")
    graph.dfs(nodes[6])
    print("BFS Traversal:")
    graph.bfs(nodes[6])


