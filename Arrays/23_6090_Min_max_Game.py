def rec(arr,n):
  if n==1:
    return arr[0]
  # print(n,n/2,n//2)
  temp=[0]*(n//2)
  for i in range(n//2):
    if i%2==0:
      temp[i]=min(arr[2*i],arr[2*i+1])
    else:
      temp[i]=max(arr[2*i],arr[2*i+1])
  out=rec(temp,n//2)
  return out

arr=[3]
n=len(arr)
print(rec(arr,n))