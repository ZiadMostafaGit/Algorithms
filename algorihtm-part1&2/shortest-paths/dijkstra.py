import heapq

def dijkstra(graph, source):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[source] = 0
    pq = [(0, source)]  
    
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)

        if current_distance > distances[current_vertex]:
            continue
        
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'D': 5},
    'C': {'A': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

source_vertex = 'A'
shortest_distances = dijkstra(graph, source_vertex)
print("Shortest distances from", source_vertex, "to all other vertices:")
for vertex, distance in shortest_distances.items():
    print(vertex, ":", distance)
