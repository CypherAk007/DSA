# max area binary Matrix
def MABM(a,n,m):
    v=[]
    for j in range(0,m):
        v.append(a[0][j])
    mx=MAH(v)
    for i in range(1,n):
        for j in range(0,m):
            if a[i][j]==0:
                v[j]=0 
            else:
                v[j]=v[j]+a[i][j]
        mx=max(mx,MAH(v))
    return mx
    
# max area histogram
def MAH(a):
    v=[]
    out=[]
    A=NSL(a)
    # print(A)
    B=NSR(a)
    # print(B)
    for i in range(len(a)):
        v.append([a[i],A[i],B[i]])
    # print(v)
    for row in v:
        out.append(row[0]*(row[2]-row[1]-1))
    # print(out)
    return max(out)
def NSL(a):
    s=[]
    v=[]
    for i in range(len(a)):
        if len(s)==0:
            v.append(-1)
        elif len(s)>0 and s[-1][0]<a[i]:
            
            v.append(s[-1][1])
        elif len(s)>0 and s[-1][0]>=a[i]:
            while(len(s)>0 and s[-1][0]>=a[i]):
                s.pop()
            if len(s)==0:
                v.append(-1)
            else:
                v.append(s[-1][1])
        s.append([a[i],i])
    return v
        
def NSR(a):
    s=[]
    v=[]
    for i in range(len(a)-1,-1,-1):
        if len(s)==0:
            v.append(len(a))
        elif len(s)>0 and s[-1][0]<a[i]:
            
            v.append(s[-1][1])
        elif len(s)>0 and s[-1][0]>=a[i]:
            while(len(s)>0 and s[-1][0]>=a[i]):
                s.pop()
            if len(s)==0:
                v.append(len(a))
            else:
                v.append(s[-1][1])
        s.append([a[i],i])
    v.reverse()
    return v
        
        
# a=[100,80,60,70,60,75,85] 
a=[6,2,5,4,5,1,6]
# print(MAH(a))
a=[[0,1,1,0],[1,1,1,1],[1,1,1,1],[1,1,0,0]]
n=len(a)
m=len(a[0])
print(MABM(a,n,m))