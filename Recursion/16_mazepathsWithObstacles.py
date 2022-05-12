def pathRestrictions(p,maze,r,c):
    if r==len(maze)-1 and c==len(maze[0])-1:
        print(p)
        return
    
    if maze[r][c]==False:
        return
    
    if r<len(maze)-1:
        pathRestrictions(p+'D',maze,r+1,c)
        
    if c<len(maze[0])-1:
        pathRestrictions(p+'R',maze,r,c+1)
        
    
board=[[True,True,True],
        [True,False,True],
        [True,True,True]]
        
        
pathRestrictions('',board,0,0)