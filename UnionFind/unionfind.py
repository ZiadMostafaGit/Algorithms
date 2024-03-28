class unionfind:
    def __init__(self,sz) -> None:
        self.id=[]
        self.size=sz
        for i in range(self.size):
            self.id.append(i)






    def root(self,i):
        while i!=self.id[i]:
            i=self.id[i]
        return i   
    def find(self,p,q):
        return self.root(p)==self.root(q)


    def union(self,p,q):
        i=self.root(p)
        j=self.root(q)
        self.id[i]=j









test=unionfind(10)
for i in range(test.size):
   p=int(input("enter p"))
   q=int(input("emter q"))
   if not  test.find(p,q):
      test.union(p,q)
      print(f"p={p} q={q}")
