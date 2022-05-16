class Node:
  def __init__(self,data=None,nxt=None):
    self.data = data
    self.nxt = nxt

class LinkedList():
  def __init__(self):
    self.head=None
    self.tail = None

  def insert_at_end(self,data):
    node=Node(data,None)
    if self.head==None:
      self.head=node
      self.tail = node
      return
    self.tail.nxt=node
    self.tail =node

  def display(self):
    if self.head==None:
      print('LL is empty.')
      return
    itr = self.head
    llstr=''
    while itr:
      llstr+=str(itr.data)+' --> '
      itr=itr.nxt
    print(llstr)

  def merge(self,first,second):
    f=first.head
    s=second.head

    ans=LinkedList()
    while(f!=None and s!=None):
      if f.data<s.data:
        ans.insert_at_end(f.data)
        f=f.nxt

      else:
        ans.insert_at_end(s.data)
        s=s.nxt

    while f!=None:
      ans.insert_at_end(f.data)
      f=f.nxt

    while s!=None:
      ans.insert_at_end(s.data)
      s=s.nxt


    return ans



if __name__=="__main__":
  first=LinkedList()
  second = LinkedList()
  ans=LinkedList()

  first.insert_at_end(1)
  first.insert_at_end(3)
  first.insert_at_end(5)

  second.insert_at_end(1)
  second.insert_at_end(2)
  second.insert_at_end(9)
  second.insert_at_end(14)

  ans=ans.merge(first,second)
  ans.display()
    








