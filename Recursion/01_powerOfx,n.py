import sys
sys.setrecursionlimit(1500)

def powerLog(x, n):
# write your code here
    if n==0:
        return 1
    xpnb2=powerLog(x,n//2)
    xn=xpnb2*xpnb2
    if n%2==1:
        xn=xn*x
        
    return xn

num = int(input())
power = int(input())
print(powerLog(num, power))