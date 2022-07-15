def findPeak(arr):
  l=0
  h=len(arr)-1
  while(l<=h):
    mid=l+(h-l)//2
    if arr[mid]>arr[mid+1]:
      # dec part
      h=mid 
    else: #asc part
      l=mid+1
  return l 

arr=[1,2,3,4,5,6,4,3,2]
print(findPeak(arr))