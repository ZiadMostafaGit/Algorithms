





class graph:
    def __init__(self,nodes) -> None:
            self.nodes=nodes
            self.matrix=[[0 for _ in range(nodes)]for _ in range(nodes)]
            for i in range(nodes):
                  for j in range(nodes):
                        self.matrix[i][j]=0



    def add_edg(self,row,col):
          self.matrix[row][col]+=1

    def print_graph(self):
          for i in range(self.nodes):
                for j in range(self.nodes):
                      print(self.matrix[i][j],end=" ")
                print() 



    def is_connected(self,row,col):
          return self.matrix[row][col]>0




class weighted_graph:
    def __init__(self,nodes) -> None:
            self.nodes=nodes
            self.matrix=[[0 for _ in range(nodes)]for _ in range(nodes)]
            for i in range(nodes):
                  for j in range(nodes):
                        self.matrix[i][j]=0



    def add_edg(self,row,col,weight):
          self.matrix[row][col]=weight

    def print_graph(self):
          for i in range(self.nodes):
                for j in range(self.nodes):
                      print(self.matrix[i][j],end=" ")
                print() 



    def is_connected(self,row,col):
          return self.matrix[row][col]>0





gr=weighted_graph(5)
gr.add_edg(0,2,4)
gr.add_edg(1,3,5)
gr.add_edg(2,4,41)
gr.add_edg(1,3,22)
gr.add_edg(3,2,4)


gr.print_graph()


print(gr.is_connected(0,2))
print(gr.is_connected(1,2))












                        