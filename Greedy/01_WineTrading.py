# https://www.spoj.com/problems/GERGOVIA/
# Gergovia consists of one street, and every inhabitant of the city is a wine salesman. 
# Everyone buys wine from other inhabitants of the city. Every day each inhabitant 
# decides how much wine he wants to buy or sell. Interestingly, demand and supply is 
# always the same, so that each inhabitant gets what he wants.

# There is one problem, however: Transporting wine from one house to another results in work. 
# Since all wines are equally good, the inhabitants of Gergovia don't care which persons they are doing trade with, 
# they are only interested in selling or buying a specific amount of wine.

# In this problem you are asked to reconstruct the trading during one day in Gergovia. 
# For simplicity we will assume that the houses are built along a straight line with equal 
# distance between adjacent houses. Transporting one bottle of wine from one house to an adjacent house 
# results in one unit of work.


def f(arr):
    buy=[]
    sell=[]
    for i in range(len(arr)):
        if arr[i]>0:
            buy.append([arr[i],i])
        else:
            sell.append([arr[i],i])
    print(buy,sell)
    ans=0
    i=0 
    j=0 
    while(i<len(buy) and j<len(sell)):
        x=min(buy[i][0],-1*sell[j][0])
        buy[i][0]-=x 
        sell[j][0]+=x 
        ans+=x*(abs(buy[i][1]-sell[j][1]))
        if buy[i][0]==0:
            i+=1 
        if sell[j][0]==0:
            j+=1 
    return ans 
    
    
    
arr=[5,-4,1,-3,1]
print(f(arr))