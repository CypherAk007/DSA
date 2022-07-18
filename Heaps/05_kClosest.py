import heapq
def kClosest(a,x,k):
    heap=[]
    for i in range(len(a)):
        heapq.heappush(heap,[-1*abs(a[i]-x),a[i]])
        if len(heap)>k:
            heapq.heappop(heap)
             
    while len(heap)>0:
        print(heap[0][1])
        heapq.heappop(heap)
        
a=[5,6,7,8,9]
x=7
k=3
kClosest(a,x,k)