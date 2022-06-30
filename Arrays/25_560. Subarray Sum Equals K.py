# brute force
c=0
arr=[]
nums=[10, 2, -2, -20, 10]
t=-10

for i in range(len(nums)):
    temp=0
    for j in range(i,len(nums)):
        temp+=nums[j]
        if temp==t:
            c+=1
            arr.append([nums[i],i,nums[j],j])
            
print(arr)
print(c)