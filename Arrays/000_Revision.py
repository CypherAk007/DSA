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
'''
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
'''

"""
# 495. Teemo Attacking
def ta(ts,d):
  count=0
  for i in range(len(ts)):
    curr=ts[i]
    poi=curr+d-1
    if i!=len(ts)-1 and ts[i+1]<=poi:
      count+=ts[i+1]-ts[i]
    else:
      count+=d

  return count


ts=[1,4]
d=2
print(ta(ts,d))
"""

"""
# 13. Roman to Integer
def rtoi(s):
  d={ "I":            1,
      "V":             5,
      "X":            10,
      "L":            50,
      "C":             100,
      "D" :            500,
      "M" :           1000}  
  # print(d)
  i=0
  res=0
  while(i<len(s)):
    if i!=len(s)-1 and d[s[i]]<d[s[i+1]]:
      res+=(d[s[i+1]]-d[s[i]])
      i+=1
    else:
      res+=d[s[i]]
    i+=1
  return res
print(rtoi("MCMXCIV"))
"""
"""
# Bubble sort

def bs(arr,k):
  for j in range(len(arr)-1):
    for i in range(len(arr)-j-1):
      if arr[i]>arr[i+1]:
        arr[i],arr[i+1]=arr[i+1],arr[i]
  return arr[-k]
arr=[3,2,1,5,6,4]
k=2
print(bs(arr,k))
print(arr)
"""
"""
# 2091. Removing Minimum and Maximum From Array

from operator import indexOf
from os import remove


def rmm(arr):
  a=min(arr)
  b=max(arr)
  i=indexOf(arr,a)
  j=indexOf(arr,b)
  print(a,i,b,j)
  lst=[]
  #remove fm min front and max back
  front=min(i,j)+1
  back = len(arr)-max(i,j)
  print(front,back)
  lst.append(front+back)
  # remove both fm front
  lst.append(max(i,j)+1)
  # remove both fm back
  lst.append(len(arr)-min(i,j))
  print(lst)
  print(min(lst))
  return min(lst)

arr=[101]
rmm(arr)
"""
"""
# two sum

def ts(arr,t):
  d={}
  for i in range(len(arr)):
    temp=abs(t-arr[i])
    if temp in d:
      return d[temp],i
    d[arr[i]]=i

arr=[2,7,11,15]
t=9
print(ts(arr,t))
"""
# three sum
# def ths(arr,t):
#   d={}
#   lst=[]
#   for i in range(len(arr)):
#     temp=t-arr[i]
#     if temp in d:
#       tlst=[]
#       print(d[temp])
#       for i in d[temp]:
#         print(f'1->{arr[i]}')
#         tlst.append(arr[i])
#       lst.append(tlst+[arr[i]])
#     else:
#       for j in range(i+1,len(arr)):
#         d[arr[i]+arr[j]]=[i,j]
#   print(d)
#   return lst  

# arr=[-1,0,1,2,-1,-4]
# t=0
# print(ths(arr,t))
      

