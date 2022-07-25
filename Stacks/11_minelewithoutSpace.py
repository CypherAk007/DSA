# Get min ele in stack O(1) space?
class GetMinimum:
    def __init__(self):
        self.s=[]
        self.minEle=0
        
    def getMin(self):
        if len(self.s)==0:
            return -1
        return minEle
    
    def push(self,x):
        if len(self.s)==0:
            self.s.append(x)
            self.minEle=x
        else:
            if x>=self.minEle:
                self.s.append(x)
            else:
                self.s.append(2*x-self.minEle)
                self.minEle=x 
    
    def pop(self):
        if len(self.s)==0:
            return -1
        else:
            if self.s[-1]>=self.minEle:
                self.s.pop()
            else:
                self.minEle=2*self.minEle-self.s[-1]
                self.s.pop()
    
    def top(self):
        if len(self.s)==0:
            return -1
        else:
            if self.s[-1]>=self.minEle:
                return self.s[-1]
            elif(self.s[-1]<self.minEle):
                return self.minEle
            
    def printf(self):
        print(self.s,self.minEle)
        
        
x=GetMinimum()
x.printf()
print(x.getMin())
x.push(10)
x.push(9)
x.printf()
print(x.top())
x.pop()
x.printf()