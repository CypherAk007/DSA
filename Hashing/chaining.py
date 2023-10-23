# Chaining in Python
class MyHash:
    def __init__(self,bucketSize):
        self.bucketSize =bucketSize 
        self.lst = [[] for i in range(bucketSize)]
        
    def insert(self,val):
        idx=val%self.bucketSize
        self.lst[idx].append(val)
    
    def search(self,val):
        idx=val%self.bucketSize
        for i in range(len(self.lst[idx])):
            if self.lst[idx][i]==val:
                return True 
        return False 
    
    def remove(self,val):
        idx=val%self.bucketSize
        for i in range(len(self.lst[idx])):
            if self.lst[idx][i]==val:
                self.lst[idx].pop(i)
                break
        
        
h = MyHash(7)
h.insert(70)
h.insert(71)
h.insert(9)
h.insert(56)
h.insert(72)
print(h.search(56))
print(h.lst,h.bucketSize)
h.remove(56)
print(h.lst,h.bucketSize)

