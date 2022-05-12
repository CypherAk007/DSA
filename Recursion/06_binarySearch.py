def bs(arr,t,s,e):
    if s>e:
        return -1
    
    m=s+(e-s)//2
    if arr[m]==t:
        return m
    if arr[m]>t:
        return bs(arr,t,s,m-1)
    return bs(arr,t,m+1,e)

if __name__=='__main__':
    arr=[1,2,3,4,55,66,78]
    t=7
    print(bs(arr,t,0,len(arr)-1))