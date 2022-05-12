# mycode
# given two sorted list
a=[1,2,3,5,8,11]
b=[2,3,5,6,9,10,13,14]
aLen=len(a)
bLen=len(b)
c=[0]*(aLen+bLen)
i=j=k=0

while(i!=aLen and j!=bLen):
  if a[i]<=b[j]:
    c[k]=a[i]
    i+=1
    k+=1
  else:
    c[k]=b[j]
    j+=1
    k+=1

while(i!=aLen):
  c[k]=a[i]
  i+=1
  k+=1
while(j!=bLen):
  c[k]=b[j]
  j+=1
  k+=1

print(c)


