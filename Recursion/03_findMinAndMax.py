def findMin(arr,n):
  if n==len(arr)-1:
    return arr[n]
  x=findMin(arr,n+1)
  if x>arr[n]:
    return arr[n]
  else:
    return x

def findMax(arr,n):
  if n==len(arr)-1:
    return arr[n]
  x=findMax(arr,n+1)
  if x<arr[n]:
    return arr[n]
  else:
    return x


arr=[1, 4, 45, 6, -10, -8]
print(findMin(arr,0))
print(findMax(arr,0))