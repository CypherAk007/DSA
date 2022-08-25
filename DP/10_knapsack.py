class Knapsack:
  def knapsack(self,weight,value,n,maxWeight):
    return self.knaprec(n-1,maxWeight,weight,value)
  def knaprec(self,idx,W,weight,value):
    # bc
    if idx==0:
      if weight[idx]<=W:
        return value[idx]
      else:
        return 0

    notTake=0+self.knaprec(idx-1,W,weight,value)

    Take=float('-inf')
    if weight[idx]<=W:
      Take=value[idx]+self.knaprec(idx-1,W-weight[idx],weight,value)
    
    return max(Take,notTake)


  def knapsackmemo(self,weight,value,n,maxWeight):
    dp=[[-1]*(maxWeight+1)for i in range(n)]
    return self.knaprecmemo(n-1,maxWeight,weight,value,dp)

  def knaprecmemo(self,idx,W,weight,value,dp):
    # bc
    if idx==0:
      if weight[idx]<=W:
        return value[idx]
      else:
        return 0

    if dp[idx][W]!=-1:
      return dp[idx][W]

    notTake=0+self.knaprecmemo(idx-1,W,weight,value,dp)

    Take=float('-inf')
    if weight[idx]<=W:
      Take=value[idx]+self.knaprecmemo(idx-1,W-weight[idx],weight,value,dp)
    dp[idx][W]=max(Take,notTake)
    return dp[idx][W]

  def knapsacktab(self,weight,value,n,maxWeight):
    dp=[[0]*(maxWeight+1)for i in range(n)]
    return self.knaprectab(n-1,maxWeight,weight,value,dp)

  def knaprectab(self,idx,maxW,wt,value,dp):
    # bc 
    n=len(wt)
    for W in range(wt[0],maxW+1):
      dp[0][W]=value[0]

    for idx in range(1,n):
      for W in range(0,maxW+1):
        notTake=0+dp[idx-1][W]

        Take=float('-inf')
        if weight[idx]<=W:
          Take=value[idx]+dp[idx-1][W-weight[idx]]
        dp[idx][W]=max(Take,notTake)
       
    return dp[n-1][W]

  def knapsacktabs(self,weight,value,n,maxWeight):
    dp=[[0]*(maxWeight+1)for i in range(n)]
    return self.knaprectabs(n-1,maxWeight,weight,value,dp)

  def knaprectabs(self,idx,maxW,wt,value,dp):
    # bc 
    n=len(wt)
    cur=[0]*(maxW+1)
    for W in range(wt[0],maxW+1):
      prev[W]=value[0]

    for idx in range(1,n):
      for W in range(0,maxW+1):
        notTake=0+prev[W]

        Take=float('-inf')
        if weight[idx]<=W:
          Take=value[idx]+prev[W-weight[idx]]
        cur[W]=max(Take,notTake)
      prev=cur 
    return prev[W]

  

if __name__=='__main__':
  k=Knapsack()
  weight=[3,2,5]
  value=[30,40,60]
  maxWeight=6
  print(k.knapsack(weight,value,len(weight),maxWeight))
  print(k.knapsackmemo(weight,value,len(weight),maxWeight))
  print(k.knapsacktab(weight,value,len(weight),maxWeight))
  print(k.knapsacktabs(weight,value,len(weight),maxWeight))