import math 
class SudokuSolver:
  # def main(self):
  #   pass 

  def solve(self,board):
    n=len(board)
    row=-1 
    col=-1 

    emptyleft=True 
    for i in range(0,n):
      for j in range(0,n):
        if board[i][j]==0:
          row=i 
          col=j
          emptyleft = False 
          break 
      if emptyleft==False:
        break 

    # sudoku is solved
    if emptyleft==True:
      return True 

    # backtrack
    for number in range(1,10):
      if self.isSafe(board,row,col,number):
        board[row][col]=number 
        if self.solve(board):
          # theboard is solved
          return True 
        else:
          # backtrack
          board[row][col]=0 
    return False 
  
  def display(self,board):
    for row in board:
      for num in row:
        print(num,end=' ')
      print()



  def isSafe(self,board,row,col,num):
    # check the row
    for i in range(len(board)):
      # check if the number is there in row or not
      if board[i][col]==num:
        return False
      
    # check for col
    for j in range(len(board)):
      # check if the number is there in col or not
      if board[row][j]==num:
        return False 
      
    # check for box
    sqrt=int(math.sqrt(len(board)))
    rowstart=row-(row%sqrt)
    colstart = col-(col%sqrt)
    
    for r in range(rowstart,rowstart+sqrt):
      for c in range(colstart,colstart+sqrt):
        if board[r][c]==num:
          return False 

    return True

  

s=SudokuSolver()
board=[[3, 0, 6, 5, 0, 8, 4, 0, 0],
[5, 2, 0, 0, 0, 0, 0, 0, 0],
[0, 8, 7, 0, 0, 0, 0, 3, 1],
[0, 0, 3, 0, 1, 0, 0, 8, 0],
[9, 0, 0, 8, 6, 3, 0, 0, 5],
[0, 5, 0, 0, 9, 0, 6, 0, 0], 
[1, 3, 0, 0, 0, 0, 2, 5, 0],
[0, 0, 0, 0, 0, 0, 0, 7, 4],
[0, 0, 5, 2, 0, 6, 3, 0, 0]]
x=s.solve(board)
print(x)
if s.solve(board):
  s.display(board)
else:
  print('Cant solve!!')