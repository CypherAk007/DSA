class Node:
  def __init__(self,key):
    self.data=key 
    self.left=None 
    self.right=None 

  def search(self,root,t):
    while(root!=None and root.data!=t):
      if t>root.data:
        root=root.right
      else:
        root=root.left
    return root 
  def inorder(self,root):
    if root==None:
      return []
    lst=[]
    lst.append(root.data)
    lst+=self.inorder(root.left)
    lst+=self.inorder(root.right)
    return lst 

  def ceil(self,root,k):
    ceil=-1
    while(root):
      if root.data==k:
        ceil=root.data 
        return ceil
      if root.data<k:
        root=root.right 
      else:
        ceil=root.data 
        root=root.left
    return ceil 

  def floor(self,root,k):
    floor=-1
    while(root):
      if root.data==k:
        floor=root.data 
        return floor
      if root.data<k:
        floor=root.data 
        root=root.right 
      else:
        root=root.left
    return floor 

  def InsertNode(self,root,val):
    if root==None:
      return Node(val)
    cur=root 
    while(True):
      if cur.data<=val:
        if cur.right:
          cur=cur.right
        else:
          cur.right=Node(val)
          break
      else:
        if cur.left:
          cur=cur.left
        else:
          cur.left=Node(val)
          break
    return root
        

if __name__=='__main__':
  rt=Node(8)
  rt.left=Node(3)
  rt.left.left=Node(1)
  rt.left.right=Node(6)
  rt.left.right.left=Node(4)
  rt.left.right.right=Node(7)
  rt.right=Node(10)
  rt.right.right=Node(14)
  rt.right.right.left=Node(13)
  print(rt.inorder(rt))
  print(rt.search(rt,10).data)
  print(rt.ceil(rt,5))
  print(rt.floor(rt,5))
  print(rt.InsertNode(rt,11))
  print(rt.inorder(rt))