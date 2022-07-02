# Maximum Sum Subarray of size K | Sliding Window | Fixed size as K is given

def mxSubarray(a,k):
    i=0
    j=0
    summ=0
    maxi=float('-inf')
    while(j<len(a)):
        summ+=a[j]
        if (j-i+1)<k:
            j+=1
        elif (j-i+1==k):
            # print(a[i],a[j])
            maxi = max(maxi,summ)
            # print(maxi,summ)
            # removes the 1st element of window so that nxt ele is added and window is maintained
            summ-=a[i] 
            i+=1
            j+=1
    return maxi        

a=[2,5,1,8,2,9,1]
k=3
print(mxSubarray(a,k))