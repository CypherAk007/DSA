

# First Negative Number in every Window of Size K | Sliding Window| Fixed size as K is given

def fstNegtivNo(a,k):
    i=0
    j=0
    lst=[]# stores the first Negative numbers
    out=[]# store the output
    while(j<len(a)):
        if a[j]<0:
            lst.append(a[j])
        if (j-i+1)<k:
            j+=1
        elif (j-i+1)==k:
            if len(lst)==0:
                out.append(0)
            else:
                out.append(lst[0])#this contains fstNegtivNo
                # move the window by removing the ith ele fm lst if exists and then i++ i.e 
                if a[i]==lst[0]:
                    lst.pop(0) # remove wrt index
            i+=1
            j+=1
    return out
                    
            
    
    

a=[12,-1,-7,8,-15,30,16,28]
k=3
print(fstNegtivNo(a,k))
# [-1, -1, -7, -15, -15, 0]