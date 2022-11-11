# PRATA - Roti Prata
def bs(nc,ranks,orders):
    lo=0
    hi=1e8
    ans=0 
    while(lo<=hi):
        mid=lo+(hi-lo)//2
        #solve returns if we can make oreder no. of parathas in  mid time
        if solve(nc,ranks,orders,mid): 
            ans=mid
        # if we can make then we can also make all times above mid so checklower
            hi=mid-1 
        else:
            lo=mid+1 
    return ans
    
def solve(nc,ranks,orders,mid):
    time=0
    parathas=0
    for i in range(0,nc):
        # 1st chef
        time=ranks[i] # 1st paratha is made in rank time
        j=2 #check fm 2nd paratha
        while(time<=mid):
            parathas+=1 
            time+=ranks[i]*j 
            j+=1 
        if parathas>=orders:
            return 1 
    return 0
        

nc=4
ranks=[1,2,3,4]
orders=10
print(bs(nc,ranks,orders))