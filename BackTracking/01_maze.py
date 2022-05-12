def allDirBackTrack(p,maze,r,c):
    if r==len(maze)-1 and c==len(maze[0])-1:
        print(p)
        return
    
    if (maze[r][c]==False):
        return
    
    maze[r][c]=False
    if r<len(maze)-1:
        allDirBackTrack(p+'D',maze,r+1,c)
        
    if c<len(maze[0])-1:
        allDirBackTrack(p+'R',maze,r,c+1)
        
    if r>0:
        allDirBackTrack(p+'U',maze,r-1,c)
        
    if c>0:
        allDirBackTrack(p+'L',maze,r,c-1)
        
    maze[r][c]=True
    
    
board=[[True,True,True],
        [True,True,True],
        [True,True,True]]
allDirBackTrack('',board,0,0)