def rotate(s):
    temp=s[-1]+s[:-1]
    return temp
    
def check(s1,s2):
    n=len(s1)
    count=0
    while(count<n):
        s2=rotate(s2)
        print(s1,s2,count)
        if s1==s2:
            return True
        else:
            count+=1
    return False
    
    
s1='ABCD'
s2='CADB'
print(check(s1,s2))