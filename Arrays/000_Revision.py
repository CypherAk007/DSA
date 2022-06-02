"""
# # 1920. Build Array from Permutation
# # Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.

def zba(arr):
  ans = [0]* len(arr)
  for i in range(len(arr)):
    ans[i]=arr[arr[i]]
  return ans

def mathzba(arr):
  length = len(arr)
  # length = 10
  for i in range(length):
    # print(arr[i],arr[arr[i]],i,'1')
    arr[i]=arr[i]+((arr[arr[i]]%length)*length)
    # print(arr[i],i,'2')
  # print(arr)
  for i in range(length):
    arr[i]=arr[i]//length
  # print(arr)
  return arr

arr=[5,0,1,2,3,4]
# print(zba(arr))
print(mathzba(arr))


# a=3
# b=2
# c=a+b*10
# print(c)
# print(c//10)
# print(c%10)
"""

"""
# 1929. Concatenation of Array
# where ans[i] == nums[i] and ans[i + n] == nums[i]
 
def ccarr(arr):
  length = len(arr)
  res= [0]*(2*len(arr))
  for i in range(len(res)):
    res[i]=arr[i%len(arr)]

  return res

arr=[1,3,2,1]
print(ccarr(arr))
"""
"""
# # 1480. Running Sum of 1d Array
# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
def rs(arr,i):
  if i>=len(arr):
    return arr
  arr[i]=arr[i-1]+arr[i]
  out=rs(arr,i+1)
  return out

arr=[1,2,3,4]
i=1
print(rs(arr,i))
"""
"""
# 35. Search Insert Position
def sip(arr,target):
  i=0
  j=len(arr)-1
  mid=0
  while(i<=j):
    mid=(i+j)//2
    if arr[mid]==target:
      return mid
    
    if arr[mid]<target:
      i=mid+1
    else:
      j=mid-1
  return mid+1

nums = [1,3,5,6]
target = 7
print(sip(nums,target))
"""
"""
# 268. Missing Number
def mn(arr):
  for i in range(len(arr)):
    if i not in arr:
      return i

def mn2(arr):
  n =len(arr)
  av=(n*(n+1))//2
  ov=0
  for i in range(n):
    ov+=arr[i]
  return av-ov

arr=[9,6,4,2,3,5,7,0,1]
print(mn(arr))
print(mn2(arr))
"""
def mat(matrix):
  print(len(matrix))
  for i in range(len(matrix)):
    row_val=[]
    col_val=[]
    row_val+=len(matrix)*[0]
    col_val+=len(matrix)*[0]
    print(row_val,col_val)
    for j in range(len(matrix)):
      rVal=matrix[i][j]
      cVal=matrix[j][i]
      print(rVal,cVal)
      if row_val[rVal-1] == 1 or col_val[cVal-1]== 1:
        return False
      
      row_val[rVal-1]=1
      col_val[cVal-1]=1
      print('2---')
      print(row_val,col_val)
        
    return True


matrix = [[1,1,1],[1,2,3],[1,2,3]]
print(mat(matrix))
