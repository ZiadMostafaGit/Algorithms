


public class testcase {





    public static void main(String[] args) {
        
        Graph G=new Graph(8);
        G.addEdge(1, 2);
        G.addEdge(4, 7);
        G.addEdge(0, 5);
        G.addEdge(5, 6);
        G.addEdge(6, 1);

        int source = 0;
        DFS dfs = new DFS(G, source);

        
        for (int v = 0; v < G.V(); v++) {
            if (dfs.marked(v)) {
                System.out.print(v + " ");
            }
        }
        System.out.println();
    }








    }
    

