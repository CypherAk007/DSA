def checkBipartite(adj,n):
  color=[]`
  for i in range(n):
    color[i]=-1`

  for 





if __name__=='__main__':
  n=7
  adj=[]
  
  for i in range(0,n):
    adj.append([])

  adj[0].append(1)
  adj[1].append(0)

  adj[1].append(2)
  adj[2].append(1)

  adj[2].append(3)
  adj[3].append(2)

  adj[4].append(3)
  adj[3].append(4)

  adj[4].append(5)
  adj[5].append(4)

  adj[4].append(6)
  adj[6].append(4)

  adj[1].append(6)
  adj[6].append(1)

  print(adj)

  if checkBipartite(adj,n)==True:
    print('Yes Bipartite')
  else:
    print('Not Bipartite')
  
