def allDirMazePaths(b,p,r,c):
  if r==len(b)-1 and c==len(b[0])-1:
    print(p)
    return
  if b[r][c]==False:
    return

  # considering this cell in my path
  b[r][c]=False

  if r<len(b)-1:
    allDirMazePaths(b,p+'D',r+1,c)
  
  if c<len(b[0])-1:
    allDirMazePaths(b,p+'R',r,c+1)
  
  if r>0:
    allDirMazePaths(b,p+'U',r-1,c)

  if c>0:
    allDirMazePaths(b,p+'L',r,c-1)

  # This line is where the funciton will be over so remove the changes masde
  b[r][c]=True

board=[[True,True,True],[True,True,True],[True,True,True]]
allDirMazePaths(board,"",0,0)