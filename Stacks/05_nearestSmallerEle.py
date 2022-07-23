def nearestsmalllestToLeft(a):
    stack=[]
    out=[]
    for i in range(len(a)):
        if len(stack)==0:
            out.append(-1)
        elif len(stack)>0 and a[i]>stack[-1]:
            out.append(stack[-1])
        elif len(stack)>0 and a[i]<=stack[-1]:
            while len(stack)>0 and a[i]<stack[-1]:
                stack.pop()
            if len(stack)==0:
                out.append(-1)
            else:
                out.append(stack[-1])
        stack.append(a[i])
    return out
        
    
    
a=[4,5,2,10,8]
print(nearestsmalllestToLeft(a))