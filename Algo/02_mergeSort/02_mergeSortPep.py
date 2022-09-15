def mergesort(arr,lo,hi):
    # bc
    if lo==hi: #only one element is there
        ba=[0]
        ba[0]=arr[lo]
        return ba
        
    mid=(lo+hi)//2
    fsh=mergesort(arr,lo,mid)
    ssh=mergesort(arr,mid+1,hi)
    fsa=merge(fsh,ssh)
    return fsa

def merge(arr1,arr2): 
    l1=len(arr1)
    l2=len(arr2)
    i=0
    j=0
    k=0
    res=[0]*(l1+l2)
    while(i<l1 and j<l2):
        if arr1[i]<arr2[j]:
            res[k]=arr1[i]
            i+=1 
        else:
            res[k]=arr2[j]
            j+=1 
        k+=1 
    
    while(i<l1):
        res[k]=arr1[i]
        i+=1 
        k+=1 
    
    while(j<l2):
        res[k]=arr2[j]
        j+=1 
        k+=1 
    
    return res 

arr=[7,4,1,3,6,8,2,5]
lo=0
hi=len(arr)-1
print(mergesort(arr,lo,hi))