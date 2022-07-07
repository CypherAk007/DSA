
def mergeSort(a):
    if len(a)==1:
        return a
    mid = len(a)//2
    leftarr=a[:mid]
    left=mergeSort(leftarr)
    rightarr =a[mid:]
    right=mergeSort(rightarr)
    return merge(left,right)
    
def merge(first,second):
    mix = [0 for i in range(len(first)+len(second))]
    # print(mix)
    i=0
    j=0
    k=0
    while(i<len(first) and j<len(second)):
        if (first[i]<second[j]):
            mix[k]= first[i]
            i+=1 
        else:
            mix[k]=second[j]
            j+=1 
        k+=1 
    while(i<len(first)):
        mix[k]=first[i]
        i+=1 
        k+=1
    while(j<len(second)):
        mix[k]=second[j]
        j+=1 
        k+=1

    return mix

a=[5,4,3,2,1]
print(mergeSort(a))