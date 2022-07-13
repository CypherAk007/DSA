print('cypherAk007')
def longSubArrEqu0And1(a):
  d={}
  d[0]=-1
  summ=0
  ans=0
  for i in range(len(a)):
    if a[i]==0:
      summ+=-1
    elif a[i]==1:
      summ+=1
    if summ in d:
      length=i-d[summ]
      if length>ans:
        ans = length
    else:
      d[summ]=i 
  return ans

a=[0,0,1,0,1,0,1,1,0,0,1,1,1]
print(longSubArrEqu0And1(a))