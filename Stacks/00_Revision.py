def NGR(a):
  s=[]
  out=[]
  for i in range(len(a)-1,-1,-1):
    if len(s)==0:
      out.append(-1)
    elif len(s)>0 and s[-1]>a[i]:
      out.append(s[-1])
    elif len(s)>0 and s[-1]<=a[i]:
      while(len(s)>0 and s[-1]<=a[i]):
        s.pop()
      if len(s)==0:
        out.append(-1)
      else:
        out.append(s[-1])
    s.append(a[i])
  out.reverse()
  return out 


def NGL(a):
  s=[]
  out=[]
  for i in range(len(a)):
    if len(s)==0:
      out.append(-1)
    elif len(s)>0 and s[-1]>a[i]:
      out.append(s[-1])
    elif len(s)>0 and s[-1]<=a[i]:
      while(len(s)>0 and s[-1]<=a[i]):
        s.pop()
      if len(s)==0:
        out.append(-1)
      else:
        out.append(s[-1])
    s.append(a[i])
  
  return out 

def NSL(a):
  s=[]
  out=[]
  for i in range(len(a)):
    if len(s)==0:
      out.append(-1)
    elif len(s)>0 and s[-1]<a[i]:
      out.append(s[-1])
    elif len(s)>0 and s[-1]>=a[i]:
      while(len(s)>0 and s[-1]>=a[i]):
        s.pop()
      if len(s)==0:
        out.append(-1)
      else:
        out.append(s[-1])
    s.append(a[i])
  
  return out 

def NSR(a):
  s=[]
  out=[]
  for i in range(len(a)-1,-1,-1):
    if len(s)==0:
      out.append(-1)
    elif len(s)>0 and s[-1]<a[i]:
      out.append(s[-1])
    elif len(s)>0 and s[-1]>=a[i]:
      while(len(s)>0 and s[-1]>=a[i]):
        s.pop()
      if len(s)==0:
        out.append(-1)
      else:
        out.append(s[-1])
    s.append(a[i])
  out.reverse()
  return out 

# stock Span Prob
def ssp(a):
  s=[]
  v=[]
  for i in range(len(a)):
    if len(s)==0:
      v.append(-1)
    elif len(s)>0 and s[-1][0]>a[i]:
      v.append(s[-1][1])
    elif len(s)>0 and s[-1][0]<=a[i]:
      while(len(s)>0 and s[-1][0]<=a[i]):
        s.pop()
      if len(s)==0:
        v.append(-1)
      else:
        v.append(s[-1][1])
    s.append([a[i],i])
  for i in range(len(v)):
    v[i]=i-v[i]
  return v



# a=[1,3,0,0,1,2,4]
# print(NGR(a))
# a=[1,3,2,4]
# print(NGL(a))
# a=[4,5,2,10,8]
# print(NSL(a))
# print(NSR(a))

# a=[100,80,60,70,60,75,85]
# print(ssp(a))