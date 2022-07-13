from traceback import print_tb


def allDirMazePathsPatterns(b,p,r,c,path,step):
  if r==len(b)-1 and c==len(b[0])-1:
    path[r][c]=step 

    for i in path:
      print(i)
    
    print(p)
    print('\n')
    return

  if b[r][c]==False:
    return

  # considering this cell in my path
  b[r][c]=False

  # considering this cell in my path and updating the path number
  path[r][c]=step

  if r<len(b)-1:
    allDirMazePathsPatterns(b,p+'D',r+1,c,path,step+1)
  
  if c<len(b[0])-1:
    allDirMazePathsPatterns(b,p+'R',r,c+1,path,step+1)
  
  if r>0:
    allDirMazePathsPatterns(b,p+'U',r-1,c,path,step+1)

  if c>0:
    allDirMazePathsPatterns(b,p+'L',r,c-1,path,step+1)

  # This line is where the funciton will be over so remove the changes masde
  b[r][c]=True
  path[r][c]=0


if __name__=='__main__':  
  board=[[True,True,True],[True,True,True],[True,True,True]]
  path=[]
  for i in range(len(board)):
    temp=[]
    for j in range(len(board[0])):
      temp.append(0)
    path.append(temp)
  print(path)
  step=1
  allDirMazePathsPatterns(board,"",0,0,path,step)