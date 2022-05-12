# kadan's Algo -TC O(n) SC O(1)
from re import S


class Solution:
    def maxSubArray(self, nums):
      #  the final start and end position of the maximum sum subarray
        start=0
        end=0
        s=0 #the temporary start position
        maxi=float('-inf')
        curSum=0
        for i in range(len(nums)):
            curSum+=nums[i]
            if curSum>maxi:
                maxi=curSum
                start=s#tells fm where to where is the maximum subarray
                end=i
            if curSum<0:
                curSum=0
                s=i+1
        return maxi,start,end