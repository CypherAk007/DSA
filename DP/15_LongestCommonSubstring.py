class Solution:
  def longestCommonSubsequence(self, text1, text2):
    n=len(text1)
    m=len(text2)
    
    # dp=[[-1]*(m) for i in range(n)]
    dp=[[0]*(m+1) for i in range(n+1)]
    
    # return self.helper(n-1,m-1,text1,text2,dp) replace n-1 and m-1 with n,m(shifting indexes)
    return self.helper(text1,text2,dp)
    # return self.helperSpace(text1,text2)
  
  # i===i-1 and j===j-1
  # Tabulation
  def helper(self,text1,text2,dp):
    # bc
    n=len(text1)
    m=len(text2)
    for j in range(0,m+1):
      dp[0][j]=0
    for i in range(0,n+1):
      dp[i][0]=0
    
    ans=0
    for idx1 in range(1,n+1):
      for idx2 in range(1,m+1):
        if text1[idx1-1]==text2[idx2-1]:
          dp[idx1][idx2]=1 + dp[idx1-1][idx2-1]
          ans=max(ans,dp[idx1][idx2])
        else:
          dp[idx1][idx2]=0
    return ans

  # Tabulation+Space Optimized(Wrong ans.)
  def helperSpace(self,text1,text2):
    # bc
    n=len(text1)
    m=len(text2)
    prev=[0]*(m+1)
    cur=[0]*(m+1)
    
    ans=0
    for idx1 in range(1,n+1):
      for idx2 in range(1,m+1):
        if text1[idx1-1]==text2[idx2-1]:
          cur[idx2]= 1 + prev[idx2-1]
          ans=max(ans,cur[idx2])
        else:
          cur[idx2]=0
      print(prev,cur)
      prev=cur

    return ans


if __name__=='__main__':
  s=Solution()
  text1='abcjk'
  text2='acjkp'
  print(s.longestCommonSubsequence(text1, text2))