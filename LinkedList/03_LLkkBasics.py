# insert using recursion
from reprlib import recursive_repr


class Node:
  def __init__(self,data,nxt):
    self.data = data
    self.nxt=nxt

class LinkedList:
  def __init__(self):
      self.head=None

  def insertRecMain(self,data,index):
    self.head=self.insertRec(data,index,self.head)

  def insertRec(self,data,index,current):
    if index==0:
      temp=Node(data,current)
      return temp
    
    robc=self.insertRec(data,index-1,current.nxt)
    current.nxt=robc 
    return current

  def printll(self):
    if self.head==None:
      print('empty ll')
      return
    
    itr=self.head
    llstr=''
    while itr:
      llstr+=str(itr.data)+' --> '
      itr=itr.nxt
    print(llstr)

  def insert_at_beg(self,data):
    node = Node(data,self.head)# so that the new node points to the old node
    self.head=node

  def insert_at_end(self,data):
    if self.head is None:
      node = Node(data,None)
      self.head=node
      return

    itr=self.head
    while itr.next:
      itr = itr.next
    itr.next=Node(data,None)

  def recursiveCount(self,current):
    if current==None:
      return 0

    else:
      temp=self.recursiveCount(current.nxt)
      return 1+temp

  def recursivePrint(self,current):
    if current==None:
      return
    print(current.data)
    self.recursivePrint(current.nxt)

  def findANode(self,current,value):
    # itr=self.head
    if current.nxt==None:
      return None

    elif (current.data==value):
      print(value,'was found')
      return value

    else:
      out=self.findANode(current.nxt,value)
      return out


if __name__=='__main__':
  ll=LinkedList()
  ll.insert_at_beg(1)
  ll.insert_at_beg(2)
  # ll.insert_at_beg(3)
  ll.insert_at_beg(4)
  ll.insert_at_beg(5)
  # print(ll.recursiveCount(ll.head))
  # ll.recursivePrint(ll.head)
  # print(ll.findANode(ll.head,5))
  ll.insertRecMain(40,0)
  ll.printll()