class stack:
    def __init__(self):
        self.lst=[]
    
    def getLen(self):
        return len(self.lst)
        
    def isEmpty(self):
        if len(self.lst)==0:
            print("st is empty")
            return True
        else:
            return False
            
    def push(self,ele):
        self.lst.append(ele)
        print("push successful")
        return "push successful"    
    
    def pop(self):
        if self.isEmpty():
            return False
        else:
            return self.lst.pop()

    def peek(self):
        if self.isEmpty():
            return False
        else:
            return self.lst[-1]
            
class sortst:
    def __init__(self):
        self.st=stack()
        
    def sortstack(self):
        if self.st.getLen()==1:
            return 
        temp=self.st.pop()
        self.sortstack()
        self.insertStack(temp)
        
        
    
    def insertStack(self,ele):
        if self.st.peek()==False or self.st.peek()<=ele :
            self.st.push(ele)
            return 
        
        temp=self.st.pop()
        self.insertStack(ele)
        self.st.push(temp)
        
        
sta=sortst()
print(sta.st.push(2))
print(sta.st.push(3))
print(sta.st.push(1))
print(sta.st.push(5))
print(sta.st.push(4))
print(sta.st.getLen())
print(sta.st.peek())
print(sta.st.lst)
sta.sortstack()
print(sta.st.peek())
print(sta.st.lst)