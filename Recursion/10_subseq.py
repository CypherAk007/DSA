def subseq(p,up):
  if len(up)==0:
    print(p)
    return
  
  ch=up[0]
  subseq(p+ch,up[1:])
  subseq(p,up[1:])

# return the list of subseq
def subSeqRet(p,up):
  if len(up)==0:
    lst=[]
    lst.append(p)
    return lst

  ch=up[0]
  left=subSeqRet(p+ch,up[1:])
  right=subSeqRet(p,up[1:])
  left=left+right
  return left


p=''
up='abc'
subseq(p,up)
print(subSeqRet(p,up))