
# stocks Span
# find the ngl - index  and i-index
# stack-[a[i],i]
def stockSpan(a):
    s=[]
    v=[]
    for i in range(len(a)):
        if len(s)==0:
            v.append(-1)
        elif len(s)>0 and s[-1][0]>a[i]:
            v.append(s[-1][1])
        elif len(s)>0 and s[-1][0]<=a[i]:
            while len(s)>0 and s[-1][0]<=a[i]:
                s.pop()
            if len(s)==0:
                v.append(-1)
            else:
                v.append(s[-1][1])
        s.append([a[i],i])
 
    for i in range(len(v)):
        v[i]=i-v[i]
    return v
    
    
a=[100,80,60,70,60,75,85]
print(stockSpan(a))