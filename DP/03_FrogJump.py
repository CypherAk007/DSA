class Frog:
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

  def frogmemo(self,n,heights):
    dp=[-1]*(n+1)
    return self.frogmemoHelper(n-1,heights,dp)
  
  def frogmemoHelper(self,idx,heights,dp):
    dp[0]=0
    if dp[idx]!=-1:
      return dp[idx]
    left=self.frogmemoHelper(idx-1,heights,dp)+abs(heights[idx]-heights[idx-1])
    right=float('inf')
    if idx>1:
      right=self.frogmemoHelper(idx-2,heights,dp)+abs(heights[idx]-heights[idx-2])
    dp[idx]=min(left,right)
    return dp[idx]

  def frogtab(self,n,heights):
    dp=[-1]*(n+1)
    return self.frogtabHelper(n-1,heights,dp)
  
  def frogtabHelper(self,n,heights,dp): 
    dp[0]=0
    # left=0
    for idx in range(1,n):
      left=dp[idx-1]+abs(heights[idx]-heights[idx-1])
      right=float('inf')
      if idx>1:
        right=dp[idx-2]+abs(heights[idx]-heights[idx-2])
      dp[idx]=min(left,right)
    return dp[n-1]

f=Frog()
n=5
heights=[30,10,60,10,60,50 ]
print(f.frogJump(n,heights))
print(f.frogmemo(n,heights))
print(f.frogtab(n,heights))