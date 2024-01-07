class Node:
    def __init__(self,value):
        self.value = value
        self.left = None 
        self.right = None
        self.height = 0

class BST:
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

        return node
    
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
    


bst = BST()
arr=[1,2,3,4,5,6]
bst.populateSorted(arr)
bst.display()
# bst.preorder()
# bst.inorder()
bst.postorder()
