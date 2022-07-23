def nextLargest(a):
  stack = []
  out=[]
  for i in range(len(a)-1,-1,-1): #reverse iteration 
    print(a[i])
    if len(stack)==0:
      out.append(-1)
      
    elif (len(stack)>0 and stack[-1]>a[i]):
      out.append(stack[-1])
    elif (len(stack)>0 and stack[-1]<=a[i]):
      while(len(stack)>0 and stack[-1]<=a[i]):
        stack.pop()
      if len(stack)==0:
        out.append(-1)
      else:
        out.append(stack[-1])
    print(stack)
    stack.append(a[i])
  out.reverse()

  return out


a=[1,3,2,4]
print(nextLargest(a))