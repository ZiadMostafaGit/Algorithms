import java.util.*;

class Graph<T> {
    private Map<T, List<T>> graph;

    public Graph() {
        graph = new HashMap<>();
    }

    public void addEdge(T fromNode, T toNode) {
        graph.computeIfAbsent(fromNode, k -> new ArrayList<>()).add(toNode);
    }

    public void dfs(T startNode) {
        Set<T> visited = new HashSet<>();
        dfsHelper(startNode, visited);
        System.out.println();
    }

    private void dfsHelper(T node, Set<T> visited) {
        visited.add(node);
        System.out.print(node + " ");
        List<T> neighbors = graph.get(node);
        if (neighbors != null) {
            for (T neighbor : neighbors) {
                if (!visited.contains(neighbor)) {
                    dfsHelper(neighbor, visited);
                }
            }
        }
    }

    public void bfs(T startNode) {
        Set<T> visited = new HashSet<>();
        Queue<T> queue = new LinkedList<>();
        queue.add(startNode);

        while (!queue.isEmpty()) {
            T node = queue.poll();
            if (!visited.contains(node)) {
                System.out.print(node + " ");
                visited.add(node);
                List<T> neighbors = graph.get(node);
                if (neighbors != null) {
                    for (T neighbor : neighbors) {
                        if (!visited.contains(neighbor)) {
                            queue.add(neighbor);
                        }
                    }
                }
            }
        }
        System.out.println();
    }

    public void printGraph() {
        for (Map.Entry<T, List<T>> entry : graph.entrySet()) {
            T node = entry.getKey();
            List<T> edges = entry.getValue();
            System.out.print(node + " -> ");
            for (T edge : edges) {
                System.out.print(edge + " ");
            }
            System.out.println();
        }
    }

    // Example Usage:
    public static void main(String[] args) {
        Graph<Integer> graph = new Graph<>();
        graph.addEdge(1, 2);
        graph.addEdge(1, 3);
        graph.addEdge(2, 3);
        graph.addEdge(3, 1);

        System.out.println("DFS Traversal:");
        graph.dfs(1);
        System.out.println("BFS Traversal:");
        graph.bfs(1);
    }
}
