def qs(arr,low,high):
    if low>=high:
        return
    s=low
    e=high
    mid=s+(e-s)//2
    pivot=arr[mid]
    
    while(s<=e):
        while(arr[s]<pivot):
            s+=1
            
        while(arr[e]>pivot):
            e-=1
            
        if(s<=e):
            arr[s],arr[e]=arr[e],arr[s]
            s+=1
            e-=1
            
    qs(arr,low,e)
    qs(arr,s,high)
    

arr=[4,3,2,1]  
low=0
high=len(arr)-1
qs(arr,low,high)       
print(arr)