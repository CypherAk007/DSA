# consider 0s as-1 and 1s as 1
def subarr(a,n):
    freq=0
    d={}
    d[0]=1
    s=0
    for i in range(n):
        if a[i]==0:
           s+=-1
        else:   
            s+=1
        if s in d:
            freq+=d[s]
            d[s]+=1
        else:
            d[s]=1
            
    return freq
    
a=[1,1,1,1,0]

n=len(a)
print(subarr(a,n))