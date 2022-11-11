def bs(arr,lo,hi,t):
    while(lo<=hi):
        mid = lo+(hi-lo)//2
        # print(lo,hi)
        # mid=(lo+hi)//2
        if arr[mid]==t:
            return mid 
        if arr[mid]>t:
            hi=mid-1 
        else:
            lo=mid+1 
    return -1 

def descbs(arr,lo,hi,t):
    while(lo<=hi):
        mid = lo+(hi-lo)//2
        if arr[mid]==t:
            return mid 
        if arr[mid]<t:
            hi = mid-1 
        else:
            lo=mid+1 
    return -1 

def oabs1(arr,lo,hi,t):
    if arr[lo]>arr[hi]:
        print("dec")
        return descbs(arr,lo,hi,t)
    else:
        print("asc")
        return bs(arr,lo,hi,t)

def oabs2(arr,lo,hi,t):
    desc=0
    if arr[lo]>arr[hi]:
        desc=1 
    while(lo<=hi):
        mid=lo+(hi-lo)//2 
        if arr[mid]==t:
            return mid 
        if desc:
            if arr[mid]<t:
                hi=mid-1 
            else:
                lo=mid+1 
        else:
            if arr[mid]<t:
                lo=mid+1 
            else:
                hi=mid-1 
    return -1 
    
# arr2=[2,4,6,8,10]
arr2=[10,8,6,4,2,1]
lo=0 
hi=len(arr2)-1 
t=10
# print(bs(arr2,lo,hi,t))
print(descbs(arr2,lo,hi,t))
# arr2=[10,8,6,4,2,1]
# lo=0 
# hi=len(arr2)-1 
# t=10
# # print(descbs(arr2,lo,hi,t))
print(oabs2(arr2,lo,hi,t))
