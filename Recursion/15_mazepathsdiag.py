def pathRetPathDiag(p,r,c):
    if r==1 and c==1:
        lst=[]
        lst.append(p)
        return lst
    
    l=list()    
    if r>1 and c>1:
        l+=pathRetPathDiag(p+'D',r-1,c-1)
        
    if r>1:
        l+=pathRetPathDiag(p+'V',r-1,c)
    
    if c>1:
        l+=pathRetPathDiag(p+'H',r,c-1)
        
    return l
print(pathRetPathDiag('',3,3))