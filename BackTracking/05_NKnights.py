class Solution:

  def main(self):
    n=4 
    board=[[False]*n for i in range(n)]
    return self.knights(board,0,0,n)

  def display(self,board):
    for row in board:
      for element in row:
        if element: # if True then queen is there at that loc
          print('K',end=' ')
        else:
          print('X',end=' ')
      print('\n')

  def knights(self,board,row,col,knights):
    # bc
    if knights ==0:
      self.display(board)
      print()
      return 1
    
    if row==len(board)-1 and col==len(board):
      return 0

    if col==len(board):
      self.knights(board,row+1,0,knights)
      return 0

    count=0
    if self.issafe(board,row,col):
      board[row][col]=True
      count+=self.knights(board,row,col+1,knights-1)
      board[row][col]=False 
      
    count+=self.knights(board,row,col+1,knights)
    return count 

  def issafe(self,board,row,col):
    if self.isvalid(board,row-2,col-1):
      if board[row-2][col-1]:
        return False 
    if self.isvalid(board,row-1,col-2):
      if board[row-1][col-2]:
        return False 
    if self.isvalid(board,row-2,col+1):
      if board[row-2][col+1]:
        return False 
    if self.isvalid(board,row-1,col+2):
      if board[row-1][col+2]:
        return False 
    return True 



  def isvalid(self,board,row,col):
    if row>=0 and row<len(board) and col>=0 and col<len(board):
      return True 
    return False 

s=Solution()
print(s.main())

    