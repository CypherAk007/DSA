# Given an array of integers nums, return the number of good pairs.

# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

def gp(arr):
  d={}
  count=0
  for i in arr:
    if i in d:
      count+=d[i]
      d[i]+=1
    else:
      d[i]=1
  return count


print(gp([1,2,3,1,1,3]))