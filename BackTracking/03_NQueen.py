def queens(board,row):# no need to take column as parameter cause we start col fm 0 every time.
  if row==len(board):# this means all the queens have been placed.
    display(board)
    print('\n')
    return 1
  
  count=0
  # placing the queen and checking for every row and col
  for col in range(0,len(board)):
    # place the queen if it is safe
    if(isSafe(board,row,col)):
      board[row][col]=True  # new queen is placed here now
      # now chek if other queen can be placed in the below row
      count+=queens(board,row+1)
      # while returning back replace how it was (no queen - false)
      board[row][col]=False
  return count

def isSafe(board,row,col):
  # check for vertical row upwards
  for i in range(0,row):
    if board[i][col]: # if there is a queen in that row,col then its not safe to place it
      return False

  # diagonal left
  # max times we can go left is
  maxLeft=min(row,col)
  for i in range(1,maxLeft+1):
    # if board[row-i][col-i] is True then there is already a queen placed 
    if board[row-i][col-i]:
      return False

  # diagonal Right
  maxLRight=min(row,len(board)-col-1)
  for i in range(1,maxLRight+1):
    # if board[row-i][col-i] is True then there is already a queen placed 
    if board[row-i][col+i]:
      return False 

  # if none of the checks returns false then return true we can place it
  return True

def display(board):
  for row in board:
    for element in row:
      if element: # if True then queen is there at that loc
        print('Q',end=' ')
      else:
        print('X',end=' ')
    print('\n')


if __name__=='__main__':
  n=4
  board=[[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]]
  print(queens(board,0)) # prints the total no. of ways we can place a queen
