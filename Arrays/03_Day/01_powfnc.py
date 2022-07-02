def power(x,n):
    ans = 1.0
    nn = n
    if n<0:
        nn*=-1
    while(nn>0):
        if nn%2==1:
            ans*=x
            nn-=1
        else:
            x*=x
            nn=nn//2
    if n<0:
        return 1/ans
    return ans
          
          
x=2 
n=-10
print(power(x,n))