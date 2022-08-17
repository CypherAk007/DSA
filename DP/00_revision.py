from copy import copy

def stairs(t,p,res):
    if t==0:
        res.append(p)
        return 
    for i in range(1,t+1):
        if i<=t:
            stairs(t-i,p+str(i),res)
           
class climb:            
    def stairsCombi(self,t):
        candidates=[]
        for i in range(1,t+1):
            candidates.append(i)
        print(candidates)
        temp=[]
        res=[]
        self.stairshelper(t,temp,res,0,candidates)
        return res
        
    def stairshelper(self,target,temp,res,i,candidates):
        if target==0:
            res.append(copy(temp))
            return
        if target<0:
            return 
        if i==len(candidates):
            return 
        self.stairshelper(target,temp,res,i+1,candidates)
        
        temp.append(candidates[i])
        self.stairshelper(target-candidates[i],temp,res,i,candidates)
        temp.pop()
    
    def climbingStairs(self,n):
        if n==0:
            return 1
        if n==1:
            return 1 
        left=self.climbingStairs(n-1)
        right=self.climbingStairs(n-2)
        return left+right
    
    def climbingStairs2(self,n,p):
        if n==0:
            print(p)
            return 1
        if n==1:
            
            return 1 
        left=self.climbingStairs2(n-1,p+str(1))
        right=self.climbingStairs2(n-2,p+str(2))
        return left+right
        
    def frogJump(self,n,heights):
        return self.frogHelper(n-1,heights)
    def frogHelper(self,idx,heights):
        if idx==0:
            return 0
        left=self.frogHelper(idx-1,heights)+abs(heights[idx]-heights[idx-1])
        right=float('inf')
        if idx>1:
            right=self.frogHelper(idx-2,heights)+abs(heights[idx]-heights[idx-2])
        return min(left,right)
        
        
    def frogJumpdp(self,n,heights):
        dp=[-1]*(n+1)
        return self.frogHelperdp(n-1,heights,dp)
    def frogHelperdp(self,idx,heights,dp):
        if idx==0:
            return 0
        if dp[idx]!=-1:
            return dp[idx]
        left=self.frogHelperdp(idx-1,heights,dp)+abs(heights[idx]-heights[idx-1])
        right=float('inf')
        if idx>1:
            right=self.frogHelperdp(idx-2,heights,dp)+abs(heights[idx]-heights[idx-2])
        dp[idx]=min(left,right)
        return dp[idx]
    
# arr=''
# res=[]
# t=3
c=climb()
# stairs(t,arr,res)
# print(res)
# print(c.stairsCombi(t))
# print(c.climbingStairs(t))
# print(c.climbingStairs2(t,''))
n=6
heights=[30,10,60,10,60,50]
print(c.frogJump(n,heights))
print(c.frogJumpdp(n,heights))