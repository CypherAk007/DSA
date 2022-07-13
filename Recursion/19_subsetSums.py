def sub(p,up):
  if len(up)==0:
    lst=[]
    lst.append(p)
    return lst 
  
  digit=up[0]
  l=sub(p.append(digit),up[1:])
  r=sub(p,up[1:])
  l+=r
  return l 

def sub1(p,a,idx):
  if idx==len(a):
    lst=[]
    lst.append(p)
    return lst 

  l=sub1(p+a[idx],a,idx+1)
  r=sub1(p,a,idx+1)
  l+=r 
  return l

def sub2(p,up):
  if len(up)==0:
    print(p)
    return 
  digit=up[0]
  print(digit)
  if p!=None:
    sub2(p.append(digit),up[1:])
  sub2(p,up[1:])
up=[2,3]
p=0
# print(sub(p,up))
# sub2(p,up)
print(sub1(p,up,0))