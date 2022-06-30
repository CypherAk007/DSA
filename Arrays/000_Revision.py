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

"""
# Sort Colors
def sc(arr):
  l=0
  m=0
  h=len(arr)-1
  i=0
  while(m<=h):
    if arr[m]==0:
      arr[l],arr[m]=arr[m],arr[l]
      l+=1
      m+=1
      print("1")
      print(i,l,m,h)
      print(arr)
    elif arr[m]==1:
      m+=1
      print("2")
      print(i,l,m,h)
      print(arr)
    else:
      arr[m],arr[h]=arr[h],arr[m]
      h-=1
      print("3")
      print(i,l,m,h)
      print(arr)
    i+=1
      
arr= [2,0,2,1,1,0]     
sc(arr)
print(arr)
"""
"""
# 442. Find All Duplicates in an Array
def fad(arr):
  out=[]
  for i in range(arr):
    if arr[i-1]<0:
      out.append(abs(arr[i]))
    else:
      arr[i-1]*=-1
"""
"""
#53. Maximum Subarray
def msa(arr):
  maxi=float('-inf')
  cur_sum=0
  for i in arr:
    cur_sum+=i
    
    if cur_sum>maxi:
      maxi=cur_sum
    print(cur_sum,maxi)
    if cur_sum<0:
      cur_sum=0
      print("zero")

msa([-2,1,-3,4,-1,2,1,-5,4])
  """
"""
# 1470. Shuffle the Array
def sa(arr,n):
  res=[]
  i=0
  j=n
  while(i!=n or j<len(arr)):
    res.append(arr[i])
    i+=1
    res.append(arr[j])
    j+=1
  return res

def saIp(arr,n):
  for i in range(n):
    arr[i]+=arr[n+i]*10000

  for i in range(n-1,-1,-1):
    arr[2*i+1]=arr[i]//10000
    arr[2*i]=arr[i]%10000

arr = [2,5,1,3,4,7]
n=3
print(saIp(arr,n))
print(arr)
"""
"""
# # 1431. Kids With the Greatest Number of Candies
# def candy(arr,e):
#   maxi=max(arr)

from tkinter.messagebox import YES

class Solution:
    def palindromicArray(self, n : int, a : List[int], k : int) -> bool:
        # code here
        i=0
        temp=[]
        for i in range(len(a)):
          if a[i]!=k:
            temp.append(a[i])
        return self.checkPalindrom(temp)
        
        
    def checkPalindrom(self,arr):
        i=0
        j=len(arr)-1
        if len(arr)==1:
            return 1
            
        while(i<j):
            if arr[i]==arr[j]:
                i+=1
                j-=1
            else:
                return False
        return True
a=[13, 55 ,7 ,60 ,63 ,3 ,58 ,13 ,12 ,12 ,13 ,58 ,3 ,63 ,60, 7 ,55 ,13]
k=58
# k=58

n=len(a)
palindromicArray( n , a , k )
"""
"""
# # 1854. Maximum Population Year
# def mp(arr):
#   f=arr[0][0]
#   l=arr[-1][1]
#   print(f,l)
#   temp=[0]*(l-f)
#   print(len(temp),l-f)
#   for i in arr:
#     print(i[0],i[1])
#     for j in range(i[0],i[1]):
#       x=j%f
#       print(x)
#       temp[x]+=1
#   print(temp)
#   max_idx=0
#   for i in range(len(temp)):
#     if temp[i]>temp[max_idx]:
#       max_idx=i
#   print(f+ max_idx)
#   return f+max_idx

# arr=[[1982,1998],[2013,2042],[2010,2035],[2022,2050],[2047,2048]]
# mp(arr)
"""
"""
# # # # # # # # # # # # # # # # lc contest
# def re(arr,op):

#   for i in range(len(op)):
#     for j in range(len(arr)):
#       if arr[j]==op[i][0]:
#         arr[j]=op[i][1]
#         break
#   print(arr)


# arr=[1,2,4,6]
# op=[[1,3],[4,7],[6,1]]
# re(arr,op)

def rec(arr,n):
  if n==1:
    return arr[0]
  # print(n,n/2,n//2)
  temp=[0]*(n//2)
  for i in range(n//2):
    if i%2==0:
      temp[i]=min(arr[2*i],arr[2*i+1])
    else:
      temp[i]=max(arr[2*i],arr[2*i+1])
  out=rec(temp,n//2)
  return out

arr=[3]
n=len(arr)
print(rec(arr,n))

"""
"""
# 989. Add to Array-Form of Integer
def add(num,k):
  c=k
  ext=[]
  for i in range(len(num)-1,-1,-1):
    if c==0:
      break
    val=c+num[i]
    num[i]=val%10
    val=val//10
    c=val
    print(num,val,c,k)
  if c!=0:
    while c!=0:
      ext.append(c%10)
      c=c//10
      
      print(c,ext)
    ext.reverse()
    for i in range(len(num)):
      ext.append(num[i])
    return ext
  return num
# num=[1,2,0,0]
# k=34
# num = [2,1,5]
# k = 806
num=[0]
k=10000
# num = [2,7,4]
# k = 181
print(add(num,k))
"""
"""

# 66.PlusOne
def po(d):
  c=1
  lst=[]
  for i in range(len(d)-1,-1,-1):
    if c==0:
      break
    temp=d[i]+c
    d[i]=temp%10
    c=temp//10
    print(c,temp,d)
  while(c!=0):
    lst.append(c%10)
    print(lst)
    c=c//10
  lst.reverse()
  lst=lst+d
  return lst

d=[9]
print(po(d))
"""
"""

# Nextpermutations
def np(a):
  i=j=len(a)-1
  # we find the breakele
  while(i>0 and a[i-1]>=a[i]):
    i-=1
  if i==0:
    a.reverse()
    return

  k=i-1 
  #we find ele that is next no.of k
  while(a[j]<=a[k]):
    j-=1
  #we swap to no.
  a[k],a[j]=a[j],a[k]
  #we have to sort the rest
  l=k+1
  r=len(a)-1
  while(l<r):
    a[l],a[r]=a[r],a[l]
    l+=1
    r-=1
  

a=[3,2,1]
np(a)
print(a)
"""
"""

# def maxProfit(prices):
#   min_val=float('inf')
#   print(min_val)
#   max_profit=0
#   for i in range(len(prices)):
#     if prices[i]<min_val:
#       min_val = prices[i]
#     if max_profit<prices[i]-min_val:
#       max_profit=prices[i]-min_val
#   return max_profit 

# prices=[7,1,4,5,6]
# print(maxProfit(prices) )

"""
"""
"""

# def mi(a):
#   i=0
#   while i<len(a)-1