def minTimeToBurn(self,root,start): #tc-O(n)-lvlorder +O(n)to burn the nodes
    parent_track={}
    target=self.bfsToMapParent(root,parent_track,start)
    mini=self.findMinDist(parent_track,target)
    return mini
    
def bfsToMapParent(self,root,parent_track,start):
    q=[]
    q.append(root)
    res=0 
    while(len(q)!=0):
        current=q.pop(0)
        if current.data==start:
            res=current
        if current.left:
            parent_track[current.left]=current
            q.append(current.left)
        if current.right:
            parent_track[current.right]=current
            q.append(current.right)
    return res

def findMinDist(self,parent_track,target):
    visited={}
    queue=[]
    queue.append(target)
    visited[target]=True
    time=0
    while len(queue)!=0:
        size=len(queue)
        flag=0 
        for i in range(size):
            current=queue.pop(0)
            if current.left!=None and current.left not in visited:
                queue.append(current.left)
                visited[current.left]=True
                flag=1 
            if current.right!=None and current.right not in visited:
                queue.append(current.right)
                visited[current.right]=True
                flag=1 
            if parent_track.get(current)!=None and parent_track.get(current) not in visited:
                queue.append(parent_track[current])
                visited[parent_track[current]]=True
                flag=1 
        if flag:
            time+=1 
    return time