import heapq

def kthSmallest(a,k):#use max heap but in py no max heap so gimmic
    heap=[]
    for i in range(len(a)):
        heapq.heappush(heap,-1*a[i])
        while(len(heap)>k):
            heapq.heappop(heap)
    return abs(heap[0])


a=[7,10,4,3,20,15]
k=3
# op->7 kth smallest element
print(kthSmallest(a,k))