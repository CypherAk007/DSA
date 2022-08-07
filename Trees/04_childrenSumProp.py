def changeTree(self,root):
        if root==None:
            return  
        child=0 #root.left+right 
        if root.left:
            child+=root.left.data 
        if root.right:
            child+=root.right.data 
        if child>= root.data:#roots value is updated 
            root.data=child 
        else:
            if root.left:
                root.left.data=root.data
            elif root.right:
                root.right.data=root.data 
        
        self.changeTree(root.left)
        self.changeTree(root.right)
        
        # when we go back we assign the root with sum of left and right
        tot=0 
        if root.left!=None:
            tot+=root.left.data 
        if root.right!=None:
            tot+=root.right.data 
        if root.left!=None or root.right!=None:#if not leaf node
            root.data = tot 