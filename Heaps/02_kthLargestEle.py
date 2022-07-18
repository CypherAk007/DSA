import heapq

def kthLargest(a,k):#heap - min heap
    heap=[]
    for i in range(len(a)):
        heapq.heappush(heap,a[i])
        while(len(heap)>k):
            heapq.heappop(heap)
    return heap[0]
    
    
a=[7,10,4,3,20,15]
k=3
# op->10 - kth largest element


print(kthLargest(a,k))
