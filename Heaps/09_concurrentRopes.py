import heapq

def ccRopes(a):
    heap=[]
    out=0
    for i in range(len(a)):
        heapq.heappush(heap,a[i])
    while(len(heap)>=2):
        var1=heapq.heappop(heap)
        var2=heapq.heappop(heap)
        var3=var1+var2
        out+=var3
        heapq.heappush(heap,var3)
    return out
        
a=[1,2,3,4,5]
print(ccRopes(a))