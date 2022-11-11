
def boyerMoore(p,s):
    # 1-> construct the table
    # value = len-curridx-1
    # last value=len 
    n=len(p)
    d={}
    for i in range(n):
        if i!=n-1:
            d[p[i]]=n-i-1 
        else:
            d[p[i]]=n 
    d['*']=n 
    print(d)
# 2,3->
    i=n-1 
    j=n-1
    cur=i
    while(i<len(s)):
        # print(i,j,cur)
        if j<0:
            return i+1 
        if s[i]==p[j]:
            i-=1 
            j-=1 
        else:
            x=0
            if s[cur] not in d:
                x=d['*']
            else:
                x=d[s[cur]]
            i=cur+x
            # print(x,cur,i,s[i],'@@@@')
            j=n-1 
            cur=i 
    return -1 
        

p='TEAMMAST'
s='WELCOMETOTEAMMAST'
print(boyerMoore(p,s))

# s='AAAXAAAAA'
# p='AAAA'
# print(boyerMoore(p,s))