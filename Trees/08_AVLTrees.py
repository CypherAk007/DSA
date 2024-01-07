class Node:
    def __init__(self,value):
        self.value = value
        self.left = None 
        self.right = None
        self.height = 0

class AVL:
    def __init__(self) -> None:
        self.root = None 

    def display(self):
        self.displayIntenal(self.root,"Root Node : ")

    def displayIntenal(self,node,details):
        if node == None:
            # print("None")
            return 
        print(details+str(node.value))
        self.displayIntenal(node.left,"LeftChildOf "+str(node.value)+": ") 
        self.displayIntenal(node.right,"RightChildOf "+str(node.value)+": ")

    def height(self,node):
        if node==None:
            return -1
        return node.height
    
    def balanced(self):
        return self.balancedInternal(self.root)
    
    def balancedInternal(self,node):
        if node==None:
            return True 
        return abs(self.height(node.left)-self.height(node.right))<=1 and self.balancedInternal(node.left) and self.balancedInternal(node.right)
    

    def insert(self,value):
        self.root = self.insertInternal(value,self.root)

    def insertInternal(self,value,node):
        if node == None:
            node = Node(value)
            return node 
        
        if value<node.value:
            node.left = self.insertInternal(value,node.left)

        if value>=node.value:
            node.right = self.insertInternal(value,node.right)

        node.height = max(self.height(node.left),self.height(node.right))+1

        # Only for the one case where the subtree is unbalanced -> it will balance and return it 
        return self.rotate(node) #fixes the structure of tree and return node
    
    #used to insert to tree from array
    def populate(self,arr):
        for i in range(len(arr)):
            self.insert(arr[i])

    #used to insert to tree from array (avoid skew tree)
    # TC => O(N* Log(N))
    def populateSorted(self,arr):
        self.populateSortedInternal(arr,0,len(arr)-1)
    
    def populateSortedInternal(self,arr,lo,hi):
        if lo>hi:
            return 
        mid = (lo+hi)//2
        self.insert(arr[mid]) #Log(N)
        self.populateSortedInternal(arr,lo,mid-1)
        self.populateSortedInternal(arr,mid+1,hi)

    def preorder(self):
        self.preorderInternal(self.root)

    def preorderInternal(self,node):
        if node==None:
            return 
        print(node.value)
        self.preorderInternal(node.left)
        self.preorderInternal(node.right)

    def inorder(self):
        self.inorderInternal(self.root)

    def inorderInternal(self,node):
        if node==None:
            return 
        self.inorderInternal(node.left)
        print(node.value)
        self.inorderInternal(node.right)

    def postorder(self):
        self.postorderInternal(self.root)

    def postorderInternal(self,node):
        if node==None:
            return 
        self.postorderInternal(node.left)
        self.postorderInternal(node.right)
        print(node.value)
    
    def rotate(self,node):
        if self.height(node.left) - self.height(node.right)>1:
            # left heavy
            if self.height(node.left.left)-self.height(node.left.right)>0:
                # Left Left case 
                return self.rightRotate(node)
            if self.height(node.left.left)-self.height(node.left.right)<0:
                # Left Right case (Right tree is greater than left)

                # 1-> left rotate child Left-Right becomes Left-Left
                node.left = self.leftRotate(node.left)
                # 2-> Right rotate parent as its Left-Left now
                return self.rightRotate(node)
            
        if self.height(node.left) - self.height(node.right)<-1:
            # Right heavy
            if self.height(node.right.left)-self.height(node.right.right)<0:
                # Right Right case 
                return self.leftRotate(node)
            if self.height(node.right.left)-self.height(node.right.right)>0:
                # Right Left case (Left tree is greater than right)

                # 1-> right rotate child Right-Left becomes right-right
                node.right = self.rightRotate(node.right)
                # 2-> left rotate parent as its Right-Right now
                return self.leftRotate(node)
            

        return node
    
    def rightRotate(self,p):
         # Reffer Diag 
        c = p.left
        t=c.right

        c.right = p 
        p.left = t 

        # update the heights as tree is rotated
        p.height = max(self.height(p.left),self.height(p.right))+1
        c.height = max(self.height(c.left),self.height(c.right))+1

        return c 

    def leftRotate(self,c):
        # Reffer Diag 
        p = c.right
        t = p.left

        p.left = c
        c.right = t

        # update the heights as tree is rotated
        p.height = max(self.height(p.left),self.height(p.right))+1
        c.height = max(self.height(c.left),self.height(c.right))+1

        return p

    # def leftRotate(self,p):
    #     # Reffer Diag 
    #     c = p.right
    #     t=c.left

    #     c.left = p 
    #     p.right = t 

    #     # update the heights as tree is rotated
    #     p.height = max(self.height(p.left),self.height(p.right))+1
    #     c.height = max(self.height(c.left),self.height(c.right))+1

    #     return c 
        
    
avl = AVL()
# arr=[1,2,3,4,5,6]
# bst.populate(arr)
# bst.display()
# # bst.preorder()
# # bst.inorder()
# bst.postorder()
for i in range(1,1001):
    avl.insert(i)
# avl.display()
# avl.inorder()
print(avl.height(avl.root))
