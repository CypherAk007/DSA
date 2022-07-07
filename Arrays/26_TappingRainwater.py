# Tapping rainwater
# Bruteforce - find the left max,rightmax and minof both and sub with current height=waterStoredin that node
def waterStored(a):
    tot=0
    lMax=0
    rMax=0
    for k in range(len(a)):
        lMax=0
        rMax=0
        for i in range(k,-1,-1):
            lMax=max(lMax,a[i])
        
        for i in range(k,len(a)):
            rMax=max(rMax,a[i])
        mini=min(lMax,rMax)
        tot+=mini-a[k]
        
    return tot


a=[0,1,0,2,1,0,1,3,2,1,2,1]
print(waterStored(a))