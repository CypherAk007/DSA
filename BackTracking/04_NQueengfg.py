class Solution:
    def solveNQueens(self, n):
        board=[[False]*n for i in range(n)]
        # print(board)
        out=[]
        self.f(0,n,board,out)
        out.sort()
        return out 
    
    def f(self,r,n,board,out):
        # bc
        if r==n:
            # p rint(self.display(board))
            out.append(self.display(board))
            return 1 
        
        count=0
        for c in range(n):
            if self.check(r,c,board)==True:
                board[r][c]=True 
                count+=self.f(r+1,n,board,out)
                board[r][c]=False
        return count
        
    def display(self,board):
        n=len(board)
        lst=[]
        for j in range(n):
            for i in range(n):
                if board[i][j]==True:
                    lst.append(i+1)
            # print(lst)
        return lst
        
    def check(self,r,c,board):
        #up 
        for i in range(0,r):
            if board[i][c]==True:
                return False
                
        # left
        for j in range(min(r,c)+1):
            if board[r-j][c-j]==True:
                return False 
        
        # right
        for k in range(min(r,len(board)-(c+1))+1):
            if board[r-k][c+k]==True:
                return False
        
        return True 
        
        
                
    
        
        
        
s=Solution()
print(s.solveNQueens(4))