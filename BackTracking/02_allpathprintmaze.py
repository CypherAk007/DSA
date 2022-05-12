def allPathPrint(p,maze,r,c,path,step):
    if r==len(maze)-1 and c==len(maze[0])-1:
        path[r][c]=step
        for i in path:
          print(i)
        print(p)
        print('\n')
        return
    
    if (maze[r][c]==False):
        return
    
    maze[r][c]=False
    path[r][c]=step

    if r<len(maze)-1:
        allPathPrint(p+'D',maze,r+1,c,path,step+1)
        
    if c<len(maze[0])-1:
        allPathPrint(p+'R',maze,r,c+1,path,step+1)
        
    if r>0:
        allPathPrint(p+'U',maze,r-1,c,path,step+1)
        
    if c>0:
        allPathPrint(p+'L',maze,r,c-1,path,step+1)
        
    maze[r][c]=True
    path[r][c]=0 
    
    
board=[[True,True,True],
        [True,True,True],
        [True,True,True]]

# path=[[0]*len(board)]*len(board[0])

path=[[0,0,0],
      [0,0,0],
      [0,0,0]]
# for i in range(0,len(board)):
#     path.append([0]*len(board[0]))

print(path)
allPathPrint('',board,0,0,path,1)