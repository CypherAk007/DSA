class Coins:
  def cc(self,coins,amount):
    n=len(coins)
    x=self.cchelper(n-1,amount,coins)
    if x==float('inf'):
      return -1
    return x
    
  def cchelper(self,idx,t,coins):
    # bc
    if idx==0:
      if t%coins[idx]==0:
        return t//coins[idx]
      else:
        return float('inf')

    np=0+self.cchelper(idx-1,t,coins)
    p=float('inf')
    if coins[idx]<=t:
      p=1+self.cchelper(idx,t-coins[idx],coins)
    return min(p,np)


if __name__=='__main__':
  c=Coins()
  coins=[2]
  amount=3
  print(c.cc(coins,amount))