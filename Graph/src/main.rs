use std::fmt::{Debug, Display};

struct Graph<T> {
    adj_list: Vec<Vec<(usize, T)>>,
    size: usize,
}

impl<T: Copy + Debug> Graph<T> {
    fn new(n: usize) -> Self {
        Graph {
            adj_list: vec![vec![]; n],
            size: n,
        }
    }
    fn dfs(&self, i: usize, visited: &mut Vec<bool>) {
        visited[i] = true;
        println!("Visited {}", i);

        for &(node, weight) in &self.adj_list[i] {
            if !visited[node] {
                //println!("node {:?} weight {:?}", node, weight);
                self.dfs(node, visited);
            }
        }
    }

    fn reachability(&self) {
        let mut visited = vec![false; self.size];
        for (index, node) in self.adj_list.iter().enumerate() {
            if !node.is_empty() {
                self.dfs(index, &mut visited);
                visited = vec![false; self.size];
                println!(
                    "===================================================================================================================================================================="
                );
            }
        }
    }

    fn add_edge(&mut self, from: usize, to: usize, w: T) {
        let max_index = from.max(to);

        if max_index >= self.size {
            self.adj_list.resize(max_index + 1, Vec::new());
            self.size = max_index + 1;
        }

        self.adj_list[from].push((to, w));
    }

    fn add_edge_undirected(&mut self, u: usize, v: usize, w: T) {
        let max_index = u.max(v);
        if max_index >= self.size {
            self.adj_list.resize(max_index + 1, Vec::new());
            self.size = max_index + 1;
        }

        self.adj_list[u].push((v, w));
        self.adj_list[v].push((u, w));
    }
}

fn main() {
    // let mut g: Graph<()> = Graph::new(10);

    // g.add_edge(2, 5, ());

    // g.add_edge(20, 7, ());

    // println!("{:?}", g.adj_list);
    let mut g: Graph<i32> = Graph::new(10);
    g.add_edge(1, 25, 100);
    g.add_edge(2, 1, 9);
    g.add_edge(25, 19, 8);
    g.add_edge(25, 2, 77);
    g.add_edge(4, 1, 6);
    g.add_edge(1, 7, 82);
    println!("{:?}", g.adj_list);

    println!("size ={}", g.size);
    // let mut g: Graph<i32> = Graph::new(10);
    // g.add_edge_undirected(1, 25, 100);
    // g.add_edge_undirected(2, 1, 9);
    // g.add_edge_undirected(25, 19, 8);
    // g.add_edge_undirected(4, 1, 6);
    // g.add_edge_undirected(1, 7, 82);

    // println!("{:?}", g.adj_list);
    println!(
        "===================================================================================================================================================================="
    );
    //let mut visited = vec![false; 30];
    //    g.dfs(1, &mut visited);
    // println!(
    //     "===================================================================================================================================================================="
    // );
    g.reachability();
}
