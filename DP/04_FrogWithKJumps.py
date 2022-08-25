class Frog:
  def frogkJump(self,n,k,heights):
    return self.frogHelper(n-1,k,heights)

  def frogHelper(self,idx,k,heights):
    if idx==0:
      return 0
    minsteps=float('inf')
    for i in range(1,k+1):
      if idx-i>=0:
        jump=self.frogHelper(idx-i,k,heights)+abs(heights[idx]-heights[idx-i])
        minsteps=min(minsteps,jump)
    return minsteps

f=Frog()
n=5
heights=[30,10,60,10,60,50 ]
k=5
print(f.frogkJump(n,k,heights))