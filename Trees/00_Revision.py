import math
class Node:
    def __init__(self,key):
        self.data = key
        self.left = None
        self.right = None
        self.prev=None
        
    def levelOrder(self,root):
        q=[]
        res=[]
        q.append(root)
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
        return res 
        
    def preorder(self,root):
        if root==None:
            return []
        lst=[]
        lst.append(root.data)
        lst+=self.preorder(root.left)
        lst+=self.preorder(root.right)
        return lst
        
        
    def inorder(self,root):
        if root==None:
            return []
        lst=[]
        lst+=self.inorder(root.left)
        lst.append(root.data)
        lst+=self.inorder(root.right)
        return lst
        
    def postorder(self,root):
        if root==None:
            return []
        lst=[]
        lst+=self.postorder(root.left)
        lst+=self.postorder(root.right)
        lst.append(root.data)
        return lst    
        
    def itrPre(self,root):
        pre=[]
        s=[]
        s.append(root)
        while(len(s)!=0):
            val=s.pop()
            if val:
                pre.append(val.data)
                s.append(val.right)
                s.append(val.left)
        return pre
        
    def itrIn(self,root):
        s=[]
        node=root
        res=[]
        while True:
            if node:
                s.append(node)
                node=node.left
            else:
                if len(s)==0:
                    break
                node=s.pop()
                
                res.append(node.data)
                node=node.right
        return res
                
    def itrPost(self,root):
        s1=[]
        s2=[]
        res=[]
        s1.append(root)
        
        while s1:
            val=s1.pop()
            if val:
                s2.append(val.data)
                s1.append(val.left)
                s1.append(val.right)
                
        while s2:
            val=s2.pop()
            if val:
                res.append(val)
        return res 
            
    def allTraversal(self,root):
        pre=[]
        ino=[]
        post=[]
        s=[]
        s.append([root,1])
        while s:
            val=s.pop()
            if val[1]==1:
                pre.append(val[0].data)
                s.append([val[0],val[1]+1])
                if val[0].left:
                    s.append([val[0].left,1])
            elif val[1]==2:
                ino.append(val[0].data)
                s.append([val[0],val[1]+1])
                if val[0].right:
                    s.append([val[0].right,1])    
            else:
                post.append(val[0].data)
        print(pre)
        print(ino)
        print(post)
        
    def height(self,root):
        if root==None:
            return 0 
        lh=self.height(root.left)
        rh=self.height(root.right)
        return 1+max(lh,rh)
        
    def balance(self,root):
        if root==None:
            return 0 
        lh=self.height(root.left)
        rh=self.height(root.right)
        if lh==-1 or rh==-1:
            return -1
        if abs(lh-rh)>1:
            return -1 

        return 1+max(lh,rh)
        
    def checkDiameter(self,root):
        dia=[0]
        self.diameter(root,dia)
        return dia[0]
    def diameter(self,root,dia):
        if root==None:
            return 0 
            
        lh=self.height(root.left)
        rh=self.height(root.right)
        dia[0]=max(dia[0],lh+rh)
        return 1+max(lh,rh)
    
    def mps(self,root):
        s=[0]
        self.ps(root,s)
        return s[0]
    def ps(self,root,s):
        if root==None:
            return 0 
            
        lh=max(0,self.height(root.left))
        rh=max(0,self.height(root.right))
        
        s[0]=max(s[0],root.data+lh+rh)
        
        return root.data+max(lh,rh)
        
    def checkIde(self,p,q):
        if p==None or q==None:
            return p==q 
        return p.data==q.data and self.checkIde(p.left,q.left) and self.checkIde(p.right,q.right)
    
    def BoundryTraversal(self,root):
        res=[]
        if root==None:
            return res 
        self.addLeft(root,res)
        self.addLeaf(root,res)
        self.addRight(root,res)
        return res 
    def addLeft(self,root,res):
        cur=root.left
        while(cur!=None):
            if self.checkLeaf(root)==False:
                res.append(cur.data)
            if cur.left!=None:
                cur=cur.left
            else:
                cur=cur.right
    def addRight(self,root,res):
        cur= root.right 
        s=[]
        while(cur!=None):
            if self.checkLeaf(root)==False:
                s.append(cur.data)
            if cur.right!=None:
                cur=cur.right
            else:
                cur=cur.left 
        for i in range(len(s)-1,-1,-1):
            res.append(s[i])
    def addLeaf(self,root,res):
        if self.checkLeaf(root)==True:
            res.append(root.data)
            return
        if root.left!=None:
            self.addLeaf(root.left,res)
        if root.right!=None:
            self.addLeaf(root.right,res)
            
    def checkLeaf(self,root):
        if root.left==None and root.right==None:
            return True
        else:
            return False
    
    def insertLevelOrder(self,arr,i,n):
        root=None
        if i<n:
            root=Node(arr[i])
            root.left=self.insertLevelOrder(arr,2*i+1,n)
            root.right=self.insertLevelOrder(arr,2*i+2,n)
        return root
        
    def verticalOrder(self,root):
        d={}
        q=[]
        q.append((root,0,0))#rt,v,l
        while q:
            val=q.pop(0)
            if val:
                if d.get(val[1])==None:
                    d[val[1]]={}
                if d[val[1]].get(val[2])==None:
                    d[val[1]][val[2]]=[]
                
                d[val[1]][val[2]].append(val[0].data)
            if val[0].left:
                q.append((val[0].left,val[1]-1,val[2]+1))
            if val[0].right:
                q.append((val[0].right,val[1]+1,val[2]+1))
        print(d)
        out=[]
        for i in sorted(d):
            col=[]
            for j in d[i]:
                col+=d[i][j]
            out.append(col)
        print(out)
    
    def checkSym(self,root):
        return root==None or self.sym(root.left,root.right)
    
    def sym(self,left,right):
        if left==None or right==None:
            return left==right
        # if left.data!=right.data:
        #     return False
        return left.data==right.data and self.sym(left.left,right.right) and self.sym(left.right,right,left)
            
    def topView(self,root):
        q=[]
        q.append([root,0])
        res= []
        d={}
        while(q):
            val=q.pop(0)
            if val[1] not in d:
                d[val[1]]=val[0]
            if val[0].left:
                q.append([val[0].left,val[1]-1])
            if val[0].right:
                q.append([val[0].right,val[1]+1])
        
        for i in sorted(d):
            res.append(d[i].data)
        return res
        
    def bottomView(self,root):
        q=[]
        q.append([root,0])
        res= []
        d={}
        while(q):
            val=q.pop(0)
            d[val[1]]=val[0]
            if val[0].left:
                q.append([val[0].left,val[1]-1])
            if val[0].right:
                q.append([val[0].right,val[1]+1])
        
        for i in sorted(d):
            res.append(d[i].data)
        return res
        
    def rv(self,root):
        q=[]
        res=[]
        self.rightView(root,0,q)
        for i in q:
            res.append(i.data)
        return res
    def rightView(self,root,level,q):
        if root==None:
            return 
        if level==len(q):
            q.append(root)
        self.rightView(root.right,level+1,q)
        self.rightView(root.left,level+1,q)
    
    def rton(self,A,B):
        a=[]
        if A==None:
            return a 
        self.getPath(A,a,B)
        return a 
    def getPath(self,root,a,node):
        if root==None:
            return False 
        a.append(root.data)
        if root.data==node:
            return True 
        if self.getPath(root.left,a,node) or self.getPath(root.right,a,node):
            return True 
        a.pop()
        return False
        
    def lca(self,root,p,q):
        if root==None or root.data==p or root.data==q:
            return root 
        
        left=self.lca(root.left,p,q)
        right=self.lca(root.right,p,q)
        
        if left==None:
            return right
        elif right==None:
            return left 
        else:
            return root
            
    def widthOfBT(self,root):
        if root==None:
            return 0 
        ans=0 
        q=[]
        q.append([root,0])
        while(len(q)!=0):
            size=len(q)
            mini=q[0][1]
            first=0 
            last=0 
            for i in range(size):
                val=q.pop(0)
                cur_id=val[1]-mini
                node=val[0]
                if i==0:
                    first=cur_id
                if i==size-1:
                    last=cur_id
                if node.left!=None:
                    q.append([node.left,cur_id*2+1])
                if node.right!=None:
                    q.append([node.right,cur_id*2+2])
            ans=max(ans,last-first+1)
        return ans
        
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
                    if val.left:
                        q.append(val.left)
                    if val.right:
                        q.append(val.right)
            if temp:
                res.append(temp)
        return res 

    def kNodesDist(self,root,t,k):
        parent={}
        self.findParent(root,parent)
        # print(parent)
        # do lvl/bfs
        res=[]
        visited={}
        q=[]
        z=self.findNode(root,t)
        q.append(z)
        # print(q)
        visited[z]=True
        lvl=0
        while len(q)!=0:
            if lvl==k:
                break
            qlen=len(q)
            # print(qlen)
            lvl+=1
            # print(lvl)
            for i in range(qlen):
                val=q.pop(0)
    
                if val.left!=None and val.left not in visited:
                    q.append(val.left)
                    visited[val.left]=True
                if val.right!=None and val.right not in visited:
                    q.append(val.right)
                    visited[val.right]=True
                if parent.get(val)!=None and parent.get(val) not in visited:
                    q.append(parent.get(val))
                    visited[parent.get(val)]=True 
                print(visited)   
        while q:       
            x=q.pop(0).data
            # print(x)
            res.append(x)
        return res
        
        
    def findParent(self,root,parent):
        # lvlorder
        q=[]
        q.append(root)
        while q:
            val=q.pop(0)
            if val.left:
                parent[val.left]=val
                q.append(val.left)
            if val.right:
                parent[val.right]=val
                q.append(val.right)
                
    def findNode(self,root,t):
        if root==None or root.data==t:
            return root
        return self.findNode(root.left,t)
        return self.findNode(root.right,t)
        
    def BurnTree(self,root,t,k):
        parent={}
        self.findParent(root,parent)
        # print(parent)
        # do lvl/bfs
        res=[]
        visited={}
        q=[]
        z=self.findNode(root,t)
        q.append(z)
        # print(q)
        visited[z]=True
        lvl=0
        while len(q)!=0:
            flag=0
            qlen=len(q)
            # print(qlen)
            
            # print(lvl,q)
            # print(lvl)
            for i in range(qlen):
                val=q.pop(0)
    
                if val.left!=None and val.left not in visited:
                    q.append(val.left)
                    visited[val.left]=True
                    flag=1
                if val.right!=None and val.right not in visited:
                    q.append(val.right)
                    visited[val.right]=True
                    flag=1
                if parent.get(val)!=None and parent.get(val) not in visited:
                    q.append(parent.get(val))
                    visited[parent.get(val)]=True 
                    flag=1
                # print(visited)   
            if flag:
                lvl+=1
        return lvl
        
    def countNodes(self,root):
        # lh==rh then 2^lh-1
        # else 1+lh+rh
        if root==None:
            return 0 
        lh=self.getleftheight(root)
        rh=self.getrightheight(root)
        if lh==rh:
            return int(math.pow(2,lh)-1)
        else:
            return 1+self.countNodes(root.left)+self.countNodes(root.right)
    def getleftheight(self,root):
        count=0
        while(root!=None):
            count+=1 
            root=root.left 
        return count 
    def getrightheight(self,root):
        count=0
        while(root!=None):
            count+=1 
            root=root.right 
        return count 
    
    def buildTreepre(self,pre,ino):
        inmap={}
        for i in range(len(ino)):
            inmap[ino[i]]=i
        root=self.helperpre(pre,0,len(pre)-1,ino,0,len(ino)-1,inmap)
        root2=self.helperpost(pre,0,len(pre)-1,ino,0,len(ino)-1,inmap)
        # print(root)
        # print(root2)
        return root
    def buildTreepost(self,pre,ino):
        inmap={}
        for i in range(len(ino)):
            inmap[ino[i]]=i
        root=self.helperpre(pre,0,len(pre)-1,ino,0,len(ino)-1,inmap)
        root2=self.helperpost(pre,0,len(pre)-1,ino,0,len(ino)-1,inmap)
        # print(root)
        # print(root2)
        return root2
    def helperpre(self,pre,prestart,preend,ino,instart,inend,inmap):
        if prestart>preend or instart>inend:
            return None
        root=Node(pre[prestart])
        idxroot=inmap[root.data]
        numsLeft=idxroot-instart
        root.left=self.helperpre(pre,prestart+1,prestart+numsLeft,ino,instart,idxroot-1,inmap)
        root.right=self.helperpre(pre,prestart+numsLeft+1,preend,ino,idxroot+1,inend,inmap)
        return root 
    def helperpost(self,pre,prestart,preend,ino,instart,inend,inmap):
        if prestart>preend or instart>inend:
            return None
        root=Node(pre[preend])
        idxroot=inmap[root.data]
        numsLeft=idxroot-instart
        root.left=self.helperpost(pre,prestart,prestart+numsLeft-1,ino,instart,idxroot-1,inmap)
        root.right=self.helperpost(pre,prestart+numsLeft,preend-1,ino,idxroot+1,inend,inmap)
        return root 
    
    def morisTra(self,root):
        inorder=[]
        cur=root
        while(cur!=None):
            # noleft
            if cur.left==None:
                inorder.append(cur.data)
                cur=cur.right 
            else:
                prev=cur.left 
                while(prev.right and prev.right!=cur ):
                    prev=prev.right 
                if prev.right==None:
                    prev.right=cur 
                    cur=cur.left 
                else:
                    prev.right=None
                    inorder.append(cur.data)
                    cur=cur.right 
        return inorder   
    def flatternbt(self,root):
        # print(root.prev)
        if root==None:
            return 
        self.flatternbt(root.right)
        self.flatternbt(root.left)
        root.right=self.prev
        root.left=None 
        self.prev=root 

        def levelOrder(self,root):
        q=[]
        q.append(root)
        res=[]
        while q:
            qlen=len(q)
            temp=[]
            for i in range(qlen):
                val=q.pop(0)
                temp.append(val.data)
                if val.left:
                    q.append(val.left)
                if val.right:
                    q.append(val.right)
                    
            res.append(temp)
        return res 

    def delete(self,root,key):
        if root==None:
            return None 
        if root.data==key:#root
            return self.helper(root)
        dummy=root
        while(root!=None):
            if root.data>key:
                if root.left!=None and root.left.data==key:
                    root.left=self.helper(root.left)
                    break
                else:
                    root=root.left
            else:
                if root.right!=None and root.right.data==key:
                    root.right=self.helper(root.right)
                    break
                else:
                    root=root.right 
        return dummy
        
    def helper(self,root):
        if root.left==None:
            return root.right 
        if root.right==None:
            return root.left 
        rchild=root.right 
        lastrchild=self.findLright(root.left)
        lastrchild.left=rchild
        return root.left
        
    def findLright(self,root):
        if root.right==None:
            return root 
        self.findLright(root.right)
        
    def validBst(self,root):
        return self.isValid(root,float('-inf'),float('inf'))
    
    def isValid(self,root,minval,maxval):
        if root==None:
            return True 
        if root.data>=maxval or root.data<=minval:
            return False
        return self.isValid(root.left,minval,root.data) and self.isValid(root.right,root.data,maxval)
        
    def lcaBt(self,root,p,q):
        if root==None:
            return None
        cur=root.data
        if p.data>cur and q.data>cur:
            return self.lcaBt(root.right,p,q)
        if p.data<cur and q.data<cur:
            return self.lcaBt(root.left,p,q)
        return root
        
       
    def bstPreorder(self,preorder):
        return self.helperp(preorder,float('inf'),[0])
    def helperp(self,preorder,bound,i):
        if i[0]==len(preorder) or preorder[i[0]]>bound:
            return None 
        root=Node(preorder[i[0]])
        i[0]+=1 
        root.left=self.helperp(preorder,root.data,i)
        root.right=self.helperp(preorder,bound,i)
        return root
        
    def inorderSuccssor(self,root,t):
        succsor=None 
        while(root!=None):
            if t>root.data:
                root=root.right
            else:
                succsor=root.data
                root=root.left
        return succsor
        
    def bstItrator(self,root):
        def __init__(self,root):
            self.s=[]
            self.pushAll(root)
        
        def pushAll(self,root):
            while(root!=None):
                self.s.append(root)
                root=root.left
        
        def Next(self):
            x=self.s.pop()
            self.pushAll(x.right)
            return x.data
        
        def hasNext(self):
            if len(s)!=0:
                return True
            else:
                return False

