
def longSubStrKUniqueChar(s,k):
    i=0
    j=0
    mx=float('-inf') #stores the max window size (max size of subarr of value = k)
    d={}
    while(j<len(s)):
        
        # 1-> calculations 
        if s[j] in d:
            d[s[j]]+=1 
        else:
            d[s[j]]=1 

        if (len(d))<k: # cond? => length of dictionary
            j+=1
        
        elif (len(d))==k: 
            
        # if no. of uniquechar == k then compare the ws with mx
            mx = max(mx,j-i+1)
            j+=1 # we are moving the pointer to find more elements for greater ws
            
        elif (len(d))>k:
            while (len(d))>k: # still len(d)<=k remove ith element from front
                d[s[i]]-=1 
                # if any element(key) in d ==0 then remove it fm d to dec. the len(d)
                if d[s[i]]==0:
                    d.pop(s[i])
                i+=1 
            
            j+=1
            
    if mx==float('-inf'):
        return 0
    return mx
            

s='aabacbebebe'
k=3 # no.of unique char in substr = 3
print(longSubStrKUniqueChar(s,k))

# Input 1:
# s='aabacbebebe'
# k=3 # no.of unique char in substr = 3
# Output 1:
#     C = 7 #max substr size