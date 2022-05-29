from ast import Delete
from multiprocessing.sharedctypes import Value

      #--TC&SC---->O(1) for all op
class Node:
  def __init__(self,value =None,next = None):
    self.value = value
    self.next = next

class LinkedList:
  def __init__(self):
    self.head = None

class Stack:
  def __init__(self) -> None:
    # object of linked list is created
      self.LinkedList = LinkedList()
  
  def isEmpty(self):
    if self.LinkedList.head ==None:
      return True
    else:
      return False

  def push(self,value):
    node = Node(value)
    node.next = self.LinkedList.head
    self.LinkedList.head = node

  def printll(self):
    temp=self.LinkedList.head
    while(temp):
      print(temp.value)
      temp = temp.next
  
  def pop(self):
    if self.isEmpty():
      return "Stack is Empty"
    else:
      nodeValue = self.LinkedList.head.value
      self.LinkedList.head = self.LinkedList.head.next
      return nodeValue

  def peek(self):
    if self.isEmpty():
      return "Stack is Empty"
    else:
      nodeValue = self.LinkedList.head.value
      return nodeValue

  def delete(self):
    self.LinkedList.head=None

customStack= Stack()
print(customStack.isEmpty())
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.printll()
print()
print(customStack.pop())
print()
customStack.printll()
print(customStack.peek())
customStack.delete()
print(customStack.isEmpty())