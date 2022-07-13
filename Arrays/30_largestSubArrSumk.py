def largestSubArr(a,k):
  d={}
  d[0]=-1
  ans=0
  summ=0
  for i in range(len(a)):
    summ+=a[i]
    if summ-k in d:
      length=i-d[summ-k]
      ans=max(ans,length)
    if summ not in d:
      d[summ]=i 
  return ans

a=[10, 5, 2, 7, 1, 9]
k=15
print(largestSubArr(a,k))