# Find the first repeated word in a string
def findfirstrep(s):
    d={}
    i=0
    j=0
    s=s+' '
    while(j<len(s)):
        if s[j]==" ":
            if s[i:j] in d:
                d[s[i:j]][0]+=1 
            else:
                d[s[i:j]]=[1,i]
            i=j+1 
            j=j+1 
        else:
            j+=1 
    print(d)
    for k,v in d.items():
        if v[0]>1:
            return k 
    
    return -1 

s="he had had he"
print(findfirstrep(s))
