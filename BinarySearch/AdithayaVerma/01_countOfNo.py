def fobs(arr,lo,hi,t):
    res = -1
    while(lo<=hi):
        mid = lo+(hi-lo)//2
        if arr[mid]==t:
            res=mid 
            hi=mid-1 
        if arr[mid]<t:
            lo=mid+1
        else:
            hi=mid-1
    return res

def lobs(arr,lo,hi,t):
    res=-1 
    while(lo<=hi):
        mid=lo+(hi-lo)//2
        if arr[mid]==t:
            res=mid 
            lo=mid+1 
        if t<arr[mid]:
            hi=mid-1 
        else:
            lo=mid+1
    return res
    
arr=[2,8,8,10,12,14,14,14]
lo=0 
hi=len(arr)-1 
t=14
x=fobs(arr,lo,hi,t)
y=lobs(arr,lo,hi,t)
print(x,y)
z=abs(x-y)+1
print(z)

