# Used when the 1st incomming goes out first

# Create queue with python list with out limit


class Queue:
  def __init__(self): # TC and SC -O(1)
    self.items = []

  def __str__(self):
    values = [str(x) for x in self.items]
    return ' '.join(values)

  def isEmpty(self):# TC and SC -O(1)
    if self.items==[]:
      return True
    else:
      return False

  def enqueue(self,value):# TC -O(n) and SC -O(1)
    self.items.append(value)
    return "The element is inserted at end of Queue"
  
  def dequeue(self):
    if self.isEmpty():
      return "Empty Queue"
    else:
      return self.items.pop(0)# TC -O(n) and SC -O(1)

  def peek(self):
    if self.isEmpty():
      return "Empty Queue"
    else:
      return self.items[0]

  def delete(self):
    self.items = []

customQueue = Queue()
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue.isEmpty())
print(customQueue)
customQueue.dequeue()
print(customQueue)
print(customQueue.peek())
customQueue.delete()
print(customQueue.isEmpty())