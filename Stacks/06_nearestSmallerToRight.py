def nearestSmallerToRight(a):
    s=[]
    out=[]
    for i in range(len(a)-1,-1,-1):
        if len(s)==0:
            out.append(-1)
        elif len(s)>0 and s[-1]<a[i]:
            out.append(s[-1])
        elif len(s)>0 and s[-1]>=a[i]:
            while(len(s)>0 and s[-1]>=a[i]):
                s.pop()
            if len(s)==0:
                out.append(-1)
            else:
                out.append(s[i])
        s.append(a[i])
    out.reverse()
    return out

a=[4,5,2,10,8]
print(nearestSmallerToRight(a))