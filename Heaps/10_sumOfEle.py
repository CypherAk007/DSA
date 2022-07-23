import heapq
def findkthSmallest(a,k):
    heap=[]
    for i in range(len(a)):
        heapq.heappush(heap,-1*a[i])
        if len(heap)>k:
            heapq.heappop(heap)
    return -1*heap[0]
    
def main(a,k1,k2):
    x1=findkthSmallest(a,k1)
    x2=findkthSmallest(a,k2)
    print(x1,x2)
    out=0
    for i in range(len(a)):
        if a[i]>x1 and a[i]<x2:
            out+=a[i]
    return out
        
a=[1,3,5,11,12,15]
k1=3
k2=6
print(main(a,k1,k2))