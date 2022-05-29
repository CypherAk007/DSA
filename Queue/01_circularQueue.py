
class Queue:
  def __init__(self,maxSize) -> None:# TC-O(1) and SC -O(n)
    self.items = maxSize*[None]
    self.maxSize = maxSize
    self.start = -1 #front
    self.top = -1  #rear
    

  def __str__(self):
    values = [str(x) for x in self.items]
    return ' '.join(values)

  def isFull(self):# TC-O(1) and SC -O(1)
    if self.top+1== self.start:
      return True
    elif self.start==0 and self.top+1 == self.maxSize:
      return True
    else:
      return False
    
  def isEmpty(self):# TC-O(1) and SC -O(1)
    if self.top==-1:
      return True
    else:
      return False
    

  def Enqueue(self,value):
    if self.isFull():# TC-O(1)
      return "Queue is Full"
    else:
      # self.length+=1
      if self.top+1==self.maxSize:# TC-O(1) 
        self.top=0
      else:
        self.top+=1
        if self.start ==-1:# TC-O(1) 
          self.start = 0
      self.items[self.top]=value
      return "Element is sucessfully added"

  def dequeue(self):
    if self.isEmpty():
      return "There is not any element in the Queue"
    else:
      firstElement = self.items[self.start]
      start = self.start
      if self.start ==self.top:
        self.start = -1
        self.top =-1
      elif self.start+ 1== self.maxSize:
        self.start = 0
      else:
        self.start+=1
      self.items[start]=None
      return firstElement

  def peek(self):# TC-O(1) and SC -O(1)
    if self.isEmpty():
      return "Queue is empty!"
    else:
      return self.items[self.start]

  def delete(self):# TC-O(1) and SC -O(1)
    self.items = self.maxSize*[None]
    self.top = -1
    self.start =-1



customQueue = Queue(3)
print(customQueue.isFull())
print(customQueue.isEmpty())
customQueue.Enqueue(1)
customQueue.Enqueue(2)
customQueue.Enqueue(3)
print(customQueue)
print(customQueue.isFull())
customQueue.dequeue()
customQueue.dequeue()
print(customQueue.dequeue())
print(customQueue.dequeue())
print(customQueue)
customQueue.Enqueue(2)
customQueue.Enqueue(3)
print()
print(customQueue.peek())
customQueue.delete()
print(customQueue)