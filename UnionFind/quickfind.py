



class quickfind:
    def __init__(self,sz) -> None:
        self.id=[]
        self.size=sz
        for i in range(sz):
           self.id.append(i)



    def connected(self,p,q):
        return self.id[p]==self.id[q]
    


    def union(self,p,q):
        pid=self.id[p]
        qid=self.id[q]    
        for i in range(self.size):
          if self.id[i] == pid:
            self.id[i]=qid






test=quickfind(10)
for i in range(test.size):
   p=int(input("enter p"))
   q=int(input("emter q"))
   if not  test.connected(p,q):
      test.union(p,q)
      print(f"p={p} q={q}")



