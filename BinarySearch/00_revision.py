
def findPeak(arr):
  l=0
  h=len(arr)-1
  while(l<h):
    mid=l+(h-l)//2
    print(l,mid,h)
    if arr[mid]>arr[mid+1]:
      # dec part
      h=mid 
    else: #asc part
      l=mid+1
  return l 
  
def bs(arr,s,e,t):
    if arr[s]<arr[e]:
        isasc=True
    else:
        isasc=False
    
    while(s<=e):
        
        m=s+(e-s)//2
        print(s,e,m)
        if arr[m]==t:
            print(arr[m])
            return m 
        if isasc:
            if arr[m]>t:
                l=m+1 
            else:
                h=m-1
        else:
            if arr[m]<t:
                l=m+1 
            else:
                h=m-1
    return -1 
    
def findInMount(arr,t):
    peak=findPeak(arr)
    l=bs(arr,0,peak,t)
    if l==-1:
        r=bs(arr,peak+1,len(arr)-1,t)
        return r
    return l
    
def findPivot(a):
    s=0
    e=len(a)-1 
    m=s+(e-s)//2
    if m<e and a[m]>a[m+1]:
        print(m,a[m])
        return m #pivot found
    if m>s and a[m]<a[m-1]:
        print(m-1,a[m-1])
        return m-1
    if a[m]<=a[s]:
        e=m-1 
    else:
        s=m+1 
    return -1 
    
def bs2(nums,start,end,target):
  
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
       
def findTar(nums,t):
    pivot=findPivot(nums)
    if pivot==-1:
        return bs2(nums,0,len(nums)-1,t)
    if nums[pivot]==t:
        return pivot
    if t>=nums[0]:
        print('1')
        return bs2(nums,0,pivot-1,t)
    else:
        return bs2(nums,pivot+1,len(nums)-1,t)
    
arr=[4,5,6,7,0,1,2]
# print(findPeak(arr))
t=3
# print(findInMount(arr,t))
print(findTar(arr,t))