# Using insertion sort - O(n^2)
def moveNegitive(arr):

  key = 0
  for j in range(1,len(arr)):
    key = arr[j]
    i=j-1
    while i!=0 and arr[i]>key:
      arr[i+1]=arr[i]
      i-=1
    arr[i+1]=key
  return arr

# 2-pointer approach -O(n)
def twoPtrMoveNegitive(arr):
  left=0
  right=len(arr)-1
  while(left<=right):
    if arr[left]<0 and arr[right]<0:
      left+=1
    elif arr[left]>0 and arr[right]>0:
      right-=1
    elif arr[left]>0 and arr[right]<0:
      arr[left], arr[right]=arr[right],arr[left]
      left+=1
      right-=1
    else:
      left+=1
      right-=1
  return arr

arr=[-12, 11, -13, -5, 6, -7, 5, -3, -6]
print(moveNegitive(arr))
print(twoPtrMoveNegitive(arr))