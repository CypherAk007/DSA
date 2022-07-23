import heapq
def dist(x,y):
    return x*x+y*y 
    
# implenetation of max heap using max heap with distance as key
def kClosestToOrigin(a,k):
    heap=[]
    out=[]
    for i in a:
        distance=dist(i[0],i[1])
        heapq.heappush(heap,[-1*distance,[i[0],i[1]]])
        if len(heap)>k:
            heapq.heappop(heap)
    while len(heap)>0:
        out.append(heapq.heappop(heap)[1])
    return out
        
a=[[1,3],[-2,2],[5,8],[0,1]]
k=2
print(kClosestToOrigin(a,k))