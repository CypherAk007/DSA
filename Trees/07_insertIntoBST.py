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

bst = BST()
arr=[3,4,5,2,6,1,7]
bst.populate(arr)
bst.display()


'''
output
Root Node : 3
LeftChildOf 3: 2
LeftChildOf 2: 1
RightChildOf 3: 4
RightChildOf 4: 5
RightChildOf 5: 6
RightChildOf 6: 7

'''
