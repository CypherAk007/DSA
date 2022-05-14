from email import header


class Node:
  def __init__(self,data=None,nxt=None):
    self.data=data
    self.nxt=nxt

class LinkedList:
  def __init__(self):
    self.head=None
    self.tail = None

  def insert(self,data):
    if self.head==None:
      node=Node(data,None)
      self.head=node
      self.tail=node
      node.nxt=self.head
      return
    node = Node(data,None)
    itr=self.head
    while(itr.nxt!=self.head):
      itr=itr.nxt
    itr.nxt=node
    node.nxt=self.head

  def insert_at_beg(self,data):
    node = Node(data,None)
    node.nxt=self.head
    itr=self.head
    if self.head == None:
      node.nxt=node
      self.head=node
      self.tail = node
      return
    while itr!=self.head:
      itr=itr.nxt
    itr.nxt=node
    self.head=node

    # def insert_at_end(self,data):
    #   node

  def display(self):
    if self.head == None:
      print('empty ll')
      return
    llstr=''
    itr=self.head
    while itr:
      llstr+=str(itr.data)+' --> '
      itr=itr.nxt
      if itr==self.head:
        break
    print(llstr)


if __name__=="__main__":
  ll=LinkedList()
  ll.insert_at_beg(1)
  ll.insert_at_beg(2)
  # ll.insert_at_beg(3)
  ll.insert(1)
  ll.insert(10)
  ll.insert(100)
  ll.display()  
    