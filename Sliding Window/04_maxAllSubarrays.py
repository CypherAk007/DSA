# Maximum of all subarrays of size k | Sliding Window| Fixed size as K is given

def maxOfAllSubArr(a,k):
    i=0
    j=0
    ans=[]
    lst=[]
    while(j<len(a)):
        
        # 1-> calculations 
        # if lstback ele is <a[j] then pop it and then store in lst
        while(len(lst)>0 and lst[len(lst)-1]<a[j]):
            lst.pop(len(lst)-1)
        lst.append(a[j])
        
        if (j-i+1)<k:
            j+=1
        
        elif (j-i+1)==k:
            # 2-> remove ans fm calculations
            ans.append(lst[0])#front of lst is append as that is maxele of that window
            
            # 3-> before moving the window ie we have to remove the calculations made by i
            if a[i]==lst[0]:
                lst.pop(0)
            i+=1
            j+=1
            
    return ans
            

a=[1, 3, -1, -3, 5, 3, 6, 7]
k=3
print(maxOfAllSubArr(a,k))
# Input 1:
#     A = [1, 3, -1, -3, 5, 3, 6, 7]
#     B = 3
# Output 1:
#     C = [3, 3, 5, 5, 6, 7] . 