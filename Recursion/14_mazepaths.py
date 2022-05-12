from turtle import left, right


def path(p,r,c):
  if r==1 and c==1:
    print(p)
    return
  if r>1:
    path(p+'D',r-1,c)

  if c>1:
    path(p+'R',r,c-1)

def pathRetLst(p,r,c):
  if r==1 and c==1:
    lst=[]
    lst.append(p)
    return lst

  left=list()
  right=list()
  if r>1:
    left=pathRetLst(p+'D',r-1,c)

  if c>1:
    right=pathRetLst(p+'R',r,c-1)

  left+=right
  return left

print(pathRetLst('',3,3))