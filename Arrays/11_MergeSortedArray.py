# Merge Sorted Array using insertion sort type algo (strver - arr-II(3) , leet-88)
def merge(nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i=0
        
        while(i<m):
            if nums1[i]>nums2[0]:
                nums1[i],nums2[0]=nums2[0],nums1[i]
                i+=1
                print(nums1,nums2)
                nums2.sort()#after swapping the array2 is not sorted
            else:
                i+=1
        
                
nums1=[1,4,7,8,10]
nums2=[2,3,9]
merge(nums1,len(nums1),nums2,len(nums2))
print(nums1,nums2)