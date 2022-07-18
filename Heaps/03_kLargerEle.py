import heapq

def kLarger(a,k):#heap - min heap
    heap=[]
    for i in range(len(a)):
        heapq.heappush(heap,a[i])
        while(len(heap)>k):
            heapq.heappop(heap)
    while(len(heap)>0):
        print(heap[0])
        heapq.heappop(heap)
    
    
a=[7,10,4,3,20,15]
k=3
# op->10,15,20 - k larger element
kLarger(a,k)