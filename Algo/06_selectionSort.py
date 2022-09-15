def selsort(arr,n):
  for i in range(0,n):
    mini=i
    for j in range(i+1,n):
      if arr[j]<arr[mini]:
        mini=j 
    if mini!=i:
      arr[i],arr[mini]=arr[mini],arr[i]
  return arr 

def selsortrec(r,c,maxi,a):
  if r==0:
    return 
  if c<r:
    if a[c]>a[maxi]:
      selsortrec(r,c+1,c,a)
    else:
      selsortrec(r,c+1,maxi,a)
  else:
    a[r-1],a[maxi]=a[maxi],a[r-1]
    selsortrec(r-1,0,0,a)
  


arr=[9,1,5,2,7,8]   #[1, 2, 5, 7, 8, 9]
print(selsort(arr,len(arr)))
a=[9,1,5,2,7,8]
print(a)
selsortrec(len(a),0,0,a)
print(a)
