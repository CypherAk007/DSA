# 1365. How Many Numbers Are Smaller Than the Current Number
def cn(arr):
  out =arr[:]
  out.sort()
  print(arr)
  d={}
  lst=[]
  for i in range(len(out)):
    if out[i] not in d:
      d[out[i]]=i
  for i in arr:
    lst.append(d[i])
  return lst

print(cn([8,1,2,2,3]))