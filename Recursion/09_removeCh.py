def remove(s,target,idx):
    if idx==len(s):
        return s
    
    if s[idx]==target:
        ch=s[:idx]
        ros=s[idx+1:]
        s=ch+ros
        out=remove(s,target,idx)
        return out
        
    else:
        out=remove(s,target,idx+1)
        return out

def remove2(s,target):
    if len(s)==0:
        return ""
    
    ch=s[0]
    
    if ch==target:
        out=remove2(s[1:],target)
        return out
    
    else:
        out=remove2(s[1:],target)
        return ch+out
    
    
    
s='bacacad'
target='a'
idx=0
# print(remove(s,target,idx))
# print(s)
print(remove2(s,target))