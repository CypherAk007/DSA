class Node:
  def __init__(self,data,nxt):
    self.data=data
    self.nxt=nxt

class LinkedList:
  def __init__(self):
    self.head=None
    self.tail=None

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

  def delDup(self,head):
    c=head
    n=head.nxt
    while n!=None:
      if n.nxt==None and c.data==n.data:
        c.nxt=None
        return
      if c.data==n.data:
        n=n.nxt
      else:
        c.nxt=n
        c=n
        n=n.nxt

  def delDupKk(self,current):
    # current=self.head
    while(current.nxt!=None):
      if current.data==current.nxt.data:
        current.nxt=current.nxt.nxt
      else:
        current=current.nxt

    tail=current
    tail.nxt=None
      
      
if __name__=='__main__':
  ll=LinkedList()
  ll.insert_at_beg(1)
  ll.insert_at_beg(1)
  ll.insert_at_beg(3)
  ll.insert_at_beg(3)
  ll.insert_at_beg(2)
  ll.insert_at_beg(2)
  # ll.delDup(ll.head)
  ll.printll() 
  ll.delDupKk(ll.head)
  ll.printll()