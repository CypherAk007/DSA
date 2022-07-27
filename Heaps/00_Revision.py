# kth largest- min heap
import heapq
def kthLargest(a,k):
  heap=[]
  for i in range(len(a)):
    heapq.heappush(heap,a[i])
    if len(heap)>k:
      heapq.heappop(heap)
  return heap[0]

def kthSmallest(a,k):
  heap=[]
  for i in range(len(a)):
    heapq.heappush(heap,-1*a[i])
    if len(heap)>k:
      heapq.heappop(heap)
  return -1*heap[0]

def sortkSorted(a,k):
  heap=[]
  out=[]
  for i in range(len(a)):
    heapq.heappush(heap,a[i])
    if len(heap)>k:
      out.append(heapq.heappop(heap))
  while(len(heap)>0):
    out.append(heapq.heappop(heap))
  return out 

def kClosestNumber(a,x,k):
  temp=[]
  heap=[]
  for i in range(len(a)):
    heapq.heappush(heap,[-1*abs(a[i]-x),a[i]])
    if len(heap)>k:
      heapq.heappop(heap)
  print(heap)
  while(len(heap)>0):
    temp.append(heapq.heappop(heap)[1])
  print(temp)

def kFreq(a,k):
  d={}
  temp=[]
  for i in range(len(a)):
    if a[i] in d:
      d[a[i]]+=1
    else:
      d[a[i]]=1
  print(d)
  heap=[]
  for i in d:
    heapq.heappush(heap,[d[i],i])
    if len(heap)>k:
      heapq.heappop(heap)
  print(heap)
  while(len(heap))>0:
    temp.append(heapq.heappop(heap)[1])
  return temp

def FreqSort(a):
  d={}
  temp=[]
  for i in range(len(a)):
    if a[i] in d:
      d[a[i]]+=1
    else:
      d[a[i]]=1
  print(d)
  heap=[]
  for i in d:
    heapq.heappush(heap,[-1*(d[i]),i])
    
  print(heap)
  while(len(heap))>0:
    x=heapq.heappop(heap)
    temp+=([x[1]]*abs(x[0]))
  return temp
class FindMedian:
  def __init__(self):
    self.small=[]
    self.large=[]
  def addNum(self,num):
    heapq.heappush(self.small,-1*num)
    if self.small and self.large and (-1*self.small[0])>self.large[0]:
      heapq.heappush(self.large,(-1*heapq.heappop(self.small)))
    if len(self.small)>len(self.large)+1:
      heapq.heappush(self.large,(-1*heapq.heappop(self.small)))
    if len(self.large)>len(self.small)+1:
      heapq.heappush(self.small,(-1*heapq.heappop(self.large)))
  def findMedian(self):
    if len(self.large)>len(self.small):
      return self.large[0]
    if len(self.large)<len(self.small):
      return self.small[0]
    return (-1*self.small[0]+self.large[0])//2

# a=[3,4,7,10,15,20]
# k=3
# print(kthLargest(a,k))
# print(kthSmallest(a,k))

# a=[6,5,3,2,8,10,9]
# k=3
# print(sortkSorted(a,k))

# a=[5,6,7,8,9]
# x=7
# k=3
# print(kClosestNumber(a,x,k))

a=[1,1,1,3,2,2,4]
k=2
# print(kFreq(a,k))
print(FreqSort(a))