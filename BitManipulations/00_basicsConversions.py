def decimalToBinary(n): 
    return bin(n).replace("0b", "") 
def dtb(n):
    if n<1:
        return ''
    val = dtb(n//2)
    val+=str(n%2)
    return val
def btd(n):
    dec = 0 
    i = 0 
    while(n>0):
        d =n%10
        dec+= d*pow(2,i)
        i+=1 
        n//=10
    return dec
# Driver code 
if __name__ == '__main__': 
    print(decimalToBinary(8),type(decimalToBinary(8))) 
    print(decimalToBinary(18)) 
    print(decimalToBinary(7)) 
    out = dtb(18)
    print(out,type(out))
    print(btd(101),type(btd(101)))