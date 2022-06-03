# Brute force O(n^3 logm)->log m- timetaken to insert into set
def bf3sum(a):
  n=len(a)
  out=set()
  for i in range(n-1):
    for j in range(i+1,n-1):
      for k in range(j+1,n-1):
        if a[i]+a[j]+a[k]==0:
          lst=(a[i],a[j],a[k])
          t=sorted(lst)
          print(t)
          out.add(tuple(t))
  return out

# Better approach Tc- O(n^2 log m) sc-O(m)+O(n)
# make dict store k-element v- no. of occurance of that ele
# a+b+c=0 c=-(a+b)
#  we have to remove the used element fm dict and added later after op is done for the next iter.
# The triplet is (a[i],a[j],-(a[i]+a[j]))
def be3sum(a):
  d={}
  for i in a:
    if i in d:
      d[i]+=1
    else:
      d[i]=1
  n=len(a)
  res=set()
  for i in range(0,n-1):
    d[a[i]]-=1
    for j in range(i+1,n-1):
      d[a[j]]-=1
      if (-(a[i]+a[j]) in d):
        if d[-(a[i]+a[j])]>0:
          lst=(a[i],a[j],-(a[i]+a[j]))
          t=sorted(lst)
          res.add(tuple(t))
      d[a[j]]+=1
    d[a[i]]+=1
  # print(d)
  return res

# optimized approach
def threeSum(num):
  num.sort()
  # print(num)
  res=[]
  for i in range(0,len(num)-2):#till the third last guy
    if i==0 or (i>0 and num[i]!= num[i-1]):# 'a' should not be same as prev
      lo=i+1
      hi=len(num)-1
      su=0-num[i]#-a
      # two ptr approach
      while (lo<hi):
        if (num[lo]+num[hi]== su):
          res.append([num[i],num[lo],num[hi]])#res is appended
          # all the similar lows and highs are skipped
          while(lo<hi and num[lo]== num[lo+1]):lo+=1
          while(lo<hi and num[hi]== num[hi-1]):hi-=1
          
          lo+=1
          hi-=1
        elif (num[lo]+num[hi]<su):
          lo+=1
        else:
          hi-=1
  return res  


a=[-1,0,1,2,-1,-4]
# a=[0,0,0]
# print(bf3sum(a))
# print(be3sum(a))
print(threeSum(a))