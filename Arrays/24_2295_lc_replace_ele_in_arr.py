def repEle(arr,op):
  d={}
  for i in range(len(arr)):
      d[arr[i]]=i
  print(d)

  for i in range(len(op)):
    k=d[op[i][0]]
    print(k)
    d.pop(op[i][0])
    arr[k]=op[i][1]
    print(arr)
    d[op[i][1]]=i
    print(d)

arr=[1,2,4,6]
op=[[1,3],[4,7],[6,1]]
repEle(arr,op)