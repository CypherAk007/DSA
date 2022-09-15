def bfsOfGraphs(V,adj): #v ->No. of Nodes
  bfs=[]
  vis=[0]*(V)
  vis[0]=1
  q=[]
  q.append(0)
  while(q):
    node=q.pop(0)
    bfs.append(node)
    for i in adj[node]:
      if vis[i]==0:
        vis[i]=1
        q.append(i)
  return bfs 


adj=[[1,2,3],[0],[0,4],[0],[2]]
V=5
print(bfsOfGraphs(V,adj))
