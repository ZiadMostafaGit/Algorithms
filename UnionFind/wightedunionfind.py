


class wuf:
     def __init__(self,s) -> None:
        self.id=[]
        self.sz=[]
        self.size=s
        for i in range(self.size):
            self.id.append(i)
            self.sz.append(1)



     def find(self,p,q):
        return self.root(p)==self.root(q)





     def root(self,i):
        while i!=self.id[i]:
            self.id[i]=self.id[self.id[i]]
            i=self.id[i]
        return i    




     def union(self,p,q):
         i=self.root(p)
         j=self.root(q)  
         if i==j:
             return
         
         if self.sz[i]>self.sz[j]:
             self.id[j]=i
             self.sz[j]+=self.sz[i]
         else:
             
             self.id[i]=j     
             self.sz[j]+=self.sz[i]






# Create an instance of the wuf class with size 10
wuf_instance = wuf(10)

# Perform some union operations
wuf_instance.union(0, 1)
wuf_instance.union(2, 3)
wuf_instance.union(4, 5)
wuf_instance.union(6, 7)
wuf_instance.union(8, 9)

# Test find operation
print(wuf_instance.find(0, 1))  # True, as 0 and 1 are connected
print(wuf_instance.find(0, 2))  # False, as 0 and 2 are not connected

# Perform more union operations
wuf_instance.union(0, 2)
wuf_instance.union(4, 6)

# Test find operation again
print(wuf_instance.find(0, 2))  # True, as 0 and 2 are now connected after union operation
print(wuf_instance.find(4, 6))  # True, as 4 and 6 are connected
print(wuf_instance.find(0, 6))  # True, as 0 and 6 are indirectly connected through other unions
