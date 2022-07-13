def ceiling(a,i,j,t):
  # Boundry case if target>last no. in the arr
  if t>a[len(a)-1]:
    return -1

  while(i<=j):
    mid = (i+j)//2
    # print(i,j,t,a[mid],mid)
    if t==a[mid]:
      return a[mid]
    if t>a[mid]:
      i=mid+1
    elif t<a[mid]:
      j=mid-1
  return a[i]

a=[2,3,5,9,14,16,18]
i=0
j=len(a)-1
t=19
print(ceiling(a,i,j,t))