def countSubArr(a,k):
  c=0
  d={}
  d[0]=1 # initial 
  summ=0
  for i in range(len(a)):
    summ+=a[i]
    if summ-k in d:
      c+=d[summ-k]
    if summ in d:
      d[summ]+=1
    else:
      d[summ]=1

  return c

a=[3,9,-2,4,1,-7,2,6,-5,8,-3,-7,6,2,1]
k=5
print(countSubArr(a,k))

