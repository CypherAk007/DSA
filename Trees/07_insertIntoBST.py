class Node:
    def __init__(self,value):
        self.value = value
        self.left = None 
        self.right = None

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

        return node
bst = BST()
bst.insert(5)
bst.insert(4)
bst.insert(6)
bst.insert(3)
bst.display()
        