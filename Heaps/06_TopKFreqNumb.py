import heapq
def topKFreqNum(a,key):
    heap=[]
    d={}
    for i in range(len(a)):
        if a[i] in d:
            d[a[i]]+=1 
        else:
            d[a[i]]=1 
    # print(d)
    # make min heap k=freq and val=arr[i]
    for k,v in d.items():
        heapq.heappush(heap,[v,k])
        while len(heap)>key:
            heapq.heappop(heap)

    while(len(heap))>0:
        print(heap[0][1])
        heapq.heappop(heap)
        
a=[1,1,1,3,2,2,4]
k=2
topKFreqNum(a,k)