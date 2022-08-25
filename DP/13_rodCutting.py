class RodCutting:
  def rodrec(self,price,N):
    n=len(price)
    return self.helper(n-1,N,price)

  def helper(self,idx,N,price):
    # bc
    if idx==0:
      return N*price[0]

    np=0+self.helper(idx-1,N,price)
    p=float('-inf')
    rodlen=idx+1
    if rodlen<=N:
      p=price[idx]+self.helper(idx,N-rodlen,price)
    return max(np,p)

  def rodmem(self,price,N):
    n=len(price)
    dp=[[-1]*(N+1) for i in range(n)]
    return self.helpermem(n-1,N,price,dp)
    
  def helpermem(self,idx,N,price,dp):
    # bc
    if idx==0:
      return N*price[0]

    if dp[idx][N]!=-1:
      return dp[idx][N]
    np=0+self.helpermem(idx-1,N,price,dp)
    p=float('-inf')
    rodlen=idx+1
    if rodlen<=N:
      p=price[idx]+self.helpermem(idx,N-rodlen,price,dp)
    dp[idx][N]=max(np,p)
    return  dp[idx][N] 

  def rodtab(self,price,N):
    n=len(price)
    dp=[[0]*(N+1) for i in range(n)]
    return self.helpertab(n-1,N,price,dp)
    
  def helpertab(self,idx,N,price,dp):
    # bc
    for n in range(0,N+1):
      dp[0][n]=n*price[0]

    for i in range(1,N):
      for n in range(0,N+1):
        np=0+dp[i-1][n]
        p=float('-inf')
        rodlen=i+1
        if rodlen<=n:
          p=price[i]+dp[i][n-rodlen]
        dp[i][n]=max(np,p)
    return  dp[len(price)-1][N] 

if __name__=='__main__':
  rc=RodCutting()
  price=[2,5,7,8,10]
  N=5
  print(rc.rodrec(price,N))
  print(rc.rodmem(price,N))
  print(rc.rodtab(price,N))