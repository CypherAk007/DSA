class SSET:
  def subSetSum(self,idx,target,a):
    if target==0:
      return True 
    if idx==0:
      return a[0]==target 
    np=self.subSetSum(idx-1,target,a)
    p=self.subSetSum(idx-1,target-a[idx],a)
    return p or np 

  
  def subSumMemo(self,idx,target,a,dp):
    if target==0:
      return True 
    if idx==0:
      return a[0]==target 
    if dp[idx][target]!=-1:
      return dp[idx][target]
    np=self.subSumMemo(idx-1,target,a,dp)
    p=False
    if a[idx]<=target:
      p=self.subSumMemo(idx-1,target-a[idx],a,dp)
    dp[idx][target]=p or np 
    return dp[idx][target]

  def subsetSumTab(self,idx,k,a,dp):
    # bc
    # idx->n-1(len(a)-1)
    for i in range(0,idx+1):
      dp[i][0]=True 
    if a[0]<=k:
      dp[0][a[0]]=True 
    print(dp)
    for idx in range(1,idx):
      for target in range(1,k+1):
        np=dp[idx-1][target]
        p=False
        if a[idx]<=target:
          p=dp[idx-1][target-a[idx]]

        dp[idx][target]= np or p
        print(dp)
    return dp[idx][k]        

  def subsetSumTabspace(self,idx,k,a,dp):
    # bc
    # idx->n-1(len(a)-1)
    prev=[0]*(k+1)
    cur=[0]*(k+1)
    prev[0]=cur[0]=True
    if a[0]<=k:
      prev[a[0]]=True
    for idx in range(1,idx):
      for target in range(1,k+1):
        np=dp[idx-1][target]
        p=False
        if a[idx]<=target:
          p=dp[idx-1][target-a[idx]]

        cur[target]= np or p
      prev=cur
    return prev[k]  



if __name__=='__main__':
  ss=SSET()
  a=[1,2,3,4]
  print(ss.subSetSum(len(a)-1,4,a))
  k=4
  idxsize=len(a)
  targetsize=k+1
  dp=[[-1]*targetsize for i in range(idxsize)]
  print(ss.subSumMemo(len(a)-1,4,a,dp))
  dp=[[False]*targetsize for i in range(idxsize)]
  # print(dp)
  print(ss.subsetSumTab(len(a)-1,k,a,dp))
  # print(dp)
  print(ss.subsetSumTabspace(len(a)-1,k,a,dp))
  # print(dp)