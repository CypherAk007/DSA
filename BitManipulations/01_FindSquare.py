# Q -> https://www.geeksforgeeks.org/calculate-square-of-a-number-without-using-and-pow/

def calcSqr(n):
    temp = abs(n)
    pos = 0 
    res = 0 
    while(temp):
        if (temp&1):
            res+=n<<pos
        pos+=1 
        temp = temp>>1
    return res 


    
n = 25 
print(calcSqr(n))