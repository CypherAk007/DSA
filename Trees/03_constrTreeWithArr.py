# Construct a complete binary tree from given array in level order fashion.
import collections


class Node:
  def __init__(self,key):
    self.data=key
    self.left=None
    self.right=None 

  def inorder(self,root):
    if root==None:
      return 
    self.inorder(root.left)
    print(root.data)
    self.inorder(root.right)

  def levelOrder(self,root):
    q=[]
    q.append(root)
    res=[]
    while q:
      qlen=len(q)
      temp=[]
      for i in range(qlen):
        val=q.pop(0)
        if val:
          temp.append(val.data)
        
          q.append(val.left)
        
          q.append(val.right)
      if temp:
        res.append(temp)
    print(res)
class Tree:
  # def __init__(self,arr) -> None:
  #   self.arr=arr

  def insertLevelOrder(self,arr,i,n):
    root = None
    if i<n:
      root = Node(arr[i])
      root.left=self.insertLevelOrder(arr,2*i+1,n)
      root.right = self.insertLevelOrder(arr,2*i+2,n)
    return root



if __name__=='__main__':
  root=Node(1)
  root.left=Node(2)
  root.right=Node(3)
  # root.inorder(root)
  # root.levelOrder(root)
  arr = [1, 2, 3, 4, 5, 6, 6, 6, 6]
  n = len(arr)
  node=Tree()
  rt=node.insertLevelOrder(arr,0,n)
  root.levelOrder(rt)

