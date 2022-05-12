def bs(arr,r,c):
    if r==0:
        return arr
    if c<r:
        if arr[c]>arr[c+1]:
            arr[c],arr[c+1]=arr[c+1],arr[c]
        return bs(arr,r,c+1)
    else:
        return bs(arr,r-1,0)
        
arr=[4,3,2,1,0]
print(bs(arr,len(arr)-1,0))