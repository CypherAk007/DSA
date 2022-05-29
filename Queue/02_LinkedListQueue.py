from ast import Delete
from collections import deque


class Node:
  def __init__(self,value=None):
    self.value = value
    self.next = None
  
  def __str__(self):
    return str(self.value)

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
  
  # By using this function we are making this linked list iterable.
  def __iter__(self):
    curNode = self.head
    while curNode:
      yield curNode
      curNode=curNode.next


class Queue:
  def __init__(self):
    self.linkedList = LinkedList()

  # To make our queue printable
  def __str__(self):
    values = [str(x) for x in self.linkedList]
    return ' '.join(values)

  def enqueue(self,value):
    newNode = Node(value)
    if self.linkedList.head==None:
      self.linkedList.head=newNode
      self.linkedList.tail=newNode
    else:
      self.linkedList.tail.next=newNode
      self.linkedList.tail=newNode

  def isEmpty(self):
    if self.linkedList.head == None:
      return True
    else:
      return False
    
  def dequeue(self):
    if self.isEmpty():
      return "queue is empty"

    else:
      temp=self.linkedList.head
      if self.linkedList.head==self.linkedList.tail:
        self.linkedList.head = None
        self.linkedList.tail = None
      else:
        self.linkedList.head=self.linkedList.head.next
      return temp

  def peek(self):
    if self.isEmpty():
      return "queue is empty"

    else:
      return self.linkedList.head

  def Delete(self):
    self.linkedList.head=None
    self.linkedList.tail=None

customQueue = Queue()
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue)
print()
print(customQueue.dequeue())
print()
print(customQueue)
print(customQueue.peek())
