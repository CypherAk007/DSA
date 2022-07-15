from operator import indexOf


def findPivot(arr):
  start=0
  end=len(arr)-1
  while(start<=end):
    mid=start+(end-start)//2
    print(arr[start],arr[mid],arr[end])
    # 4cases 
    if mid<end and arr[mid]>arr[mid+1]:
      print(arr[mid],mid)
      return mid
    if mid>start and arr[mid]<arr[mid-1]:
      print(arr[mid],mid)
      return mid
    if arr[mid]<=arr[start]:
      end=mid-1
    else:#start<mid
      start=mid+1
  return -1

def findRotCnt(arr):
  pivot=findPivot(arr)
  print(pivot)
  if pivot==-1:
    return 0
  else:
    return pivot+1



arr=[3,4,1,2]
print(findRotCnt(arr))

# Input: arr[] = {15, 18, 2, 3, 6, 12}
# Output: 2
# Explanation: Initial array must be {2, 3, 6, 12, 15, 18}. We get the given array after rotating the initial array twice.

# Input: arr[] = {7, 9, 11, 12, 5}
# Output: 4

# Input: arr[] = {7, 9, 11, 12, 15};
# Output: 0