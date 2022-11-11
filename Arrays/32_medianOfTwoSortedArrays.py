def medianOfSortedArrays(arr1,arr2): 
    l1=len(arr1)
    l2=len(arr2)
    i=0
    j=0
    k=0
    res=[0]*(l1+l2)
    c=0
    while(i<l1 and j<l2 and c<=l1):
        if arr1[i]<arr2[j]:
            res[k]=arr1[i]
            i+=1 
        else:
            res[k]=arr2[j]
            j+=1 
        k+=1 
        c+=1
    
    while(i<l1 and c<=l1):
        res[k]=arr1[i]
        i+=1 
        k+=1 
        c+=1
    
    while(j<l2 and c<=l1):
        res[k]=arr2[j]
        j+=1 
        k+=1 
        c+=1
    print(res)
    return (res[l1]+res[l1-1])//2
    
    
a1=[1,12,15,26,38]
a2=[2,13,17,30,45]
print(medianOfSortedArrays(a1,a2))