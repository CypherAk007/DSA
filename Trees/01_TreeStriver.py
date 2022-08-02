class Node:
  def __init__(self,key) :
    self.data=key 
    self.left=None 
    self.right=None 

  def preorder(self,node):
    if node==None:
      return 
    print(node.data)
    self.preorder(node.left)
    self.preorder(node.right)

  def inorder(self,node):
    if node==None:
      return 
    self.inorder(node.left)
    print(node.data)
    self.inorder(node.right)
  
  def postorder(self,node):
    if node==None:
      return 
    self.postorder(node.left)
    self.postorder(node.right)
    print(node.data)

if __name__=='__main__':
  root=Node(1)
  root.left=Node(2)
  root.right=Node(3)
  root.left.left=Node(4)
  root.left.right=Node(5)
  root.right.left=Node(6)
  root.right.right=Node(7)

  # root.preorder(root)
  # root.inorder(root)
  root.postorder(root)