def allDirMaze(p,maze,r,c):
  if r==len(maze)-1 and c==len(maze[0])-1:
    print(p)
    return
  
  if maze[r][c]==False:
    return
  
  maze[r][c]=False

  if r<len(maze)-1:
    allDirMaze(p+'D',maze,r+1,c)

  if c<len(maze[0])-1:
    allDirMaze(p+'R',maze,r,c+1)

  if r>0:
    allDirMaze(p+'U',maze,r-1,c)

  if c>0:
    allDirMaze(p+'L',maze,r,c-1)

  maze[r][c]=True


def allDirMazeStep(p,maze,path,step,r,c):
  if r==len(maze)-1 and c==len(maze[0])-1:
    print(p)
    path[r][c]=step
    for i in path:
      print(i)
    print('\n')
    return
  
  if maze[r][c]==False:
    return
  
  maze[r][c]=False
  path[r][c]=step

  if r<len(maze)-1:
    allDirMazeStep(p+'D',maze,path,step+1,r+1,c)

  if c<len(maze[0])-1:
    allDirMazeStep(p+'R',maze,path,step+1,r,c+1)

  if r>0:
    allDirMazeStep(p+'U',maze,path,step+1,r-1,c)

  if c>0:
    allDirMazeStep(p+'L',maze,path,step+1,r,c-1)

  path[r][c]=0
  maze[r][c]=True



# p=''
# maze=[[True,True,True],
#       [True,True,True],
#       [True,True,True]]
# allDirMaze(p,maze,0,0)
  
p=''
maze=[[True,True,True],
      [True,True,True],
      [True,True,True]]
step=1
path=[[0,0,0],
      [0,0,0],
      [0,0,0]]
allDirMazeStep(p,maze,path,step,0,0)
