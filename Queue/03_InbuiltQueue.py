#using collections class
from collections import deque

customQueue=deque(maxlen=3)#if param is not specified then queue is aurbitary length
print(customQueue)
customQueue.append(1)
customQueue.append(2)
customQueue.append(3)
print(customQueue)
print(customQueue.popleft())
print(customQueue)
print(customQueue.clear())
print(customQueue)
