def ss(arr,r,c,maxi):
    if r==0:
        return arr
        
    if c<r:
        if arr[maxi]<arr[c]:
            maxi=c
        return ss(arr,r,c+1,maxi)
    else:
        arr[r-1],arr[maxi]=arr[maxi],arr[r-1]
        return ss(arr,r-1,0,0)

arr=[4,2,3,1,0]
print(ss(arr,len(arr),0,0))
#original obj(array) is changed so no need to return fm ss as in line 14,11,8,3 only make call no return type |3->return;
print(arr)