# 2035 Partition Array Into Two Arrays to Minimize Sum Difference

class Solution:
    def minimumDifference(self, nums):
        totSum=sum(nums)
        n=len(nums)
        dp=[[False]*(totSum+1) for i in range(n)]
        self.subsetSumTab(totSum,nums,dp)
        
        # dp[n-1][col->0,1,...totsum]
        mini=float('inf')
        for i in range(0,totSum+1):
            if dp[n-1][i]==True:
                s1=i
                s2=totSum-i
                mini=min(mini,abs(s2-s1))
        return mini

    ###UNABLE TO HANDLE THE -VE NUMBERS...

    def subsetSumTab(self,k,a,dp):
        n=len(a)
        for i in range(0,n):
            dp[i][0]=True
        if a[0]<=k:
            dp[0][a[0]]=True
        for idx in range(1,n):
            for target in range(1,k+1):
                np=dp[idx-1][target]
                p=False
                if a[idx]<=target:
                    p=dp[idx-1][target-a[idx]]
                dp[idx][target]=np or p
        return dp[n-1][k]


s=Solution()
a=[3,2,7]
print(s.minimumDifference(a)) #op=>2
