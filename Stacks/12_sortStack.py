class SortStack:
  def __init__(self) :
    self.s1=[]
    self.s2=[]
  
  def push(self,x):
    
    if len(self.s1)==0:
      self.s1.append(x)
    elif len(self.s1)>0 and x>self.s1[-1]:
      self.s1.append(x)
    elif len(self.s1)>0 and x<=self.s1[-1]:
      while(len(self.s1)>0 and x<=self.s1[-1]): 
        val=self.s1.pop()
        self.s2.append(val)
      self.s1.append(x)
      while(len(self.s2)>0): 
        val=self.s2.pop()
        self.s1.append(val)

  def pop(self):
    if len(self.s1)    !=0:
      return self.s1.pop()
  
  def printf(self):
    print(self.s1)
s=SortStack()
s.push(10)
s.push(40)
s.push(30)
s.push(20)
s.printf()
