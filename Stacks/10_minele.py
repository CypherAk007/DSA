def getMinEle(s,ss):
  if len(ss)==0:
    print(-1)
    return -1
  print(s[-1])
  return s[-1]

def push(a,s,ss):
  s.append(a)
  if len(ss)==0 or ss[-1]>a:
    ss.append(a)
  return 

def pop(s,ss):
  if len(s)==0:
    print(-1)
    return -1
  ans =s[-1]
  s.pop()
  if ss[-1]==ans:
    ss.pop()
  print(ans)
  return ans 


if __name__== "__main__":
  s=[]
  ss=[]
  pop(s,ss)
  push(3,s,ss)
  getMinEle(s,ss)