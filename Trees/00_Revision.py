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


  def itrPreorder(self,root):
      preorder=[]
      if root==None:
          return preorder
      s=[]
      s.append(root)
      while(s):
          node=s.pop()
          preorder.append(node.data)
          if node.right!=None:
              s.append(node.right)
              
          if node.left!=None:
              s.append(node.left)
      print(preorder)

  def itrInorder(self,root):
    inorder=[]
    s=[]
    node=root 
    while True:
      if node!=None:
        s.append(node)
        node=node.left
      else:
        if len(s)==0:
          break
        node=s.pop()
        inorder.append(node.data)
        node=node.right
    print(inorder)

  def postOrderTraversal(self,root):
    s1=[]
    s2=[]
    postorder=[]
    if root==None:
      return postorder
    s1.append(root)
    while(len(s1)!=0):
      root=s1.pop()
      s2.append(root)
      if root.left!=None:
        s1.append(root.left)
      if root.right!=None:
        s1.append(root.right)
    while(len(s2)!=0):
      postorder.append(s2.pop().data)
    print(postorder)

  def AllInOneTraversal(self,root):
    s=[]
    s.append([root,1])
    pre=[]
    inorder=[]
    post=[]
    if root==None:
      return 
    while(len(s)!=0):
      val=s.pop()
      if val[1]==1:
        pre.append(val[0].data)
        val[1]+=1
        s.append(val)
        if val[0].left!=None:
          s.append([val[0].left,1])
      elif val[1]==2:
        inorder.append(val[0].data)
        val[1]+=1
        s.append(val)
        if val[0].right!=None:
          s.append([val[0].right,1])
      else:
        post.append(val[0].data)
    print(pre,inorder,post)

  def maxDepth(self,root):
    if root==None:
      return 0
    lh=self.maxDepth(root.left)
    rh=self.maxDepth(root.right)
    return 1+max(lh,rh)

  def checkB(self,root):
    if root==None:
      return 0
    lh=self.checkB(root.left)
    rh=self.checkB(root.right)
    if lh ==-1 or rh==-1:
      return -1 
    if abs(lh-rh)>1:
      return -1
    return 1+max(lh,rh)

  def findLongestpath(self,root):
    diameter=[-1]
    self.findpath(root,diameter)
    return diameter[0]
  def findpath(self,root,diameter):
    if root==None:
      return 0 
    lh=self.findpath(root.left,diameter)
    rh=self.findpath(root.right,diameter)
    diameter[0]=max(diameter[0],lh+rh)
    return 1+max(lh,rh)

  def maxPathSum(self,root):
    maxValue=[float('-inf')]
    self.maxPathDown(root,maxValue)
    return maxValue[0]

  def maxPathDown(self,root,maxValue):
    if root==None:
      return 0
    l=max(0,self.maxPathDown(root.left,maxValue))
    r=max(0,self.maxPathDown(root.right,maxValue))
    maxValue[0]=max(maxValue[0],l+r+root.data)
    return root.data+max(l,r)

if __name__=="__main__":
  root=Node(1)
  root.left=Node(2)
  root.left.left=Node(4)
  root.left.right=Node(5)
  root.right=Node(3)
  root.right.left=Node(6)
  root.right.right=Node(7)
  root.inorder(root)
  root.levelOrder(root)
  root.itrPreorder(root)
  root.itrInorder(root)
  root.postOrderTraversal(root)
  root.AllInOneTraversal(root)
  print(root.maxDepth(root))
  print(root.checkB(root))
  print(root.findLongestpath(root))
  print(root.maxPathSum(root))