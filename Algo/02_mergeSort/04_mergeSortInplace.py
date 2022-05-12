def mergesortinplace(arr,s,e):
    if e-s==1:
        return
    mid=(s+e)//2
    mergesortinplace(arr,s,mid)
    mergesortinplace(arr,mid,e)
    merge(arr,s,e,mid)
    
def merge(arr,s,e,mid):
    mix=[0]*(e-s)
    i=s
    j=mid
    k=0
    while(i<mid and j<e):
        if arr[i]<arr[j]:
            mix[k]=arr[i]
            i+=1
        else:
            mix[k]=arr[j]
            j+=1
        k+=1
        
    while(i<mid):
        mix[k]=arr[i]
        i+=1
        k+=1
        
    while(j<e):
        mix[k]=arr[j]
        j+=1
        k+=1
        
    for k in range(len(mix)):
        arr[s+k]=mix[k]
        
    
arr=[4,3,2,1,3,100,3]
mergesortinplace(arr,0,len(arr))
print(arr)