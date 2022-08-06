# Two Sum
def twoSum(arr,t):
  d={}
  res=[]
  for i in range(len(arr)):
    a=t-arr[i]
    if a in d:
      res.append([d[a],i])
    else:
      d[arr[i]]=i 
    print(d)
  return res 

def sortedColors(a):
  l=0
  h=len(a)-1
  m=0
  while(m<=h):
    if a[m]==0:
      a[l],a[m]=a[m],a[l]
      m+=1 
      l+=1
    elif a[m]==1:
      m+=1
    elif a[m]==2:
      a[h],a[m]=a[m],a[h]
      h-=1 

def ms(a,l,h):
  if l<h:
    mid=l+(h-l)//2
    ms(a,l,mid)
    ms(a,mid+1,h)
    merge(a,l,mid,h)

def merge(a,L,mid,H):
  n1=mid-L+1#no. of ele
  n2=H-mid 
  
  l=[0]*n1 
  r=[0]*n2 
  for i in range(n1):
    l[i]=a[L+i]
  for j in range(n2):
    r[j]=a[mid+1+j]

  i=0
  j=0
  k=l
  while(i<n1 and j<n2):
    if l[i]<=r[j]:
      a[k]=l[i]
      i+=1
    else:
      a[k]=r[j]
      j+=1
    k+=1

  while(i<n1):
    a[k]=l[i]
    i+=1
    k+=1
  
  while(j<n2):
    a[k]=r[j]
    j+=1
    k+=1


def countPairs(a,n,k):
  d={}
  count=0
  for i in range(n):
    if k-a[i] in d:
      count+=d[k-a[i]]
    if a[i] in d:
      d[a[i]]+=1
    else:
      d[a[i]]=1
  return count

def validPalindrome(a):
    i=0
    j=len(a)-1
    while(i<j):
        if a[i]!=a[j]:
            return palindrome(a,i,j-1) or palindrome(a,i+1,j)
        i+=1 
        j-=1 
    print('out1')
    return True

def palindrome(a,i,j):
    while(i<j):
        if a[i]!=a[j]:
            return False
        i+=1 
        j-=1 
    return True
    
    
def firstOcc(a,idx,t):
    if idx==len(a):
        return -1
    if a[idx]==t:
        return idx
    else:
        return firstOcc(a,idx+1,t)
def firstOcc2(a,idx,t):
    if idx==len(a):
        return -1
    x=firstOcc2(a,idx+1,t)
    if a[idx]==t:
        x=idx
    return x 
        
import math
from turtle import right
def reverseNo(n):
    
    digits=math.log10(n)
    return helper(n,int(digits)+1)
    
def helper(n,digits):
    if n<=0:
        return 0
    rem=n%10
    n=n//10
    curr=rem*(int)(math.pow(10,digits-1))
    prev=helper(n,digits-1)
    return curr+prev
    
from copy import copy
def pattern(r,c,temp,res):
    if r==0:
        return res 
    # temp=[]
    if c<r:
        # temp.append('X')
        print('x',end=' ')
        temp.append('x')
        return pattern(r,c+1,temp,res)
    else:
        print('\n')
        res.append(copy(temp))
       
        temp=[]
        return pattern(r-1,0,temp,res)

def subset(p,up):
  if len(up)==0:
    lst=[]
    lst.append(p)
    return lst 
  ch=up[0]
  left=subset(p+ch,up[1:])
  right=subset(p,up[1:])
  return left+right

def perm(p,up):
  if len(up)==0:
    # print(p)
    # return
    lst=[]
    lst.append([p])
    return lst 
  ch=up[0]
  lst=[]
  for i in range(len(p)+1):
    f=p[0:i]
    s=p[i:]
    # lst+=perm(f+ch+s,up[1:])
    lst+=perm(f+ch+s,up[1:])
  return lst
# print(perm('','abc'))

def printAllMazePaths(p,maze,r,c):
  if r==len(maze)-1 and c==len(maze[0])-1:
    print(p)
    return 
  if maze[r][c]==False:
    return 
  
  maze[r][c]=False
  if r<len(maze)-1:
    printAllMazePaths(p+'D',maze,r+1,c)

  if c<len(maze[0])-1:
    printAllMazePaths(p+'R',maze,r,c+1)
  
  if c>0:
    printAllMazePaths(p+'L',maze,r,c-1)

  if r>0:
    printAllMazePaths(p+'U',maze,r-1,c)
  
  maze[r][c]=True 

def longestConsiquitive(a):
    d={}
    for i in range(len(a)):
        if a[i] in d:
            d[a[i]]+=1 
        else:
            d[a[i]]=1 
    longestStreak=0
    currentStreak=0
    for i in range(len(a)):
        if a[i]-1 not in d:
            currNo=a[i]
            currentStreak=1 
            while currNo+1 in d:
                currNo+=1 
                currentStreak+=1 
        longestStreak=max(longestStreak,currentStreak)
    return currentStreak
    
def longestPalinss(a):
    res=""
    resLen=0
    for i in range(len(a)):
        l,r=i,i 
        while l>=0 and r<len(a) and a[l]==a[r]:
            if r-l+1>resLen:
                res=a[l:r+1]
                resLen=r-l+1 
            l-=1 
            r+=1 
        l,r=i,i+1 
        while l>=0 and r<len(a) and a[l]==a[r]:
            if r-l+1>resLen:
                res=a[l:r+1]
                resLen=r-l+1 
            l-=1 
            r+=1 
    return res
            
a='abccbbbbba'            
print(longestPalinss(a))

# a=[100,4,200,1,3,2]
# print(longestConsiquitive(a)) 

# maze=[[True,True,True],
# [True,True,True],
# [True,True,True]]
# printAllMazePaths('',maze,0,0)

# print(subset('','abc'))
  
# print(pattern(4,0,[],[]))

# n=1234
# print(reverseNo(n))

# a=[2,3,6,9,8,3,2,6,2,4]
# idx=0
# t=8
# print(firstOcc(a,idx,t))
# print(firstOcc2(a,idx,t))

# a='abca'
# print(validPalindrome(a))


# a=[1,5,7,1]
# n=len(a)
# k=6
# print(countPairs(a,n,k))

# a=[6,5,3,1,8,7,2,4]
# l=0
# h=len(a)-1
# ms(a,l,h)
# print(a)
# a=[0,2,2,0,1,2,0,1,2]
# sortedColors(a)
# print(a)

# arr=[2,6,3,9,11,3]
# print(twoSum(arr,9))
    