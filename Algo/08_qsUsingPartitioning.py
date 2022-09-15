def partition(arr,low,hi,pivot):
  i=low
  j=low
  while(i<=hi):
    if arr[i]>pivot:
      i+=1
    else:
      arr[i],arr[j]=arr[j],arr[i]
      i+=1
      j+=1
  # return arr 
  return j-1 #return the pivot index

def quicksort(arr,low,hi):
  if low>=hi:
    return

  pivot=arr[hi]
  pi=partition(arr,low,hi,pivot) #stores the pivot index
  quicksort(arr,low,pi-1)
  quicksort(arr,pi+1,hi)



arr=[7,9,4,8,3,6,7,8,5]
quicksort(arr,0,len(arr)-1)
# print(partition(arr,0,len(arr)-1,5))
print(arr)