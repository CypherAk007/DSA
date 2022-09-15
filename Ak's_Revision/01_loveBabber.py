# Input: arr[] = {3, 5, 4, 1, 9}
# Output: Minimum element is: 1
#               Maximum element is: 9
def minmax(arr,n):
    mini=float('inf')
    maxi=float('-inf')
    for i in range(n):
        if arr[i]>maxi:
            maxi=arr[i]
        elif arr[i]<mini:
            mini=arr[i]
    return mini,maxi 
    
arr=[3, 5, 4, 1, 9]
print(minmax(arr,len(arr)))
