class fib: 
  def fibonacci(self,n):
    if n<=1:
      return n 
    return self.fibonacci(n-1)+self.fibonacci(n-2)

  def fiboMemo(self,n):
    dp=[-1]*(n+1)
    return self.fibmemoHelper(n,dp)
  def fibmemoHelper(self,n,dp):
    dp[0]=0
    if n>=1:
      dp[1]=1
    if dp[n]!=-1:
      return dp[n]

    dp[n]=self.fibmemoHelper(n-1,dp)+self.fibmemoHelper(n-2,dp)
    return dp[n]

  def fiboTab(self,n):
    dp=[-1]*(n+1)
    return self.fibTabHelper(n,dp)
  def fibTabHelper(self,n,dp):
    dp[0]=0
    if n>=1:
      dp[1]=1
    # if dp[n]!=-1:
    #   return dp[n]
    for i in range(2,n+1):
      dp[i]=self.fibTabHelper(i-1,dp)+self.fibTabHelper(i-2,dp)
    return dp[n]


  def fiboTabspace(self,n):
    # dp=[-1]*(n+1)
    return self.fibTabspaceHelper(n)
  def fibTabspaceHelper(self,n):
    # dp[0]=0
    # if n>=1:
    #   dp[1]=1
    # if dp[n]!=-1:
    #   return dp[n]
    previ=1
    prev2i=0
    if n==0:
      return prev2i
    for i in range(2,n+1):
      curi=previ+prev2i
      prev2i=previ
      previ=curi
    return previ

if __name__=='__main__':
  s=fib()
  print(s.fibonacci(1))
  n=6
  print(s.fiboMemo(n))
  print(s.fiboTab(n))
  print(s.fiboTabspace(n))