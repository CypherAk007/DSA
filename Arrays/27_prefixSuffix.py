def prefixSum(a):
    for i in range(1,len(a)):
        a[i]=a[i]+a[i-1]
    return a

def suffixSum(a):
    for i in range(len(a)-2,-1,-1):
        a[i]=a[i]+a[i+1]
    return a    

def prefixMax(a):
    
    for i in range(1,len(a)):
        a[i]=max(a[i],a[i-1])
    print(a)
    
def suffixMax(a):
    for i in range(len(a)-2,-1,-1):
        a[i]=max(a[i],a[i+1])
    print(a)

# a=[1,2,3,0,3]
# p=prefixSum(a)
# print(a)
# a=[1,2,3,0,3]
# s=suffixSum(a)
# print(a)
# for i in range(len(p)):
#     if p[i]==s[i]:
#         print('Equilibrium point')
#         print(p[i],i)
#         break
a=[0,1,0,2,1,0,1,3,2,1,2,1]
prefixMax(a)
a=[0,1,0,2,1,0,1,3,2,1,2,1]
suffixMax(a)