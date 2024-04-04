import sys

def dijkstra(graph, source):
    V = len(graph)
    
    distances = [sys.maxsize] * V
    
    distances[source] = 0
    
    visited = [False] * V
    
    for _ in range(V):
        u = min_distance(distances, visited)
        
        visited[u] = True
        
        for v in range(V):
            if graph[u][v] > 0 and not visited[v] and distances[v] > distances[u] + graph[u][v]:
                distances[v] = distances[u] + graph[u][v]
    
    return distances

def min_distance(distances, visited):
    min_dist = sys.maxsize
    min_index = -1
    
    for v in range(len(distances)):
        if distances[v] < min_dist and not visited[v]:
            min_dist = distances[v]
            min_index = v
    
    return min_index

graph = [
    [0, 4, 0, 2],
    [4, 0, 5, 0],
    [0, 5, 0, 1],
    [2, 0, 1, 0]
]

source_vertex = 0
shortest_distances = dijkstra(graph, source_vertex)
print("Shortest distances from vertex", source_vertex, "to all other vertices:")
for vertex, distance in enumerate(shortest_distances):
    print("Vertex", vertex, ":", distance)
