# mycode
def bubbleSort(arr,n):
  l=n-1
  while(l!=0):
    for i in range(0,l+1):
      if i+1<=l and arr[i]>arr[i+1]:
        arr[i],arr[i+1]=arr[i+1],arr[i]
    l-=1
  return arr 

def bubbleSortoriginal(arr,n):
  for i in range(n):
    for j in range(0,n-1-i):
      if arr[j]>arr[j+1]:
        arr[j],arr[j+1]=arr[j+1],arr[j]
  return arr 

# preForRecursionBubbleSort
def star(r,c):
  if r==0:
    return 
  if c<r:
    print('*',end=' ')
    star(r,c+1)
  else:
    print()
    star(r-1,0)

def bs(r,c,a):
  if r==0:
    return a
  if c<r:
    if a[c]>a[c+1]:
      a[c],a[c+1]=a[c+1],a[c]
    return bs(r,c+1,a)
  else:
    return bs(r-1,0,a)




arr=[-2,0,11,-9,45]
print(bubbleSort(arr,len(arr)))
print(bubbleSortoriginal(arr,len(arr)))
star(4,0)
a=[-2,0,11,-9,45]
print(a)
print(bs(len(a)-1,0,a))
print(a)
  