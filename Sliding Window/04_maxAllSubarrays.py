# Maximum of all subarrays of size k | Sliding Window| Fixed size as K is given

def maxOfAllSubArr(a,k):
    i=0
    j=0
    lst=[]
    maxi1=float('-inf')
    maxi2=float('-inf')
    while(j<len(a)):
        if a[j]>maxi1: 
            maxi2=maxi1
            maxi1=a[j]
        elif a[j]>maxi2:
            maxi2=a[j]
        print(a[j],maxi1,maxi2) 
        if (j-i+1)<k:
            j+=1
        elif (j-i+1)==k:
            lst.append(maxi1)
            print(lst)
            if a[i]==maxi1:
                maxi1=maxi2
                maxi2=float('-inf')
                print(maxi1,maxi2)
            elif a[i]==maxi2:
                maxi2=float('-inf')
            i+=1
            j+=1
    return lst
            
    
a=[1, 3, -1, -3, 5, 3, 6, 7]
k=1
print(maxOfAllSubArr(a,k))