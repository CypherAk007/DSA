a=[3,4,7,2,-3,1,4,2]
k=7
c=0

for i in range(len(a)):
    summ=0
    for j in range(i,len(a)):
        summ+=a[j]
        if summ==k:
            c+=1 
print(c)


def bsol(a,k):
    c=0
    for start in range(len(a)):
        for end in range(start+1,len(a)+1):
            summ=0
            for i in range(start,end):
                summ+=a[i]
            if summ==k:
                c+=1 
    return c 
a=[3,4,7,2,-3,1,4,2]
k=7    
print(bsol(a,k))
    
def mapsol(a,k):
    c=0
    s=0
    d={}
    d[0]=1
    for i in range(len(a)):
        s+=a[i]
        if s-k in d:
            c+=d[s-k]
        if s in d:
            d[s]+=1
        else:
            d[s]=1 
    return c 
a=[3,4,7,2,-3,1,4,2]
k=7
print(mapsol(a,k))