if __name__=='__main__':
    rt=Node(1)
    rt.left=Node(2)
    rt.left.left=Node(3)
    rt.left.left.right=Node(4)
    rt.left.left.right.left=Node(5)
    rt.left.left.right.right=Node(6)
    rt.right=Node(7)
    rt.right.right=Node(8)
    rt.right.right.left = Node(9)
    rt.right.right.left.left=Node(10)
    rt.right.right.left.right = Node(11)
    print(rt.preorder(rt))
    print(rt.inorder(rt))
    print(rt.postorder(rt))
    print(rt.levelOrder(rt))
    print(rt.itrPre(rt))
    print(rt.itrIn(rt))
    print(rt.itrPost(rt))
    rt.allTraversal(rt)
    print(rt.height(rt))
    print(rt.balance(rt))
    print(rt.checkDiameter(rt))
    print(rt.mps(rt))
    print(rt.checkIde(rt,rt))
    print(rt.BoundryTraversal(rt))
    arr=[1,2,3,4,5,6,6,6,6]
    print(rt.levelOrder(rt.insertLevelOrder(arr,0,len(arr))))
    # rt.verticalOrder(rt)
    # print(rt.sym(rt.left,rt.right))
    # print(rt.topView(rt))
    # print(rt.bottomView(rt))
    # print(rt.rv(rt))
    # print(rt.rton(rt,4))
    # print(rt.lca(rt,5,11).data)
    # print(rt.widthOfBT(rt))
    # print(rt.levelOrder(rt))
    # print(rt.changeTree(rt))
    # print(rt.levelOrder(rt))