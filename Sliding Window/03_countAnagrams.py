# Count Occurrences Of Anagrams | Sliding Window| Fixed size as K is given

def countOfOccAnagrams(s,p):
    i=0
    j=0
    ans = 0 # stores the count of the answers
    k=len(p)#window size
    # make dictionary for pattern
    d={}
    for x in range(k):
        if s[x] in d:
            d[s[x]]+=1
        else:
            d[s[x]]=1
    
    # make count varible i.e len(map)
    count = len(d)
    
    while(j<len(s)):
        if s[j] in d and d[s[j]]>=0:
            d[s[j]]-=1
            
            if d[s[j]]==0:
                count-=1
                
        
        #ws<k
        if (j-i+1)<k:
            
            j+=1
            
        #ws==k
        elif (j-i+1)==k:
            
            #anagram has matched
            if count==0:
                ans+=1
                
            
            #slide window
            #if ith letter in d then increment- remove ith calc
            if s[i] in d:
                d[s[i]]+=1
                # if ith letter was 0 before and inc and became 1
                # the count also should increment as letter is back
                if d[s[i]]==1:
                    count+=1
            
            i+=1 
            j+=1

    return ans
            
             
# s='forxxorfxdofr'        
# p='for'
# Explanation: for, orf and ofr appears
# in the txt, hence answer is 3.
    

s='aabaabaa'
p='aaba'
# Explanation: aaba is present 4 times
print(countOfOccAnagrams(s,p))