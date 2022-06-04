# tell the 5th smallest element
def quickSelect(arr,lo,hi,k):
  pivot=arr[hi]
  pi=partition(arr,pivot,lo,hi)
  print(pivot,k,pi,arr)
  if k>pi:#kth index>pivot index then search in right part
    return quickSelect(arr,pi+1,hi,k)
  elif k<pi:
    return quickSelect(arr,lo,pi-1,k)
  else:
    return pivot

def partition(arr,pivot,lo,hi):
  # i-end - unknown
  # 0- j-1- small
  # j- i-1  -big elements
  i=lo
  j=lo
  while(i<=hi):
    if arr[i]<=pivot:
      swap(arr,i,j)
      i+=1
      j+=1
    else:
      i+=1
  return j-1#returns pivot position

def swap(arr,i,j):
  arr[i],arr[j]=arr[j],arr[i]



if __name__=="__main__":
  arr=[2,8,1,3,7,6,4,5]
  k=4#4th smallest element
  print(quickSelect(arr,0,len(arr)-1,k-1))