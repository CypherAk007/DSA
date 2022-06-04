def partition(arr,pivot):
  i=0
  j=0
  while(i<len(arr)):
    if arr[i]>pivot:
      i+=1
    else:
      swap(arr,i,j)
      i+=1
      j+=1

def swap(arr,i,j):
  arr[i],arr[j]=arr[j],arr[i]


arr=[7,9,4,8,3,6,2,1]
partition(arr,5)
print(arr)