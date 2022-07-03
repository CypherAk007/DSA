# Minimum Window Substring  | Variable Size Sliding Window

def minWinSubStr(s,t):
    j=0
    i=0
    mini=float('inf') #stores the max window size (max size of subarr of value = k)
    d={}
    start=0 # tomove the optimize ptr
    # here we make map of t string for future use
    for i in range(len(t)):
        if t[i] in d:
            d[t[i]]+=1 
        else:
            d[t[i]]=1
    count=len(d) #tells the no. of unique char in the t string
    # print(d,count)
    
    while(j<len(s)):
        
        # 1-> calculations 
        # we check if there is s[i] in d if there then we dec it
        if (count>0): # cond? => count of var satisified/got
            if s[j] in d:
                d[s[j]]-=1
                if d[s[j]]==0:
                    count-=1
            j+=1
            
        
        elif (count== 0): 
            # now we got the ans now we try to optimize it by moving the ith ptr
            mini = min(mini,j-i+1)
            start=i
            while(count==0):
                if s[i] in d:
                    d[s[i]]+=1
                    if d[s[i]]>0:
                        count+=1
                    i+=1
                else:
                    i+=1
                if count==0:
                    mini = min(mini,j-i+1)
    
    if mini==float('inf'):
        return 0
    return mini
            

s="ADOBECODEBANC"
t="ABC"
print(minWinSubStr(s,t))

# Input 1:
# Input: s = 'totmtaptat'
# k='tta'
# Output: 3
# Explanation: The answer is "TAT" last three letters which is min


# Example 2:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"-(4)
