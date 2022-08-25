class MSNAE:
  # memo
  def maxsum(self,idx,a,dp):
    if idx==0:
      return a[idx]
    if idx<0:
      return 0
    if dp[idx]!=-1:
      return dp[idx]
    pick=a[idx]+self.maxsum(idx-2,a,dp)
    notp=0+self.maxsum(idx-1,a,dp)
    dp[idx]=max(pick,notp)
    return dp[idx]

if __name__=='__main__':
  m=MSNAE()
  a=[2,1,4,9]
  idx=len(a)-1
  dp=[-1]*(idx+1)
  print(m.maxsum(idx,a,dp))