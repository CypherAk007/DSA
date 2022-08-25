class UbKp:
  def ubknaprec(self,wt,val,W):
    n=len(wt)
    return self.ubrechelper(n-1,W,wt,val)

  def ubrechelper(self,idx,W,wt,val):
    if idx==0:
      return (W//wt[0])*val[0]
    
    np=0+self.ubrechelper(idx-1,W,wt,val)
    p=float('-inf')
    if wt[idx]<=W:
      p=val[idx]+self.ubrechelper(idx,W-wt[idx],wt,val)
    return max(p,np)

  def ubknapmem(self,wt,val,W):
    n=len(wt)
    dp=[[-1]*(W+1) for i in range(n)]
    return self.ubmemhelper(n-1,W,wt,val,dp)

  def ubmemhelper(self,idx,W,wt,val,dp):
    if idx==0:
      return (W//wt[0])*val[0]
    
    if dp[idx][W]!=-1:
      return dp[idx][W]
    np=0+self.ubmemhelper(idx-1,W,wt,val,dp)
    p=float('-inf')
    if wt[idx]<=W:
      p=val[idx]+self.ubmemhelper(idx,W-wt[idx],wt,val,dp)
    dp[idx][W]=max(p,np)
    return dp[idx][W]

  def ubknaptab(self,wt,val,W):
    n=len(wt)
    dp=[[0]*(W+1) for i in range(n)]
    return self.ubtabhelper(W,wt,val,dp)

  def ubtabhelper(self,W,wt,val,dp):
    n=len(wt)
    for w in range(0,W+1):
      dp[0][w]=(w//wt[0])*val[0]

    for idx in range(1,n):
      for w in range(0,W+1):
        np=0+dp[idx-1][w]
        p=0
        if wt[idx]<=w:
          p=val[idx]+dp[idx][w-wt[idx]]
        dp[idx][w]=max(p,np)
    
    return dp[n-1][W]

if __name__=='__main__':
  u=UbKp()
  wt=[2,4,6]
  val=[5,11,13]
  W=10
  print(u.ubknaprec(wt,val,W))
  print(u.ubknapmem(wt,val,W))
  print(u. ubknaptab(wt,val,W))