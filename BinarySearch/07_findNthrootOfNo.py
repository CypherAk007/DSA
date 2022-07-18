def multiply(number,n):
  ans=1.0
  for i in range(1,n+1):
    ans=ans*number 
  return ans   

def getNthRoot(n,m):
  low=1 
  high=m 
  eps = 1e-6

  while((high-low)>eps):
    # print(high-low)
    mid=(low+high)/2.0
    if multiply(mid,n)<m:
      low=mid 
    else:
      high=mid 
  print("{:.6f}".format(low))
  print(int(low))


n=3
m=9
getNthRoot(n,m)
