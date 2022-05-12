#Two sum modified
def twosum(arr,summ,n):
  unordered_map = {}
  count = 0
  for i in range(n):
    b=summ - arr[i] 
    if b in unordered_map:
      count += unordered_map[b]
    if arr[i] in unordered_map:
      unordered_map[arr[i]] += 1
    else:
      unordered_map[arr[i]] = 1
  return count
            
            
nums=[1,5,1,7]
nums1=[1,1,1,1]
n=len(nums)
target=6
target2=2
n2=len(nums1)
print(twosum(nums1,target2,n2))
