def permutations(p,up):
    if len(up)==0:
        print(p)
        return
    ch=up[0]
    # _a_b_c_ so len(p)+1
    for i in range(len(p)+1):
        first=p[0:i]
        second=p[i:len(p)]
        permutations(first+ch+second,up[1:])
    
    
def perarrlst(p,up):
    if len(up)==0:
        lst=list()
        lst.append(p)
        return lst
    ch=up[0]
    ans=list()
    for i in range(len(p)+1):
        first=p[0:i]
        second=p[i:len(p)]
        out=perarrlst(first+ch+second,up[1:])
        ans+=out
    return ans


p=''
up='aaa'
permutations(p,up)
