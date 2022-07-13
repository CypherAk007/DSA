def largeSubArrSum(a,k):
    i=0
    j=0
    mx=float('-inf') #stores the max window size (max size of subarr of value = k)
    summ=0
    while(j<len(a)):
        
        # 1-> calculations 
        summ = summ +a[j]

        if (summ)<k:
            j+=1
        
        elif (summ)==k:
            
            mx = max(mx,j-i+1)
            j+=1 # we are moving the pointer to find more elements
        elif summ>k:
            while summ>k:
                summ=summ-a[i]
                i+=1
                # if summ==k:
                #     mx = max(mx,j-i+1)
            
            j+=1
            
    if mx==float('-inf'):
        return 0
    return mx
            

a=[4,1,1,1,2,3,5]
k=5 #sum = 5
print(largeSubArrSum(a,k))
# Input 1:
#     A = [4,1,1,1,2,3,5]
#     B = 5
# Output 1:
#     C = 4 . 