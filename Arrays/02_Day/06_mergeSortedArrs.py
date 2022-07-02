'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
def mergeSortedArrays(nums1, m, nums2, n):
    if len(nums1)==0:
        print(nums2)
        return nums2
    elif len(nums2)==0:
        print(nums1)
        return nums1
    i=0
    while(i<m):
        if nums1[i]>nums2[0]:
            nums1[i],nums2[0]=nums2[0],nums1[i]
# sort the arr2 due to swap the non dec order is distrubed
            nums2.sort()
            i+=1
        else:
            i+=1
    #now take the ele of nums2 and put in nums1
    start=m
    k=0
    while(start<len(nums1) and k<n):
        nums1[start]=nums2[k]
        start+=1
        k+=1
    print(nums1)    
    
# nums1 = [1,2,3,0,0,0]
# m = 3
# nums2 = [2,5,6]
# n = 3

nums1 = []
m = 0
nums2 = [1]
n = 1
mergeSortedArrays(nums1, m, nums2, n)