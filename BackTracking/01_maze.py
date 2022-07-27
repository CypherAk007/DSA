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
    
from copy import copy   
# ans in the form of list of lists
def allDir(temp,ans,maze,r,c):
    if r==len(maze)-1 and c==len(maze[0])-1:
        ans.append(copy(temp))
        return 
    
    if maze[r][c]==False:
        return
    
    maze[r][c]=False
    if r<len(maze)-1:
        temp.append('D')
        allDir(temp,ans,maze,r+1,c)
        temp.pop()
    if c<len(maze[0])-1:
        temp.append('R')
        allDir(temp,ans,maze,r,c+1)
        temp.pop()
    if r>0:
        temp.append('U')
        allDir(temp,ans,maze,r-1,c)
        temp.pop()
    if c>0:
        temp.append('L')
        allDir(temp,ans,maze,r,c-1)
        temp.pop()
    maze[r][c]=True
    


board=[[True,True,True],
        [True,True,True],
        [True,True,True]]
allDirBackTrack('',board,0,0)