# special no - 123
# 1^4+2^4+3^4 and 1*2*3
# gcd(both)>1
# count +=increment 
# return count

import math

def gcd(a,b):
    while(b):
        a,b=b,a%b
    return a
    
def quadraticPow(n):
    tempNo=n
    s=0
    while tempNo!=0:
        modNo=int(tempNo%10)
        # print(modNo)
        s= s+math.pow(modNo,4)
        tempNo//=10
        # print(tempNo)
    # print(s)
    return s
    
def multipleOfDigits(n):
    tempNo=n
    s=1
    while tempNo!=0:
        modNo=int(tempNo%10)
        # print(modNo)
        s*=modNo
        tempNo//=10
        # print(tempNo)
    # print(s)
    return s
    
def findSpecialNumberCount(n):
    tempOut=0
    for i in range(1,n+1):
        
        currentNumber=i
        # print(currentNumber)
        quadratic=quadraticPow(currentNumber)
        # print(quadratic)
        multiple=multipleOfDigits(currentNumber)
        # print(multiple)
        hcf=gcd(quadratic,multiple)
        # print(hcf)
        if hcf>1:
            tempOut+=1
    return tempOut
            
print(findSpecialNumberCount(101))