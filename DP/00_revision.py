from copy import copy

def stairs(t,p,res):
    if t==0:
        res.append(p)
        return 
    for i in range(1,t+1):
        if i<=t:
            stairs(t-i,p+str(i),res)

# 0 1 1 2 3 5 8 13 21
class Fibo:
    def fib(self,n):
        if n<=1:
            return n 
        return self.fib(n-1)+self.fib(n-2)

    def fibmemo(self,n):
        dp=[-1]*(n+1)
        return self.fibmemohelper(n,dp)
    
    def fibmemohelper(self,n,dp):
        dp[0]=0
        if n>=1:
            dp[1]=1 
        if dp[n]!=-1:
            return dp[n]
        dp[n]=self.fibmemohelper(n-1,dp)+self.fibmemohelper(n-2,dp)
        return dp[n]
    
    def fibtab(self,n):
        dp=[-1]*(n+1)
        return self.fibtabhelper(n,dp)
    
    def fibtabhelper(self,n,dp):
        dp[0]=0
        if n>=1:
            dp[1]=1 
        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]
            # print(dp[i])
        # print(dp)
        return dp[n]
        
    def fibtab(self,n):
        dp=[-1]*(n+1)
        return self.fibtabhelper(n,dp)
    
    def fibtabhelper(self,n,dp):
        dp[0]=0
        if n>=1:
            dp[1]=1 
        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]
            # print(dp[i])
        # print(dp)
        return dp[n]
    
    def fibtabs(self,n):
        dp=[-1]*(n+1)
        return self.fibtabshelper(n,dp)
    
    def fibtabshelper(self,n,dp):
        prev2=0
        prev1=1 
        if n==0:
            return prev2
        for i in range(2,n+1):
            cur=prev1+ prev2
            prev2=prev1 
            prev1=cur
        return prev1
                  
class climb:            
    def stairsCombi(self,t):
        candidates=[]
        for i in range(1,t+1):
            candidates.append(i)
        print(candidates)
        temp=[]
        res=[]
        self.stairshelper(t,temp,res,0,candidates)
        return res
        
    def stairshelper(self,target,temp,res,i,candidates):
        if target==0:
            res.append(copy(temp))
            return
        if target<0:
            return 
        if i==len(candidates):
            return 
        self.stairshelper(target,temp,res,i+1,candidates)
        
        temp.append(candidates[i])
        self.stairshelper(target-candidates[i],temp,res,i,candidates)
        temp.pop()
    
    def climbingStairs(self,n):
        if n==0:
            return 1
        if n==1:
            return 1 
        left=self.climbingStairs(n-1)
        right=self.climbingStairs(n-2)
        return left+right
    
    def climbingStairs2(self,n,p):
        if n==0:
            print(p)
            return 1
        if n==1:
            
            return 1 
        left=self.climbingStairs2(n-1,p+str(1))
        right=self.climbingStairs2(n-2,p+str(2))
        return left+right
        
    def frogJump(self,n,heights):
        return self.frogHelper(n-1,heights)
    def frogHelper(self,idx,heights):
        if idx==0:
            return 0
        left=self.frogHelper(idx-1,heights)+abs(heights[idx]-heights[idx-1])
        right=float('inf')
        if idx>1:
            right=self.frogHelper(idx-2,heights)+abs(heights[idx]-heights[idx-2])
        return min(left,right)
        
        
    def frogJumpdp(self,n,heights):
        dp=[-1]*(n+1)
        return self.frogHelperdp(n-1,heights,dp)
    def frogHelperdp(self,idx,heights,dp):
        if idx==0:
            return 0
        if dp[idx]!=-1:
            return dp[idx]
        left=self.frogHelperdp(idx-1,heights,dp)+abs(heights[idx]-heights[idx-1])
        right=float('inf')
        if idx>1:
            right=self.frogHelperdp(idx-2,heights,dp)+abs(heights[idx]-heights[idx-2])
        dp[idx]=min(left,right)
        return dp[idx]
    def fjump(self,n):
        if n<=1:
            return 1 
        l=self.fjump(n-1)
        r=self.fjump(n-2)
        return l+r 
        
    def fjmemo(self,n):
        dp=[-1]*(n+1)
        return self.fjmhelper(n,dp)
        
    def fjmhelper(self,n,dp):
        if n<=1:
            return 1 
        l=self.fjmemo(n-1)
        r=self.fjmemo(n-2)
        dp[n]=l+r
        # print(dp)
        return dp[n] 
        
    def fjtab(self,n):
        dp=[-1]*(n+1)
        return self.fjmtabhelper(n,dp)
        
    def fjmtabhelper(self,n,dp):
        dp[0]=1 
        if n>=1:
            dp[1]=1 
        for i in range(2,n+1):
            l=dp[i-1]
            r=dp[i-2]
            dp[i]=l+r
            # print(dp)
        return dp[n] 
        
    def fjtabs(self,n):
        
        return self.fjmtabshelper(n)
        
    def fjmtabshelper(self,n):
        prev2=1
        prev1=1 
        if n==0:
            return prev2
        for i in range(2,n+1):
            l=prev1
            r=prev2
            cur=l+r
            # print(cur)
            prev2=prev1 
            prev1=cur
        return prev1
        
    def adj(self,idx,nums):
        if idx==0:
            return nums[idx]
        if idx<0:
            return 0
        p=nums[idx]+self.adj(idx-2,nums)
        np=0+self.adj(idx-1,nums)
        return max(p,np)
    
    def adjmemo(self,idx,nums):
        dp=[-1]*(idx+1)
        return self.adjmemohelper(idx,nums,dp)
    
    def adjmemohelper(self,idx,nums,dp):
        dp[0]=nums[0]
        if idx<0:
            return 0 
        if dp[n]!=-1:
            return dp[n]
        p=nums[idx]+self.adj(idx-2,nums)
        np=0+self.adj(idx-1,nums)
        dp[n]=max(p,np)
        return dp[n]
        
    def adjmemot(self,idx,nums):
        dp=[-1]*(idx+1)
        return self.adjmemohelpert(idx,nums,dp)
    
    def adjmemohelpert(self,idx,nums,dp):
        dp[0]=nums[0]
        for i in range(1,n+1):
            p=nums[idx]+self.adj(idx-2,nums)
            np=0+self.adj(idx-1,nums)
            dp[n]=max(p,np)
        return dp[n]
        
    def adjmemot(self,idx,nums):
        return self.adjmemohelpert(idx,nums)
    
    def adjmemohelpert(self,idx,nums,dp):
        dp[0]=nums[0]
        for i in range(1,n+1):
            p=nums[idx]+self.adj(idx-2,nums)
            np=0+self.adj(idx-1,nums)
            dp[n]=max(p,np)
        return dp[n]
# arr=''
# res=[]
# t=3
c=climb()
# stairs(t,arr,res)
# print(res)
# print(c.stairsCombi(t))
# print(c.climbingStairs(t))
# print(c.climbingStairs2(t,''))
n=6
heights=[30,10,60,10,60,50]
print(c.frogJump(n,heights))
print(c.frogJumpdp(n,heights))