class Stack:
  def __init__(self,maxSize):
    self.maxSize = maxSize
    self.list = []

  def __str__(self):
    values = reversed(self.list)
    values = [str(x) for x in values]
    return '\n'.join(values)

  # isEmpty
  def isEmpty(self):
    if self.list==[]:
      return True
    else:
      return False

  # isFull
  def isFull(self):
    if len(self.list)==self.maxSize:
      return True
    else:
      return False
  
  # Push
  def Push(self,value):#--TC---->O(1)| O(n^2)- #--SC---->O(1)-
    if self.isFull():
      return "The stack is Full"
    else:
      self.list.append(value)
      return "The element has appended successfully"

    # pop
  def pop(self):
    if self.isEmpty():
      return "Stack is Empty"
    else:
      return self.list.pop() # returns the element and pops it out.

  def peek(self):
    if self.isEmpty():
      return "Stack is Empty"
    else:
      #--TC&SC---->O(1)
      return self.list[len(self.list)-1]

  def delete(self):#--TC&SC---->O(1)
    self.list = []
customStack = Stack(4)
print(customStack.isEmpty())
print(customStack.isFull())
customStack.Push(1)
customStack.Push(2)
customStack.Push(3)
print(customStack)
