class WaysToReach:
  def countwtr(self,n):
    if n<=1:
      return 1
    left=self.countwtr(n-1)
    right=self.countwtr(n-2)
    return left+right

  def wtr(self,n,p):
    if n==0:
      print(p+str(1))
      return 

    if n==1:
      
      return 
    self.wtr(n-1,p+str(1))
    self.wtr(n-2,p+str(2))
    
  def wtrmemo(self,n):
    dp=[-1]*(n+1)
    return self.wtrmemoHelper(n,dp)
  def wtrmemoHelper(self,n,dp):
    dp[0]=1
    if n>=1:
      dp[1]=1
    if dp[n]!=-1:
      return dp[n]
    left=self.wtrmemoHelper(n-1,dp)
    right=self.wtrmemoHelper(n-2,dp)
    dp[n]=left+right 
    return dp[n]

  def wtrtab(self,n):
    return self.wtrtabhelper(n)
  def wtrtabhelper(self,n):
    prev2i=1
    if n>=1:
      previ=1
    if n==0:
      return prev2i
    for i in range(2,n+1):
      curi=previ+prev2i
      prev2i=previ
      previ=curi
    return previ    

if __name__=='__main__':
  w=WaysToReach()
  print(w.countwtr(5))
  n=5
  p=''
  # print(w.wtr(n,p))
  print(w.wtrmemo(n))
  print(w.wtrtab(n))