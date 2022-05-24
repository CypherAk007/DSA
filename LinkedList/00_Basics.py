import tarfile


class Node:
  def __init__(self,data=None,next=None):
    self.data = data
    self.next = next

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail=None
  
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
    self.tail=itr.next

  def printop(self):
    if self.head is None:
      print("Linked List is empty")
      return 

    itr = self.head
    llstr=''

    while itr:
      # print(f'itr {itr}')
      llstr+=str(itr.data)+' --> '
      itr = itr.next
    print(llstr)

  def insert_values(self,data_lst):
    # self.head = None
    for data in data_lst:
      self.insert_at_end(data)

  def lengthofLL(self):
    count=0
    itr=self.head
    while itr:
      count+=1
      itr=itr.next
    return count
    
  def remove_at(self,index):
    if index<0 or index>=self.lengthofLL():
      raise Exception("Invalid Index")
    
    if index==0:
      self.head = self.head.next
      return
    
    count=0
    itr=self.head
    while count!=index-1:
      itr=itr.next
      count+=1
      # print(count,itr.data)
    # print(f'itr.data {itr.data} {itr.next.data}')
    itr.next=itr.next.next

  def insert_at(self,index,data):
    if index<0 or index>self.lengthofLL():
      raise Exception("Invalid Index")
    
    if index==self.lengthofLL():
            self.insert_at_end(data)
            return

    if index==0:
      self.head=Node(data,self.head)
      return
    
    count=0
    itr=self.head
    while itr:
      if count==index-1:
        node=Node(data,itr.next)
        itr.next=node
        break

      itr=itr.next
      count+=1

  def reversell(self):
    # itrative with 3 ptrs approach.
    n=self.head
    c=self.head
    p=None
    while n:
      n=c.next
      c.next=p
      p=c
      c=n
    self.head=p
    
  def reversellRecursive(self,node):
    if node== self.tail:
      self.head=self.tail
      return
    
    self.reversellRecursive(node.next)
    self.tail.next=node
    self.tail=node
    self.tail.next=None

if __name__ == '__main__':
  ll=LinkedList()
  # ll.insert_at_beg(5)
  # ll.insert_at_beg(89)
  # ll.insert_at_end(100)
  # data_lst=[1,2,3,4,5]
  # ll.insert_values(data_lst)
  # print(ll.lengthofLL())
  # ll.remove_at(4)
  # ll.insert_at(1,90)
  # ll.printop()
  # ll.reversell()
  # ll.printop()


  data_lst=[5,10,20,2,1]
  ll.insert_values(data_lst)
  print(ll.lengthofLL())
  ll.printop()
  # ll.reversell()
  # ll.printop()
  ll.reversellRecursive(ll.head)
  ll.printop()