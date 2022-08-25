class Countss:
  def countssofs(self,arr,idx,t):
    if t==0:
      return 1 
    if idx==0:
      if arr[idx]==t:
        return 1 
      else:
        return 0 
    
    np=self.countssofs(arr,idx-1,t)
    p=0
    if arr[idx]<=t:
      p=self.countssofs(arr,idx-1,t-arr[idx])
    return p+np 

  def countssOfsMemo(self,arr,idx,t):
    dp=[[-1]*(idx+1) for i in range(t+1)]
    return self.countssofsMemoHelper(arr,idx,t,dp)

  def countssofsMemoHelper(self,arr,idx,t,dp):
    if t==0:
      return 1 
    if idx==0:
      if arr[idx]==t:
        return 1 
      else:
        return 0 
    if dp[idx][t]!=-1:
      return dp[idx][t]
    np=self.countssofsMemoHelper(arr,idx-1,t,dp)
    p=0
    if arr[idx]<=t:
      p=self.countssofsMemoHelper(arr,idx-1,t-arr[idx],dp)
    dp[idx][t]=p+np
    return dp[idx][t]

  def countssOfsTab(self,arr,idx,t):
    dp=[[0]*(idx+1) for i in range(t+1)]
    n=len(arr)
    return self.countssofsTabHelper(arr,idx,t,dp,n)


  def countssofsTabHelper(self,arr,idx,t,dp,n):
    for i in range(0,n):
      dp[i][0]=1

    if arr[0]<=t:
      dp[0][arr[0]]=1
    print(dp,n,t)

    for i in range(1,n):
      for j in range(1,t+1):
        np=dp[i-1][j]

        p=0
        if arr[i]<=t:
          p=dp[i-1][j-arr[i]]

        dp[i][j]=p+np
    print(dp,n,t)
    return dp[n-1][t]

  def countssOfsTabs(self,arr,idx,t):
    dp=[[0]*(idx+1) for i in range(t+1)]
    n=len(arr)
    return self.countssofsTabHelpers(arr,idx,t,dp,n)


  def countssofsTabHelpers(self,arr,idx,t,dp,n):
    prev=[0]*(t+1)
    cur=[0]*(t+1)
    prev[0]=cur[0]=1
    if arr[0]<=t:
      prev[arr[0]]=1
    print(prev,cur)
    print()
    for i in range(1,n):
      for j in range(0,t+1):
        np=prev[j]

        p=0
        if arr[i]<=t:
          p=prev[j-arr[i]]

        cur[j]=p+np
      print(prev,cur)
      prev=cur
    
    return prev[t]



if __name__=='__main__':
  c=Countss()
  # arr=[1,2,2,3]
  arr=[1,1,1,1,1]
  n=len(arr)
  t=3
  print(c.countssofs(arr,n-1,t))
  # print(c.countssOfsMemo(arr,n-1,t))
  # print(c.countssOfsTab(arr,n-1,t))
  # print(c.countssOfsTabs(arr,n-1,t))
