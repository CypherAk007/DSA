def pad(p,up):
  if len(up)==0:
    print(p)
    return
  digit=int(up[0])
  for i in range((digit-1)*3,digit*3):
    ch=chr(97+i) # convert ascii to charcter
    pad(p+ch,up[1:])


def padlst(p,up):
  if len(up)==0:
    lst=list()
    lst.append(p)
    return lst
  
  digits=int(up[0])
  x=list()
  for i in range((digits-1)*3,digits*3):
    ch=chr(97+i)
    out=padlst(p+ch,up[1:])
    x+=out
  return x

def padCount(p,up):
  if len(up)==0:
    return 1
  count=0
  digit=int(up[0])
  for i in range((digit-1)*3,digit*3):
    ch=chr(97+i) # convert ascii to charcter
    count= count+ padCount(p+ch,up[1:])
  return count



p=''
up='12'
print(padlst(p,up))
print(padCount(p,up))