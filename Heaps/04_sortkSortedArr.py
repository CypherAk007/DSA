import heapq

def sortKele(a,k):
    heap=[]
    out=[]
    for i in range(len(a)):
        heapq.heappush(heap,a[i])
        while(len(heap)>k):
            out.append(heapq.heappop(heap))
    while(len(heap)>0):
        out.append(heapq.heappop(heap))
    
    print(out)
    return out
    
def sortKele2(a,k):
    heap=[]
    out=[]
    for i in range(len(a)):
        heapq.heappush(heap,a[i])
        while(len(heap)>k):
            out.append(heap[0])
            heapq.heappop(heap)
    while(len(heap)>0):
        out.append(heap[0])
        heapq.heappop(heap)
    print(out)
    return out
a=[6,5,3,2,8,10,9]
k=3
# op->10,15,20 - k larger element
sortKele2(a,k)