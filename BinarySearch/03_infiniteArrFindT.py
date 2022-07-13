def ans(arr,target):
  start=0
  end=1
  while(target>arr[end]):
    temp=end+1
    end=end+(end-start+1)*2
    start = temp
  
  return binarySearch(arr,target,start,end)
def binarySearch(nums,target,start,end):
  
  while(start<=end):
    mid = start+(end-start)//2

    if target<nums[mid]:
      end=mid-1
    elif target>nums[mid]:
      start= mid+1
    else:
      #find the potetial ans
      return mid
  return -1


arr=[3,5,7,9,10,90,100,130,140,160,170]
target=10
print(ans(arr,target))