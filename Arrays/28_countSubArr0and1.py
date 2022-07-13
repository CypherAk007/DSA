def countSubArr(a):
  d={}
  d[0]=1 #map has summ and freq
  summ=0
  ans=0
  for i in range(len(a)):
    if a[i]==0:
      summ+=-1
    elif a[i]==1:
      summ+=1
    
    if summ in d:
      ans+=d[summ]
      d[summ]+=1
    else:
      d[summ]=1
  return ans

a=[0,0,1,0,1]
print(countSubArr(a))