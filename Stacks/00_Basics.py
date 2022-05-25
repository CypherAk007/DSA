# Using the list method
class Stack:
  def __init__(self):
      self.list=[]  #--TC&SC---->O(1)- empty list

  def __str__(self):
    values = reversed(self.list)
    values = [str(x) for x in values]
    return '\n'.join(values)

  def isEmpty(self):  #--TC&SC---->O(1)
    if self.list ==[]:
      return True
    else:
      return False

  # push
  def push(self,value): #--TC---->O(1)| O(n^2)- #--SC---->O(1)-
    self.list.append(value)
    return "The element has been successfully inserted"

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


customStack = Stack()
print(customStack.isEmpty())
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)
print('\n')
print((customStack.pop()))
print('\n')
print(customStack)
print()
print(customStack.peek())
customStack.delete()
print(customStack)
