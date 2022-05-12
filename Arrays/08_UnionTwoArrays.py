# Given two arrays a[] and b[] of size n and m respectively. 
# The task is to find union between these two arrays.
# Union of the two arrays can be defined as the set containing 
# distinct elements from both the arrays. If there are repetitions, 
# then only one occurrence of element should be printed in the union.

# inbuilt methods
def unionArrays(arr1,arr2):
  outArr=arr1+arr2
  print(outArr)
  outArr=set(outArr)
  print(outArr)
  return len(list(outArr))

def unionArrays2(arr1,arr2):
  s=set()
  for i in range(len(arr1)):
    s.add(arr1[i])
  for j in range(len(arr2)):
    s.add(arr2[j])
  return len(list(s))

# 1) Use two index variables i and j, initial values i = 0, j = 0 
# 2) If arr1[i] is smaller than arr2[j] then print arr1[i] and increment i. 
# 3) If arr1[i] is greater than arr2[j] then print arr2[j] and increment j. 
# 4) If both are same then print any of them and increment both i and j. 
# 5) Print remaining elements of the larger array

# two pointer approach
def twoPointerUnion(arr1,arr2):
  arr1.sort()
  arr2.sort()
  m=len(arr1)
  n=len(arr2)
  i=0
  j=0
  out= []
  # keep track of last element to avoid duplicates
  prev = None

  while i<m and j<n:
    if arr1[i]<arr2[j]:
      if arr1[i]!=prev:
        out.append(arr1[i])
        prev=arr1[i]
      i+=1
    elif arr1[i]>arr2[j]:
      if arr2[j]!=prev:
        out.append(arr2[j])
        prev=arr2[j]
      j+=1
    else:
      if arr1[i]!=prev:
        out.append(arr1[i])
      i+=1
      j+=1

  while i<m:
    if arr1[i]!=prev:
      out.append(arr1[i])
      prev = arr1[i]
    i+=1

  while j<n:
    if arr2[j]!=prev:
      out.append(arr2[j])
      prev = arr2[j]
    j+=1

  return len(out)



arr1=[1,2,3,4,5]
arr2=[1,2,3]
print(unionArrays(arr1,arr2))
print(unionArrays2(arr1,arr2))
print(twoPointerUnion(arr1,arr2))
