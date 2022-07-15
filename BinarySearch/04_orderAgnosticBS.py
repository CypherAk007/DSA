def orderAgnoBinarySearch(nums,target):
  # check for ascending order
  # isAsc=nums[start]<nums[end]
  # or
  start=0
  end=len(nums)-1
  if nums[start]<nums[end]:
    isAsc=True
  else:
    isAsc=False 

  while(start<=end):
    mid = start+(end-start)//2

    if nums[mid]==target:
      return mid 
    if isAsc:
      if target<nums[mid]:
        end=mid-1
      elif target>nums[mid]:
        start= mid+1
    else:
      if target>nums[mid]:
        end=mid-1
      elif target<nums[mid]:
        start= mid+1
  return -1


arr=[-18,-12,-4,0,2,3,4,15,16,18,22,45,89]
target=22
print(orderAgnoBinarySearch(arr,target))