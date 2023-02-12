class Node:
    def __init__(self,data):
        self.data = data 
        self.next=None 
        self.prev=None
        
class Stackm:
    def __init__(self):
        node=Node(-1)
        self.head = node  
        self.mid=node  
        self.count=0

def createMyStack():
    ms=Stackm()
    return ms 
    

def push(ms,val):
    cur=Node(val)
    cur.prev=None 
    cur.next=ms.head 
    ms.count+=1 
    ms.head.prev=cur
    ms.head=cur 
    if ms.count==1:
        ms.mid=cur
    elif ms.count%2==0:
        ms.mid=ms.mid.prev
        
def pop(ms):
    if ms.count==0:
        print('stack empty')
        return -1 
        
    x=ms.head.data
    ms.head=ms.head.next
    if ms.head!=None:
        ms.head.prev=None 
    ms.count-=1 
    if ms.count%2==1:
        ms.mid=ms.mid.next 
    print('poped ele is :',x)
    return x 
        
def middle(ms):
    if ms.count==0:
        print('stack is empty')
        return -1 
    
    return ms.mid.data 

def printdata(ms):
    cur=ms.head
    if ms.count==0:
        print('stack is empty')
        return 
    
    for i in range(ms.count):
        print(cur.data)
        cur=cur.next 


if __name__=='__main__':
    st=Stackm()
    # print(st.head)
    push(st,1)
    push(st,2)
    push(st,3)
    push(st,4)
    push(st,5)
    
    printdata(st)
    print('mid ele is:',middle(st))
    print()
    pop(st)
    pop(st)
    
    printdata(st)
    print('mid ele is:',middle(st))
    print()
