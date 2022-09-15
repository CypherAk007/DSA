def part(arr,p):
  i=0
  j=0
  while(i<len(arr)):
    if arr[i]>p:
      i+=1
    else:
      arr[i],arr[j]=arr[j],arr[i]
      i+=1
      j+=1
  return arr 

arr=[7,9,4,8,3,6,7,8,5]
print(part(arr,5))