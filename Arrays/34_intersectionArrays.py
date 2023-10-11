def intersection(a,b):
    n=len(a)
    m=len(b)
    res=[]
    i=j=0
    while(i<n and j<m):
        if a[i]<b[j]:
            i+=1 
        elif b[j]<a[i]:
            j+=1
            
        else:
            if(len(res)==0):
                res.append(a[i])
                i+=1 
                j+=1 
            else:
                if res[len(res)-1]!=a[i]:
                    res.append(a[i])
                i+=1 
                j+=1 
    return res
    
# a=[3,5,8]
# b=[2,8,9,10,15]

a=[1,1,3,3,3]
b=[1,1,1,1,3,5,7]
print(intersection(a,b))
