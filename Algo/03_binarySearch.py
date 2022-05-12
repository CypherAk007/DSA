def binarySearch(arr,element):
  low = 0
  high = len(arr)-1
  mid =0
  while(low<=high):
    mid=(low+high)//2
    if element==arr[mid]:
      return mid
    elif element<arr[mid]:
      high= mid-1
    elif element>arr[mid]:
      low=mid+1
  else:
    print("element not in array")
    return -1

arr=[1,2,3,4,5,6]
element=30
print(binarySearch(arr,element))