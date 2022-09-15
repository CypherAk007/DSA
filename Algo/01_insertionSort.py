# arr = [9,1,5,2,7,8]
# for i in range(0,len(arr)):
#   key = arr[i]
#   j=i-1
#   while j>=0 and arr[j]>key:
#     arr[j+1]=arr[j]
#     j-=1
#   arr[j+1]=key

# for i in arr:
#   print(i)

def inssort(arr,n):
  for i in range(n):
    temp=arr[i]
    j=i-1
    while(j>=0 and arr[j]>temp):
      arr[j+1]=arr[j]
      j-=1
    arr[j+1]=temp 
  return arr 







arr = [9,1,5,2,7,8]
print(inssort(arr,len(arr)))