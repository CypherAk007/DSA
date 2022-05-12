def rotateOne(arr):
  i=len(arr)-1
  temp=arr[i]
  while i>0:
    arr[i]=arr[i-1]
    i-=1
  arr[i]=temp
  return arr

def rotate( arr, n):
   x = arr[n-1]
   for i in range(n-1, 0, -1):
       arr[i] = arr[i-1]
   arr[0] = x

arr=[9, 8, 7, 6, 4, 2, 1, 3]
rotate(arr,len(arr))
print(arr)

