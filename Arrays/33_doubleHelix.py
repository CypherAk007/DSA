def doubleHelix(arr1,n,arr2,m):
    s1=0
    s2=0
    i=0
    j=0
    mxsum=0
    while(i<n and j<m):
        if arr1[i]<arr2[j]:
            s1+=arr1[i]
            i+=1 
        elif arr1[i]>arr2[j]:
            s2+=arr2[j]
            j+=1 
        else:
            mxsum+=max(s1,s2)
            mxsum+=arr1[i]
            s1=0
            s2=0
            i+=1 
            j+=1 
    
    while(i<n):
        s1+=arr1[i]
        i+=1 
    while(j<m):
        s2+=arr2[j]
        j+=1
    mxsum+=max(s1,s2)
    return mxsum
    
    
    
arr1=[3,5,7,9,20,25,30,40,55,56,57,60,62]
arr2=[1,4,7,11,14,25,44,47,55,57,100]
print(doubleHelix(arr1,len(arr1),arr2,len(arr2)))