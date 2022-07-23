import heapq
def FreqSort(a):
    heap=[]
    d={}
    out=[]
    for i in range(len(a)):
        if a[i] in d:
            d[a[i]]+=1 
        else:
            d[a[i]]=1 
    print(d)
    # make max heap k=freq and val=arr[i]
    for k,v in d.items():
        heapq.heappush(heap,[-1*v,k])
    print(heap) 
    while len(heap)>0:
        x=heapq.heappop(heap)
        out+=[x[1]]*abs(x[0])
    print(out)
    
        
a=[1,1,1,3,2,2,4]
k=2
FreqSort(a)