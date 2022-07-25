# import 01_TreeBasics


# tree.root = build_product_tree()
# # print(root.get_level()) # 0
# tree.root.print_tree()

# class Stack:
#     def __init__(self):
#         self.stack=[]
    
#     def push(self,x):
#         self.stack.append(x)
    
#     def pop(self):
#         x=self.stack[-1]
#         self.stack.pop()
#         return x 
        
#     def top(self):
#         return self.stack[-1]
    
#     def size(self):
#         return len(self.stack)
    
#     def printf(self):
#         self.stack.reverse()
#         print(self.stack)
        
# from sys import maxsize


# class Queue:
#   def __init__(self,maxsize):
#     self.queue=[None]*maxsize 
#     self.front=-1
#     self.rear=-1
#     self.maxsize = maxsize

#   def getLen(self):
#     if self.rear==-1 and self.front==-1:
#       return 0
#     return self.rear-self.front+1

#   def enqueue(self,x):
#     if self.rear==-1 and self.front==-1:
#       self.rear=0
#       self.front=0
#       self.queue[self.rear]=x 
#     elif self.rear+1%self.maxsize==self.front:
#       print("queue is full")
#       return "queue is full"
#     else:
#       self.rear+=1
#       self.queue[self.rear]=x 

#   def dequeue(self):
#     if not self.getLen():
#       x=self.queue[self.front]
#       self.queue[self.front]=None 
#       self.front+=1
#     else:
#       return 'queue is empty'

#   def printf(self):
#     print(self.queue)

#   def frontf(self):
#     print(self.front,self.queue[self.front])

# q=Queue(5)
# q.enqueue(10)
# q.enqueue(20)
# q.enqueue(30)
# q.enqueue(40)
# q.enqueue(50)
# q.frontf()
# q.enqueue(50)
# q.enqueue(50)
# q.printf()
# print(q.getLen())



class Add:
  def __init__(self):
    self.a=[]
    self.b=[]
  def add(self):
    for i in range(5):
      self.a.append((i))
    print(self.a)
    self.b=self.a
    self.b[0]=1000
    print(self.b)

sol=Add()
sol.add()


