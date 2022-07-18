import math 

def solve(board):#solve the sudoku
  n=len(board)
  row=-1
  col=-1
# if we get an empty element
  emptyLeft=True
  # this is how we are replacing the r,c in the arg
  for i in range(n):
    for j in range(n):
      if board[i][j]==0:
        row=i
        col=j
        emptyLeft=False
        break
    # if u found some empty element in row,then break
    if emptyLeft==False:
      break 

  # if sudoku is solved
  if emptyLeft==True:
    return True
  
  for number in range(1,10):
    if isSafe(board,row,col,number):
      board[row][col]=number 
      if solve(board):
        # found the ans
        return True
      else:
        # backtrack
        board[row][col]=0
  return False

def display(board):
  for row in board:
    for num in row:
      print(num+" ")
    print()

def isSafe(board,row,col,num):
  # check the row
  for i in range(len(board)):
    if board[row][i] == num:
      return False 

  # check for the col
  for nums in board:
    if nums[col]==num:
      return False

  # check for the square matrix
  sqrt=int(math.sqrt(len(board)))
  rowStart=row-row%sqrt 
  colStart = col - col % sqrt 
  for r in range(rowStart,rowStart+sqrt):
    for c in range(colStart,colStart+sqrt):
      if board[r][c]==num:
        return False 
  return True 