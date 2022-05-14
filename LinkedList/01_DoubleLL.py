from pip import main


class Node:
  def __init__(self,data=None,prev=None,nxt=None):
    self.data = data
    self.prev=prev
    self.nxt=nxt

class LinkedList:
  def __init__(self):
      self.head = None

  def insert_at_beg(self,data):
    node = Node(data,None,self.head)
    if self.head==None:
      self.head=node
      return
    self.head.prev=node
    self.head=node


  def printdll(self):
    if self.head==None:
      print('empty ll')
      return
    
    itr=self.head
    llstr=''
    while itr:
      llstr+=str(itr.data)+' --> '
      itr=itr.nxt
    print(llstr)
    # return llstr

  def insert_at_end(self,data):
    node=Node(data,None,None)
    if self.head==None:
      self.head=node
      return
    itr =self.head
    while itr.nxt:
      itr=itr.nxt
    itr.nxt=node
    node.prev=itr


if __name__=='__main__':
  ll=LinkedList()
  ll.insert_at_beg(12)
  ll.insert_at_beg(11)
  ll.insert_at_beg(10)
  ll.insert_at_end(99)
  ll.printdll()
